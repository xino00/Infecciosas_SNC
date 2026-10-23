#!/usr/bin/env python3
"""Genera el MP3 del podcast a partir de guion.md con espeak-ng + MBROLA.

Requisitos (Ubuntu/Debian): apt-get install espeak-ng mbrola mbrola-es1 mbrola-es3 ffmpeg

Uso:
    python3 generar_audio.py                      # guion.md -> podcast_03_encefalitis.mp3
    python3 generar_audio.py --actualizar-marcas  # además reescribe las marcas [mm:ss] del guion

Las tablas de espeak-ng para las voces mb-es3 y mb-es4 están desalineadas con sus
bases MBROLA (p. ej., la «r» simple sale como «h» en es3), y las de es1/es2 emiten
«e/» y «o/», que esas bases no tienen. Por eso los fonemas se generan siempre con la
tabla de mb-es1 (en SAMPA), se traducen al inventario de cada voz y se sintetizan
llamando directamente a mbrola.
"""

import argparse
import math
import re
import struct
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TASA = 22050  # Hz, mono, 16 bits

MBROLA = Path("/usr/share/mbrola")

# Personaje -> (base MBROLA, factor de tono). La prosodia sale de mb-es1 (voz
# masculina), así que la voz femenina es3 se sube de tono.
VOCES = {"ANA": ("es3", 1.8), "LUIS": ("es1", 1.0)}

# Fonemas de la tabla de mb-es1 que cada base no tiene. es3 es seseante y yeísta y
# carece de «ch», «ñ», «rr» y de la yod tras consonante: se aproximan.
COMUN = {"e/": ["e"], "o/": ["o"]}
TRADUCCION = {
    "es1": {"w": ["u"]},
    "es3": {"x": ["H"], "T": ["s"], "L": ["j"], "jj": ["i"], "rr": ["R"], "w": ["u"],
            "J": ["n", "j"], "tS": ["t", "s"]},
}

PAUSA_TURNO = 0.45  # s entre intervenciones
PAUSA_BLOQUE = 0.9  # s antes y después de la sintonía de transición

# Pronunciación de siglas y nombres propios que espeak-ng lee mal en español.
# Se aplican en orden, como palabras completas.
PRONUNCIACION = [
    ("SARS-CoV-2", "sars cov dos"),
    ("RT-QuIC", "erre te quik"),
    ("Creutzfeldt-Jakob", "kroisfelt yákob"),
    ("Guillain-Barré", "guilán barré"),
    ("Epstein-Barr", "épstein bar"),
    ("West Nile", "güest nail"),
    ("Wernicke", "vérnique"),
    ("Ziehl", "cil"),
    ("hockey", "jóquei"),
    ("Mycobacterium", "micobacterium"),
    ("Cryptococcus", "criptococus"),
    ("Aspergillus", "aspergilus"),
    ("Brucella", "brucela"),
    ("Candida", "cándida"),
    ("ESCMID", "es ce eme i de"),
    ("SEMES", "Semes"),
    ("SEN", "Sen"),
    ("NICE", "nais"),
    ("FLAIR", "fléar"),
    ("NMDA", "ene eme de a"),
    ("CD20", "cedé veinte"),
    ("CD4", "cedé cuatro"),
    ("IgM", "i ge eme"),
    ("VIH", "uve i hache"),
    ("LCR", "ele ce erre"),
    ("PCR", "pe ce erre"),
    ("UCI", "uci"),
    ("ADA", "ada"),
    ("JC", "jota ce"),
    ("T2", "te dos"),
]


def leer_guion(ruta):
    """Devuelve una lista de bloques: (título, [(personaje, texto), ...])."""
    bloques = []
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## \[[^\]]*\] (.+)$", linea)
        if m:
            bloques.append((m.group(1).strip(), []))
            continue
        m = re.match(r"^\*\*(ANA|LUIS):\*\* (.+)$", linea)
        if m:
            if not bloques:
                sys.exit("Hay una intervención antes de la primera marca de bloque.")
            bloques[-1][1].append((m.group(1), m.group(2).strip()))
    return bloques


def preparar_texto(texto):
    texto = re.sub(r"[*_«»\"]", "", texto)
    for sigla, dicho in PRONUNCIACION:
        texto = re.sub(rf"(?<![\w-]){re.escape(sigla)}(?![\w-])", dicho, texto)
    return texto


def traducir_pho(pho, base):
    """Adapta un .pho de mb-es1 al inventario de la base y funde fonemas repetidos."""
    tabla = TRADUCCION.get(base, {})
    salida = []
    for linea in pho.splitlines():
        campos = linea.split("\t")
        if not linea.strip() or len(campos) < 2:
            continue
        nuevos = tabla.get(campos[0], COMUN.get(campos[0], [campos[0]]))
        if len(nuevos) == 1:
            campos[0] = nuevos[0]
            filas = [campos]
        else:
            dur = int(campos[1]) // len(nuevos)
            filas = [[f, str(dur)] for f in nuevos]
        for fila in filas:
            # «la anamnesis» -> a-a: la base no tiene difonos de un fonema consigo mismo.
            if salida and fila[0] != "_" and salida[-1][0] == fila[0]:
                salida[-1][1] = str(int(salida[-1][1]) + int(fila[1]))
            else:
                salida.append(fila)
    return "\n".join("\t".join(f) for f in salida) + "\n"


