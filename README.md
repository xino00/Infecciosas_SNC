# Infecciosas_SNC

Apuntes de **infecciones del sistema nervioso central (SNC) para urgencias**, centrados en el paciente adulto. Están pensados para consultarse a pie de cama: cada capítulo sigue la misma estructura y destaca en MAYÚSCULAS y negrita lo que hay que ver de un vistazo, y deja en *cursiva* los matices y los datos de evidencia.

> **Aviso**: son apuntes de estudio, no un protocolo asistencial. No sustituyen al juicio clínico ni a los protocolos y la epidemiología de cada centro. Comprueba siempre las dosis (y su ajuste a la función renal) antes de prescribir.

## Fuentes y jerarquía

Todo dato procede de una fuente autorizada. Ante una discrepancia **manda la situada más arriba**; lo que una fuente superior no concreta puede completarse con la siguiente, sin atribuir a la primera lo que no dice. La discrepancia se anota en *cursiva*. **La SEN 2025 es la fuente de referencia: en los capítulos revisados (por ahora, el 1) solo se cita cuando otra fuente dice algo distinto**; los capítulos 2-8 conservan la atribución de cada dato hasta su revisión. Esta es la jerarquía general:

| Nivel | Fuente | Por qué ocupa ese nivel |
|---|---|---|
| **1** | **SEN 2025**: *Manual del Residente de Neurología* (caps. 40-44) de la Sociedad Española de Neurología | Referencia española principal: meningitis agudas y crónicas, absceso, empiemas e infecciones víricas, fúngicas y parasitarias |
| **2** | **ESCMID 2016** (meningitis bacteriana aguda) y **ESCMID 2024** (absceso cerebral) | Guías europeas con revisión sistemática; árbitro de lo que la SEN no detalla. La de 2024 es la guía principal del absceso cerebral y, **solo en ese capítulo, manda también sobre la SEN 2025**, que se redactó antes y no la incorpora |
| **3** | **NICE NG240 (2024)**: meningitis bacteriana y enfermedad meningocócica | Guía con metodología GRADE; reconocimiento, tiempos, pruebas, alta y seguimiento |
| **4** | **SEMES 2012**: *Manejo de Infecciones en Urgencias*, caps. 18-23 | Estructura de actuación en urgencias y lo que no cubren las otras tres |

