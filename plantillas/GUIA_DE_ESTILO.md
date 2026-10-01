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
   - Terapia secuencial / desescalada, **duración**, **tratamiento adyuvante** (con datos de metaanálisis: n, RR, IC 95 %, certeza).
6. **ESTUDIOS MICROBIOLÓGICOS / PRUEBAS** — escalonado por gravedad (lo que se pide y lo que NO, y por qué).
7. **NOTAS PARA EL CONTEXTO ESPAÑOL Y EUROPEO** — viñetas: discrepancias entre guías (SEMES vs. IDSA/ESCMID), resistencias locales, disponibilidad de fármacos.
8. **REFERENCIAS** — cita completa en negrita-cursiva + *para qué se ha usado cada una*.

## Convenciones

- **Fuente principal de tratamiento**: guía española (SEMES 2026 u otra que se aporte). Las guías internacionales (IDSA, ESCMID…) se usan como contraste y se señala explícitamente cuando discrepan.
- Negrita para conceptos y fármacos clave; MAYÚSCULAS para lo que hay que "ver de un vistazo" en urgencias.
- *Cursiva* = matiz, dato de evidencia o comentario de fondo (prescindible en lectura rápida).
- Dosis siempre con vía e intervalo (y ajuste en perfusión extendida/función renal si procede).
- Cuando la evidencia sea débil, contradictoria o el dato no esté verificado, **se indica explícitamente**.
- Referencias verificadas (PMID/DOI); no se dejan citas del tipo "probablemente corresponde a…".

## Formato Markdown

- Un archivo `.md` por capítulo en `apuntes/` (`01_Meningitis_bacteriana.md`, …).
- Título del capítulo con `#`; secciones numeradas con `##` (`## 1. DEFINICIÓN Y FISIOPATOLOGÍA`), subapartados con `###` (`### 4.1. …`) y `####` para el tercer nivel.
- Numeración real y correlativa (el ejemplo de NAC, exportado desde Word, repite "1." en todas las secciones y tiene restos de `****`; aquí no).
- Listas con `-` o `1.`; pautas de tratamiento como `- **---> PRIMERA ELECCIÓN:** …`.
- Tablas Markdown para comparativas (perfil de LCR, etiología por edad, dosis).
- Notas clave en bloque de cita `>`; nada de HTML.