def sintetizar(texto, voz, velocidad, carpeta, n):
    """Sintetiza un turno y lo devuelve como muestras PCM de 16 bits a TASA Hz."""
    base, tono = voz
    bruto = carpeta / f"{n:03d}_bruto.wav"
    final = carpeta / f"{n:03d}.wav"
    pho = subprocess.run(
        ["espeak-ng", "-v", "mb-es1", "-s", str(velocidad), "-q", "--pho", texto],
        capture_output=True, text=True, check=True,
    ).stdout
    r = subprocess.run(
        ["mbrola", "-e", "-f", str(tono), str(MBROLA / base / base), "-", str(bruto)],
        input=traducir_pho(pho, base), capture_output=True, text=True,
    )
    if r.returncode != 0 or not bruto.exists() or bruto.stat().st_size < 1000:
        sys.exit(f"mbrola falló en el turno {n}: {(r.stderr + r.stdout).strip()[:300]}")
    avisos = (r.stderr + r.stdout).count("unknown, replaced")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(bruto), "-ac", "1", "-ar", str(TASA),
         "-sample_fmt", "s16", str(final)],
        check=True,
    )
    with wave.open(str(final), "rb") as w:
        return w.readframes(w.getnframes()), avisos


def silencio(segundos):
    return b"\x00\x00" * int(TASA * segundos)


def tonos(notas, duracion, volumen=0.18):
    """Sintonía sencilla: notas sucesivas (Hz) con envolvente suave."""
    out = bytearray()
    n = int(TASA * duracion)
    for f in notas:
        for i in range(n):
            env = math.sin(math.pi * i / n) ** 2
            s = volumen * env * (math.sin(2 * math.pi * f * i / TASA)
                                 + 0.3 * math.sin(4 * math.pi * f * i / TASA))
            out += struct.pack("<h", int(max(-1, min(1, s)) * 32767))
    return bytes(out)


SINTONIA_INICIO = tonos([523.25, 659.25, 783.99], 0.45)  # do-mi-sol
SINTONIA_BLOQUE = tonos([659.25, 783.99], 0.25, volumen=0.12)
SINTONIA_FIN = tonos([783.99, 659.25, 523.25], 0.45)


def mmss(segundos):
    s = int(round(segundos))
    return f"{s // 60:02d}:{s % 60:02d}"


def actualizar_marcas(ruta, inicios):
    lineas = ruta.read_text(encoding="utf-8").splitlines(keepends=True)
    i = 0
    for k, linea in enumerate(lineas):
        if re.match(r"^## \[[^\]]*\] ", linea):
            lineas[k] = re.sub(r"^## \[[^\]]*\]", f"## [{mmss(inicios[i])}]", linea)
            i += 1
    ruta.write_text("".join(lineas), encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--guion", type=Path, default=AQUI / "guion.md")
    p.add_argument("--salida", type=Path, default=AQUI / "podcast_03_encefalitis.mp3")
    p.add_argument("--velocidad", type=int, default=170, help="palabras por minuto de espeak-ng")
    p.add_argument("--actualizar-marcas", action="store_true",
                   help="reescribe las marcas [mm:ss] de cada bloque del guion")
    args = p.parse_args()

    bloques = leer_guion(args.guion)
    turnos = sum(len(t) for _, t in bloques)
    print(f"{len(bloques)} bloques, {turnos} intervenciones")

    audio = bytearray(SINTONIA_INICIO + silencio(0.6))
    inicios, avisos_total, n = [], 0, 0
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for b, (titulo, intervenciones) in enumerate(bloques):
            if b > 0:
                audio += silencio(PAUSA_BLOQUE) + SINTONIA_BLOQUE + silencio(PAUSA_BLOQUE)
            inicios.append(len(audio) / 2 / TASA)
            for personaje, texto in intervenciones:
                n += 1
                muestras, avisos = sintetizar(preparar_texto(texto), VOCES[personaje],
                                              args.velocidad, tmp, n)
                avisos_total += avisos
                audio += muestras + silencio(PAUSA_TURNO)
            print(f"  [{mmss(inicios[-1])}] {titulo}")
        audio += silencio(0.6) + SINTONIA_FIN

        mezcla = tmp / "mezcla.wav"
        with wave.open(str(mezcla), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(TASA)
            w.writeframes(bytes(audio))
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", str(mezcla), "-af", "loudnorm=I=-18:TP=-1.5",
             "-ar", str(TASA), "-ac", "1", "-codec:a", "libmp3lame", "-b:a", "56k",
             "-metadata", "title=Episodio 3: Encefalitis aguda del adulto",
             "-metadata", "album=Infecciosas del SNC en urgencias",
             "-metadata", "comment=Voz sintética. Material de estudio, no protocolo asistencial.",
             str(args.salida)],
            check=True,
        )

    print(f"Duración: {mmss(len(audio) / 2 / TASA)} · difonos sustituidos por MBROLA: {avisos_total}")
    print(f"Escrito: {args.salida}")
    if args.actualizar_marcas:
        actualizar_marcas(args.guion, inicios)
        print(f"Marcas actualizadas en {args.guion}")


if __name__ == "__main__":
    main()
