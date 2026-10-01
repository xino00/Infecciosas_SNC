# GUÍA DE ESTILO DE LOS APUNTES (extraída del modelo de NAC)

## Estructura fija de cada capítulo

1. **DEFINICIÓN Y FISIOPATOLOGÍA** — párrafo denso: qué es, mecanismo de entrada del patógeno, cascada inflamatoria, cómo se traduce en clínica y **cómo se establece el diagnóstico** (criterios). Cierra con el *diagnóstico diferencial frente a la entidad "hermana"* en cursiva.
2. **EPIDEMIOLOGÍA** — incidencia (Europa/España primero), ingreso, UCI, mortalidad y secuelas.
3. **ETIOLOGÍA** — patógenos por frecuencia; dato europeo vs. EE. UU. en cursiva cuando difiera.
4. **GRAVEDAD Y LUGAR DE TRATAMIENTO** — escalas/criterios, criterios de UCI.
   - **x.1 FACTORES DE RIESGO PARA AMPLIAR COBERTURA** — una lista por patógeno, con el factor en **MAYÚSCULAS NEGRITA** y la evidencia que lo sustenta en *cursiva*.
   - **x.x ¿Cuándo es OBLIGATORIO cubrir…?**
5. **TRATAMIENTO** — un subapartado por escenario clínico:
   - `---> PRIMERA ELECCIÓN:` familia en MAYÚSCULAS + **FÁRMACO dosis intervalo**.
   - `---> ALTERNATIVA:` (alergia, fracaso…).
   - Comentario farmacológico/evidencia en *cursiva*.
   - Terapia secuencial / desescalada, **duración**, **tratamiento adyuvante** (con los datos de evidencia que recojan las guías).
6. **ESTUDIOS MICROBIOLÓGICOS / PRUEBAS** — escalonado por gravedad (lo que se pide y lo que NO, y por qué).
7. **NOTAS PARA EL CONTEXTO ESPAÑOL Y EUROPEO** — viñetas: discrepancias entre las cuatro guías, resistencias locales, disponibilidad de fármacos.
8. **REFERENCIAS** — solo las cuatro fuentes: cita completa en negrita-cursiva + *nivel en la pirámide y qué aporta cada una*.

## Convenciones

- **Fuentes: solo cuatro**, en pirámide: **SEN 2023 → ESCMID 2016 → NICE NG240 2024 → SEMES 2012**. Ante una discrepancia manda la de más arriba; lo que no trata se toma de la siguiente. La discrepancia se anota en *cursiva*.
- **Cada dato se atribuye a su fuente** entre paréntesis: NICE con el número de recomendación (p. ej., NICE 1.4.7) y ESCMID con su grado (A-D). Los estudios primarios solo aparecen cuando los recoge alguna de las cuatro guías, y se citan a través de ella (p. ej., "la ESCMID resume la revisión Cochrane…").
- Negrita para conceptos y fármacos clave; MAYÚSCULAS para lo que hay que "ver de un vistazo" en urgencias.
- *Cursiva* = matiz, dato de evidencia o comentario de fondo (prescindible en lectura rápida).
- Dosis siempre con vía e intervalo (y ajuste en perfusión extendida/función renal si procede).
- Cuando la evidencia sea débil, contradictoria o el dato no esté verificado, **se indica explícitamente**.
- **Referencias**: solo las cuatro fuentes, con la cita completa en negrita-cursiva (PMID y DOI cuando existan) y debajo una explicación en *cursiva* de qué nivel ocupa en la pirámide y qué aporta al capítulo. No se dejan citas del tipo "probablemente corresponde a…".

## Formato Markdown

- Un archivo `.md` por capítulo en `apuntes/` (`01_Meningitis_bacteriana.md`, …).
- Título del capítulo con `#`; secciones numeradas con `##` (`## 1. DEFINICIÓN Y FISIOPATOLOGÍA`), subapartados con `###` (`### 4.1. …`) y `####` para el tercer nivel.
- Numeración real y correlativa (el ejemplo de NAC, exportado desde Word, repite "1." en todas las secciones y tiene restos de `****`; aquí no).
- Listas con `-` o `1.`; pautas de tratamiento como `- **---> PRIMERA ELECCIÓN:** …`.
- Tablas Markdown para comparativas (perfil de LCR, etiología por edad, dosis).
- Notas clave en bloque de cita `>`; nada de HTML.
