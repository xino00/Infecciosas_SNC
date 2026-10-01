# Infecciosas_SNC

Apuntes de **infecciones del sistema nervioso central (SNC) para urgencias**, centrados en el paciente adulto. Están pensados para consultarse a pie de cama: cada capítulo sigue la misma estructura y destaca en MAYÚSCULAS y negrita lo que hay que ver de un vistazo, y deja en *cursiva* los matices y los datos de evidencia.

> **Aviso**: son apuntes de estudio, no un protocolo asistencial. No sustituyen al juicio clínico ni a los protocolos y la epidemiología de cada centro. Comprueba siempre las dosis (y su ajuste a la función renal) antes de prescribir.

## Fuentes: solo cuatro, en pirámide

Todo dato se atribuye a una de estas cuatro fuentes. Ante una discrepancia **manda la situada más arriba**; lo que una fuente superior no trata se toma de la siguiente, y la discrepancia se anota en *cursiva*.

| Nivel | Fuente | Por qué ocupa ese nivel |
|---|---|---|
| **1** | **SEN 2023**: *Manual de Urgencias Neurológicas* de la Sociedad Española de Neurología, cap. 12 | Referencia española más reciente para el tratamiento; adapta la ESCMID 2016 a nuestro medio |
| **2** | **ESCMID 2016** (meningitis bacteriana aguda) y **ESCMID 2024** (absceso cerebral) | Guías europeas con revisión sistemática; árbitro de lo que la SEN no detalla. La de 2024 es la guía principal del absceso cerebral |
| **3** | **NICE NG240 (2024)**: meningitis bacteriana y enfermedad meningocócica | Guía con metodología GRADE; reconocimiento, tiempos, pruebas, alta y seguimiento |
| **4** | **SEMES 2012**: *Manejo de Infecciones en Urgencias*, caps. 18-23 | Estructura de actuación en urgencias y capítulos que no cubren las otras tres |

Los estudios primarios solo aparecen cuando los recoge alguna de las cuatro guías, y se citan a través de ella. La evaluación completa de las fuentes, las discrepancias ya resueltas, los puntos de la SEMES 2012 que han quedado superados y los documentos revisados pero descartados (entre ellos, las guías IDSA) están en [`apuntes/FUENTES.md`](apuntes/FUENTES.md).

## Contenido

| # | Capítulo | Estado |
|---|---|---|
| 1 | [Meningitis bacteriana aguda del adulto](apuntes/01_Meningitis_bacteriana.md) | ✅ Redactado |
| 2 | [Meningitis linfocitaria, aséptica y subaguda](apuntes/02_Meningitis_linfocitaria_subaguda.md) | ✅ Redactado |
| 3 | [Encefalitis aguda](apuntes/03_Encefalitis.md) | ✅ Redactado |
| 4 | [Absceso cerebral](apuntes/04_Absceso_cerebral.md) | ✅ Redactado |
| 5 | [Infecciones parameníngeas y medulares](apuntes/05_Infecciones_parameningeas_medulares.md) | ✅ Redactado |
| 6 | [Infecciones de derivaciones de LCR y meningitis posneuroquirúrgica](apuntes/06_Derivaciones_LCR_posneuroquirurgica.md) | ✅ Redactado |

El contenido clave de cada capítulo y qué fuentes lo cubren se detallan en el índice: [`apuntes/00_INDICE.md`](apuntes/00_INDICE.md).

## Estructura del repositorio

```
.
├── README.md
├── apuntes/
│   ├── 00_INDICE.md                    # Índice de capítulos, contenido y fuentes de cada uno
│   ├── FUENTES.md                      # Pirámide de fuentes, cobertura y discrepancias
│   ├── 01_Meningitis_bacteriana.md
│   ├── 02_Meningitis_linfocitaria_subaguda.md
│   ├── 03_Encefalitis.md
│   ├── 04_Absceso_cerebral.md
│   ├── 05_Infecciones_parameningeas_medulares.md
│   └── 06_Derivaciones_LCR_posneuroquirurgica.md
└── plantillas/
    ├── GUIA_DE_ESTILO.md               # Estructura fija y convenciones de formato
    └── EJEMPLO_NAC_IDSA_SEMES.md       # Modelo original (NAC) del que se extrajo el estilo
```

## Cómo leer los apuntes

Cada capítulo sigue la estructura fija de la [guía de estilo](plantillas/GUIA_DE_ESTILO.md): definición y fisiopatología, epidemiología, etiología, gravedad y lugar de tratamiento, tratamiento, pruebas, notas para el contexto español y europeo y referencias.

- **MAYÚSCULAS en negrita**: lo imprescindible en urgencias.
- **Negrita**: conceptos y fármacos clave.
- *Cursiva*: matiz, dato de evidencia o discrepancia entre guías; prescindible en una lectura rápida.
- **Atribución entre paréntesis** tras cada dato: la NICE con el número de recomendación (p. ej., NICE 1.4.7) y la ESCMID con su grado (A-D en la de 2016; fuerza y certeza GRADE en la de 2024).
- **Pautas de tratamiento**: `---> PRIMERA ELECCIÓN:` y `---> ALTERNATIVA:`, siempre con fármaco, dosis, vía e intervalo.
- Cuando la evidencia es débil, contradictoria o el dato no está verificado, se dice explícitamente.

## Cómo añadir un capítulo

1. Crear `apuntes/NN_Nombre_del_capitulo.md` siguiendo la [guía de estilo](plantillas/GUIA_DE_ESTILO.md): título con `#`, secciones numeradas con `##` y subapartados con `###`; tablas Markdown y nada de HTML.
2. Usar solo las cuatro fuentes de la pirámide y atribuir cada dato. Si dos fuentes discrepan, aplicar la pirámide y dejar la discrepancia anotada en *cursiva*.
3. Cerrar con las **referencias**: cita completa en negrita-cursiva (PMID y DOI cuando existan) y, debajo, qué nivel ocupa cada fuente y qué aporta al capítulo.
4. Actualizar el estado en [`apuntes/00_INDICE.md`](apuntes/00_INDICE.md) y en la tabla de contenido de este README, y registrar en [`apuntes/FUENTES.md`](apuntes/FUENTES.md) las discrepancias nuevas que se hayan resuelto.

## Limitaciones conocidas

- La **SEMES 2012** está desactualizada en varios puntos; los que ya se han detectado están listados en `FUENTES.md`.
- La **ESCMID 2016** no usa GRADE (niveles de evidencia 1-3 y grados A-D).
- Los **datos españoles de resistencia del neumococo** que recogen las cuatro fuentes son del ECDC de 2011; no hay datos más recientes dentro de la pirámide.
- En el **capítulo 4**, las dosis de la ESCMID 2024 están en su material suplementario (tabla S10), que no se ha revisado; se usan las de la SEMES 2012.
- Los capítulos 5 y 6 se apoyan casi solo en la SEMES 2012, porque las fuentes de nivel superior no los tratan (salvo la pauta empírica tras neurocirugía de la SEN). La NICE excluye expresamente de su alcance a los portadores de derivaciones y a los pacientes con neurocirugía previa.