**Revisión con Mensa (05/10/2026):** en los apartados revisados de meningitis bacteriana, las complicaciones de PL y la HTIC criptocócica se aplica **SEN 2025 → Mensa 2026 → ESCMID 2016 → NICE NG240 → SEMES 2012**. De **Mensa 2026** solo se dispone de dos fragmentos; no se ha leído la guía completa. En **crisis epilépticas**, el texto principal se limita a SEN y la propuesta de Mensa de considerar profilaxis neumocócica queda en cursiva. En el **manitol para la HTIC** se sigue a la ESCMID 2016 por decisión del autor (06/10/2026), y el capítulo 1 explica la postura de cada fuente. El alcance y los datos pendientes constan en [FUENTES, §9](apuntes/FUENTES.md#9-revisión-con-los-extractos-de-mensa-2026). El resto de los capítulos conserva su jerarquía, incluida la prioridad de ESCMID 2024 en absceso cerebral.

**Ecología local (fuera de la pirámide).** Donde las fuentes piden adaptar la pauta a la resistencia local, los capítulos añaden porcentajes de resistencia de 2024 procedentes de **informes internos de la FJD**. En el capítulo 1 se citan junto al punto de decisión como «resistencia en la FJD (…; informes internos de 2024)»; los capítulos 2-8 los llevan en *cursiva* con la etiqueta **(ecología local 2024)** hasta su revisión. No son recomendaciones ni cambian la pirámide: ayudan a ver qué deja sin cubrir cada pauta y a elegir entre las opciones que ya dan las fuentes. Reglas y limitaciones en [`apuntes/FUENTES.md`](apuntes/FUENTES.md) (§8).

Los estudios primarios solo aparecen cuando los recoge alguna de las fuentes autorizadas, y se citan a través de ella. La evaluación de las fuentes, los capítulos de SEN 2025 con sus autores, las discrepancias, las posibles erratas y los documentos descartados están en [`apuntes/FUENTES.md`](apuntes/FUENTES.md).

## Contenido

| # | Capítulo | Estado |
|---|---|---|
| 1 | [Meningitis bacteriana aguda del adulto](apuntes/01_Meningitis_bacteriana.md) | ✅ Redactado |
| 2 | [Meningitis linfocitaria, aséptica, subaguda y crónica](apuntes/02_Meningitis_linfocitaria_subaguda.md) | ✅ Redactado |
| 3 | [Encefalitis aguda](apuntes/03_Encefalitis.md) | ✅ Redactado |
| 4 | [Absceso cerebral](apuntes/04_Absceso_cerebral.md) | ✅ Redactado |
| 5 | [Infecciones parameníngeas y medulares](apuntes/05_Infecciones_parameningeas_medulares.md) | ✅ Redactado |
| 6 | [Infecciones de derivaciones de LCR y meningitis posneuroquirúrgica](apuntes/06_Derivaciones_LCR_posneuroquirurgica.md) | ✅ Redactado |
| 7 | [Infecciones fúngicas y parasitarias del SNC](apuntes/07_Infecciones_fungicas_parasitarias.md) | ✅ Redactado |
| 8 | [Complicaciones de la punción lumbar en el adulto](apuntes/08_Complicaciones_puncion_lumbar.md) | ✅ Redactado |

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
│   ├── 06_Derivaciones_LCR_posneuroquirurgica.md
│   ├── 07_Infecciones_fungicas_parasitarias.md
│   └── 08_Complicaciones_puncion_lumbar.md
└── plantillas/
    ├── GUIA_DE_ESTILO.md               # Estructura fija y convenciones de formato
    └── EJEMPLO_NAC_IDSA_SEMES.md       # Modelo original (NAC) del que se extrajo el estilo
```

## Cómo leer los apuntes

Cada capítulo sigue la estructura fija de la [guía de estilo](plantillas/GUIA_DE_ESTILO.md): definición y fisiopatología, epidemiología, etiología, gravedad y lugar de tratamiento, tratamiento, pruebas, notas para el contexto español y europeo y referencias. En los capítulos revisados (por ahora, el 1), esas notas se integran en el apartado al que se refieren y no forman una sección propia.

- **MAYÚSCULAS en negrita**: lo imprescindible en urgencias.
- **Negrita**: conceptos y fármacos clave.
- *Cursiva*: matiz, dato de evidencia o discrepancia entre guías; prescindible en una lectura rápida.
- **Atribución entre paréntesis** tras cada dato: la SEN y la ESCMID con su año (SEN 2025; ESCMID 2016 o 2024), la NICE con el número de recomendación (p. ej., NICE 1.4.7) y la ESCMID con su grado (A-D en la de 2016; fuerza y certeza GRADE en la de 2024). En el capítulo 1, la SEN 2025 solo se cita cuando otra fuente discrepa. Los porcentajes de resistencia local se citan como «resistencia en la FJD, informes internos de 2024» en el capítulo 1 y con la etiqueta **(ecología local 2024)** en los demás.
- **Pautas de tratamiento**: `---> PRIMERA ELECCIÓN:` y `---> ALTERNATIVA:`, siempre con fármaco, dosis, vía e intervalo.
- Cuando la evidencia es débil, contradictoria o el dato no está verificado, se dice explícitamente.

## Cómo añadir un capítulo

1. Crear `apuntes/NN_Nombre_del_capitulo.md` siguiendo la [guía de estilo](plantillas/GUIA_DE_ESTILO.md): título con `#`, secciones numeradas con `##` y subapartados con `###`; tablas Markdown y nada de HTML.
2. Usar las fuentes autorizadas para ese ámbito y atribuir cada dato. Mensa solo puede usarse en los apartados de la revisión descrita, sin extrapolar sus fragmentos a otros capítulos. Si dos fuentes discrepan, aplicar la jerarquía y dejar la discrepancia en *cursiva*. Si la resistencia local es pertinente, añadirla junto al punto de decisión como «resistencia en la FJD (…; informes internos de 2024)» (reglas en `FUENTES.md`, §8). Citar la SEN 2025 solo cuando otra fuente diga algo distinto.
3. Cerrar con las **referencias** en formato **Vancouver** (con el DOI cuando exista), seguidas del nivel en la jerarquía y de lo que aporta cada fuente. Mensa se cita en el texto como **Mensa 2026** y en las referencias como *Mensa J, Soriano A. Guía de terapéutica antimicrobiana 2026. 36.ª ed. Barcelona: Antares; 2026*, sin inventar páginas ni grados. Las notas sobre cómo se redactó el capítulo y los datos pendientes van en `FUENTES.md`, no en el capítulo.
4. Actualizar el estado en [`apuntes/00_INDICE.md`](apuntes/00_INDICE.md) y en la tabla de contenido de este README, y registrar en [`apuntes/FUENTES.md`](apuntes/FUENTES.md) las discrepancias nuevas que se hayan resuelto.

## Limitaciones conocidas

- **Mensa 2026**: acceso limitado a dos extractos. La unidad de Hb y la validez de ese objetivo, así como el fármaco, pauta y umbral/unidades del coma barbitúrico, siguen pendientes; no son pautas operativas validadas y no figuran en el capítulo 1 (constan en `FUENTES.md`, §9).
- La **SEMES 2012** está desactualizada en varios puntos; los que ya se han detectado están listados en `FUENTES.md`.
- La **SEN 2025** es un manual formativo, sin grados de recomendación, y su bibliografía se consultó en 2023: no incorpora la ESCMID 2024 ni la NICE 2024. Tiene algunas ambigüedades y posibles erratas (intervalos que faltan, una dosis baja de cloxacilina, la tuberculosis sin etambutol de entrada), señaladas en cada capítulo y listadas en `FUENTES.md`.
- La **ESCMID 2016** no usa GRADE (niveles de evidencia 1-3 y grados A-D).
- Los **datos españoles de resistencia del neumococo** que recogen las fuentes son del ECDC de 2011; no hay datos más recientes dentro de la pirámide. Fuera de ella, los informes internos de la FJD de 2024 dan un 12 % de neumococos no sensibles a la cefotaxima con el punto de corte de meningitis.
- La **ecología local de 2024** agrega todas las muestras del hospital (no hay datos del LCR ni por servicio) y no incluye meningococo, *Listeria*, grupo *S. anginosus*, *Nocardia* ni *Acinetobacter*.
- En el **capítulo 4**, las dosis de la ESCMID 2024 están en su material suplementario (tabla S10), que no se ha revisado; se usan las dosis específicas para absceso de la SEMES 2012. Las tablas de meningitis de la SEN 2025 no se consideran equivalentes para esta indicación.
- Los **capítulos 5 y 6** se apoyan en la SEN 2025 (empiemas, absceso epidural espinal, meningitis nosocomial) y en la SEMES 2012; la tromboflebitis séptica de senos y el manejo quirúrgico de las derivaciones siguen saliendo casi solo de la SEMES 2012. La NICE excluye expresamente de su alcance a las personas con inmunodeficiencia, a los portadores de derivaciones y a los pacientes con neurocirugía previa.
- El **capítulo 7** se basa casi por completo en la SEN 2025, que a su vez resume guías de la OMS y de la IDSA; buena parte de su contenido (malaria, tripanosomiasis, helmintos) es de manejo especializado más que de urgencias.
