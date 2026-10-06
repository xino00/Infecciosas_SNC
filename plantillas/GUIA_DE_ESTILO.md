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
7. **NOTAS PARA EL CONTEXTO ESPAÑOL Y EUROPEO** — viñetas: discrepancias entre las fuentes autorizadas, resistencias locales (si es pertinente), disponibilidad de fármacos. *En los capítulos revisados (por ahora, el 1) no forman una sección propia: cada nota va en el apartado al que se refiere, sin repetirla.*
8. **REFERENCIAS** — fuentes autorizadas para el ámbito: cita en formato **Vancouver** + *nivel en la jerarquía y qué aporta cada una*.

El capítulo 8, dedicado a complicaciones de PL, adapta esta estructura a seguridad, complicaciones, verificación y referencias. Su desarrollo completo permanece en un Markdown independiente; el capítulo 1 y su Word conservan la seguridad de la PL y una remisión.

## Convenciones

- **Jerarquía general**: **SEN 2025 (Manual del Residente) → ESCMID (2016 meningitis; 2024 absceso cerebral) → NICE NG240 2024 → SEMES 2012**. Ante una discrepancia manda la de más arriba; lo que no concreta puede completarse con la siguiente. El silencio de una fuente no permite atribuirle una afirmación ni una negación. La discrepancia se anota en *cursiva*.
  - En el **absceso cerebral** manda la **ESCMID 2024**: **ESCMID 2024 → SEN 2025 → SEMES 2012**.
  - **Revisión de Mensa 2026**: solo apartados revisados de meningitis del adulto, capítulo 8 y HTIC criptocócica del capítulo 7: **SEN 2025 → Mensa 2026 → ESCMID 2016 → NICE NG240 → SEMES 2012**. No extrapolar los extractos a otros capítulos ni las dosis pediátricas al adulto. Una pauta concreta dentro de un intervalo más amplio puede ser compatible.
  - **Excepción de manitol (capítulo 1)**: por decisión del autor (06/10/2026), en la HTIC de la MBA se sigue a la **ESCMID 2016** (no recomienda el uso adyuvante rutinario del manitol, grado D) y se explicitan las posturas de NICE, SEN 2025 y Mensa 2026.
  - **Excepción de crisis**: texto principal exclusivamente respaldado por SEN. Si SEN no se pronuncia, decirlo. La propuesta de Mensa de considerar profilaxis neumocócica y sus dosis, si se incluyen, permanecen dentro de una aclaración en *cursiva*, con atribución inequívoca; no se transforma en profilaxis universal ni se atribuye a SEN el criterio de ESCMID.
- **Cada dato se atribuye a su fuente** entre paréntesis: la NICE con el número de recomendación (p. ej., NICE 1.4.7) y la ESCMID con su año y su grado (A-D en la de 2016; fuerza y certeza GRADE en la de 2024). **La SEN 2025 es la fuente de referencia y, en los capítulos revisados (por ahora, el 1), solo se cita (SEN 2025) cuando otra fuente dice algo distinto.** Los capítulos 2-8 conservan la atribución sistemática a la SEN hasta su revisión. Mensa se cita como **Mensa 2026**. Los estudios primarios solo aparecen cuando los recoge alguna de las fuentes, y se citan a través de ella (p. ej., "la ESCMID resume la revisión Cochrane…").
- **Ecología local (2024)**: porcentajes de resistencia de **informes internos de la FJD** de 2024, **fuera de la pirámide** y sin referencia bibliográfica; el cuadro de fuentes de cada capítulo indica su procedencia. Solo se añaden donde las fuentes piden adaptar la pauta a la resistencia local, junto al punto de decisión: «resistencia en la FJD a ampicilina en *H. influenzae*: ≈9 %, informes internos de 2024». Los capítulos 2-8 los llevan en *cursiva* con la etiqueta **(ecología local 2024)** hasta su revisión. No cambian pautas ni resuelven discrepancias; lo que sea interpretación y no dato se señala como tal. Reglas en `apuntes/FUENTES.md` (§8).
- Negrita para conceptos y fármacos clave; MAYÚSCULAS para lo que hay que "ver de un vistazo" en urgencias.
- *Cursiva* = matiz, dato de evidencia o comentario de fondo (prescindible en lectura rápida).
- Dosis siempre con vía e intervalo (y ajuste en perfusión extendida/función renal si procede).
- Cuando la evidencia sea débil, contradictoria o el dato no esté verificado, **se indica explícitamente**.
- Cifras y unidades: «≈» para las aproximaciones (no «~»), recuentos celulares en **/µL** (no /mm³), comillas latinas «» y nombres completos cuando la sigla es ambigua (proteína C reactiva frente a PCR).
- **Referencias**: formato **Vancouver** (con el DOI cuando exista), numeradas, y debajo el nivel en la jerarquía y lo que aporta cada fuente. Mensa: *Mensa J, Soriano A. Guía de terapéutica antimicrobiana 2026. 36.ª ed. Barcelona: Antares; 2026*; no inventar páginas, grados ni acceso a la guía completa (solo se dispone de dos extractos).
- **Fidelidad y validación**: distinguir transcripción, interpretación y validación clínica. Las posibles erratas se conservan atribuidas y pendientes, nunca como pautas operativas: no corregir silenciosamente Hb, el barbitúrico ni las unidades de PIC. Las notas sobre cómo se redactó el capítulo y los datos pendientes de validación se registran en `apuntes/FUENTES.md`, no en el capítulo. Una comprobación CIMA/AEMPS, si se realiza, se identifica como farmacológica oficial y no como recomendación de las guías. Verificar una a una dosis y cifras contra el original disponible o el extracto, y repetir la comprobación de forma adversarial antes de entregar.

## Formato Markdown

- Un archivo `.md` por capítulo en `apuntes/` (`01_Meningitis_bacteriana.md`, …).
- Título del capítulo con `#`; secciones numeradas con `##` (`## 1. DEFINICIÓN Y FISIOPATOLOGÍA`), subapartados con `###` (`### 4.1. …`) y `####` para el tercer nivel.
- Numeración real y correlativa (el ejemplo de NAC, exportado desde Word, repite "1." en todas las secciones y tiene restos de `****`; aquí no).
- Listas con `-` o `1.`; pautas de tratamiento como `- **---> PRIMERA ELECCIÓN:** …`.
- Tablas Markdown para comparativas (perfil de LCR, etiología por edad, dosis).
- Notas clave en bloque de cita `>`; nada de HTML.
