# GUÍA DE ESTILO DE LOS APUNTES

> Los apuntes están pensados para el **médico de urgencias a pie de cama**. Cada capítulo abre con una **FICHA DE ACTUACIÓN EN URGENCIAS** y sigue la secuencia asistencial: sospecha → actuación inicial → pruebas → tratamiento empírico → soporte → destino → salud pública. Lo que no se decide en urgencias (tratamiento dirigido, duración, seguimiento, fundamentos y evidencia de fondo) va al final.
>
> El estilo (MAYÚSCULAS para lo imprescindible, cursiva para los matices, pautas con `--->`) viene del modelo de NAC (`EJEMPLO_NAC_IDSA_SEMES.md`). Ese archivo es un modelo de **estilo**, no de estructura.

## Estructura fija de cada capítulo

```
# TÍTULO DEL CAPÍTULO
> Cabecera de fuentes
## FICHA DE ACTUACIÓN EN URGENCIAS
## 1. SOSPECHA CLÍNICA Y DIAGNÓSTICO DIFERENCIAL
## 2. ACTUACIÓN INICIAL: TIEMPOS Y SECUENCIA
## 3. PRUEBAS COMPLEMENTARIAS
## 4. TRATAMIENTO EMPÍRICO EN URGENCIAS
## 5. SOPORTE Y COMPLICACIONES AGUDAS
## 6. DESTINO E INTERCONSULTAS
## 7. SALUD PÚBLICA
## 8. DESPUÉS DE URGENCIAS
## 9. FUNDAMENTOS
## 10. CONTEXTO ESPAÑOL Y EUROPEO, DISCREPANCIAS Y PENDIENTES
## REFERENCIAS
```

Las secciones `##` 1-10 existen en **todos** los capítulos, con el mismo número y título, para que «capítulo N, §x» signifique lo mismo en todos. Dentro de ellas solo son obligatorios los `###` marcados con ✱; los demás se crean si hay contenido. Si una sección no tiene alguno, lo dice en una sola línea al final: «No tratados por las fuentes: … (→ §10.3)».

| Sección | Pregunta que responde | Subapartados |
|---|---|---|
| **Cabecera** (bloque `>`, ≤6 líneas) | ¿De qué fuentes sale? | Pirámide del capítulo y ámbito exacto de cada excepción; equivalencias de cita (p. ej., «ESCMID = ESCMID 2016 en este capítulo»); aviso de evidencia; «Ver `FUENTES.md`». Sin datos clínicos |
| **FICHA DE ACTUACIÓN EN URGENCIAS** | ¿Qué hago ahora? | Ver «Ficha de actuación en urgencias» |
| **1. Sospecha clínica y diagnóstico diferencial** | ¿Qué puede ser y qué no debo descartar? | 1.1 Cuándo sospecharla (en los capítulos multientidad, tabla de TRIAJE) · 1.2 Lo que no la descarta y presentaciones atípicas · 1.3 Pistas de etiología y anamnesis dirigida · 1.4 Diagnóstico diferencial (tabla Entidad · Qué la separa · Dónde se trata) |
| **2. Actuación inicial** | ¿Qué hago ya y en qué orden? | 2.1 Primeros minutos ✱ (objetivo de tiempo en `>` y lista numerada) · 2.2 Exploración dirigida · 2.3 Imagen y punción ✱ (algoritmo con ramas SÍ/NO) · 2.4 Contraindicaciones y lo que no se hace |
| **3. Pruebas complementarias** | ¿Qué pido, cómo y cómo lo leo? | Nota «PCR» (proteína C reactiva frente a reacción en cadena de la polimerasa) si el capítulo usa las dos · 3.1 Sangre y otras muestras («ANTES DEL ANTIBIÓTICO») · 3.2 Muestra diana: qué pedir y cómo · 3.3 Interpretación · 3.4 Rendimiento y límites (qué no se pide y por qué) · 3.5 Imagen |
| **4. Tratamiento empírico en urgencias** | ¿Qué antimicrobiano y qué adyuvante, ahora? | 4.1 Gérmenes que hay que cubrir según el contexto y los factores de riesgo (la etiología que decide la pauta) · 4.2 Principios y momento del antimicrobiano · 4.3 Pautas por escenario ✱ (un `####` con nombre estable por escenario) · 4.4 Adyuvantes y coberturas añadidas · 4.5 Situaciones especiales: alergia, embarazo, función renal (solo reúne y remite; lo que falte, a §10.3) · 4.6 Dosis de referencia (opcional; si existe, siempre la última) |
| **5. Soporte y complicaciones agudas** | ¿Cómo lo sostengo y qué complicación trato ya? | Soporte vital, sepsis y shock · HTIC · crisis · líquidos, sintomático y lo que NO se usa · complicaciones agudas (tabla con remisión al capítulo que las trata) |
| **6. Destino e interconsultas** | ¿Adónde va y a quién llamo? | 6.1 Criterios de destino ✱ (tabla con filas UCI, Ingreso, Observación y Alta, en ese orden; si un criterio solo procede de la SEMES 2012, se indica) · 6.2 Datos de gravedad y pronóstico (no son criterios) · 6.3 Interconsultas y avisos · 6.4 Alta |
| **7. Salud pública** | ¿Quién más está en riesgo? | Aislamiento · declaración · contactos y profilaxis. Si no aplica, una sola línea |
| **8. Después de urgencias** | ¿Qué pasa en planta? | Tratamiento dirigido y duración · retirada de adyuvantes y dispositivos · evolución durante el ingreso · antes del alta, prevención y seguimiento |
| **9. Fundamentos** | ¿Por qué? | Definición y clasificación · fisiopatología (condensada) · epidemiología y pronóstico (Europa y España primero) · etiología por frecuencia · evidencia de fondo que resumen las guías |
| **10. Contexto, discrepancias y pendientes** | ¿En qué discrepan las fuentes y qué falta? | 10.1 Contexto español y europeo · 10.2 Discrepancias entre fuentes ✱ (sincronizadas con `FUENTES.md` §3-§4; aquí van las tablas que comparan fuentes) · 10.3 Datos dudosos y pendientes ✱ («Pendiente: … No se rellena») |
| **REFERENCIAS** (sin número) | | Solo las cuatro fuentes: cita completa en negrita-cursiva (PMID y DOI) y, debajo, *nivel en la pirámide y qué aporta* |

**Capítulos multientidad (2, 5 y 7).** La entidad es el tercer nivel (`####`) o una columna «Entidad» en las tablas. La ficha se organiza por escenario o síndrome de presentación, nunca por germen.

**Capítulos de manejo sobre todo especializado (7).** Si una entidad no tiene decisión en urgencias, su sospecha va a §1 como una fila del TRIAJE y su manejo a §8-§9, en tablas compactas, sin perder filas ni atribuciones.

### Equivalencias con la estructura anterior

| Antes | Ahora |
|---|---|
| 1. Definición y fisiopatología | §9.1-§9.2; diagnóstico → §3.3; diagnóstico diferencial → §1.4 |
| 2. Epidemiología | §9.3; lo que apoya la decisión de destino → §6.2 |
| 3. Etiología | §4.1 si decide la pauta; §9.4 si es frecuencia; pistas clínicas → §1.3 |
| 4. Gravedad y lugar de tratamiento | §6; «factores de riesgo para ampliar cobertura» → §4.1 |
| 5. Tratamiento | Empírico y adyuvante → §4; dirigido y duración → §8 |
| 6. Pruebas | §3 |
| 7. Notas para el contexto español y europeo | §10 |
| 8. Referencias | REFERENCIAS |

## Ficha de actuación en urgencias

**La ficha resume, no origina.** Toda cifra, dosis, fármaco y atribución de la ficha está en el cuerpo (§1-§10) con la misma atribución. Se escribe la última, a partir del cuerpo, y se revisa cada vez que cambia el cuerpo. Encabezado exacto: `## FICHA DE ACTUACIÓN EN URGENCIAS`, sin número.

**Extensión:** 1-2 pantallas; como máximo unas **45 líneas no vacías y 900 palabras**.

**Bloques, en este orden**, y cada uno con la remisión a su sección (`**PEDIR** (→ §3)`):

| Bloque | Forma |
|---|---|
| Mensaje clave | Bloque `>` en MAYÚSCULAS y negrita, con su atribución (1-2 frases) |
| **SOSPECHAR SI** (→ §1) | ≤4 viñetas. En los capítulos multientidad, **TRIAJE**: tabla Presentación · Pensar en · Prueba clave · Acción (§), ≤8 filas |
| **PRIMEROS MINUTOS** (→ §2) | Lista numerada; cada decisión como sublista **SÍ** / **NO** de un nivel. Si las fuentes no dan objetivo de tiempo: «Sin objetivo de tiempo en las fuentes» |
| **PAUTA EMPÍRICA** (→ §4.3) | Tabla Escenario · PRIMERA ELECCIÓN · ALTERNATIVA (motivo); los adyuvantes, como filas que empiezan por **+** |
| **DESTINO** (→ §6) | Tabla con filas UCI, Ingreso, Observación y Alta |
| **PEDIR** (→ §3) y **NO HACER** | Viñetas cortas |
| **AVISAR Y PROFILAXIS** (→ §6.3, §7) | Servicio + motivo; profilaxis con dosis completas |
| **ERRORES FRECUENTES** | ≤5, «error: por qué (fuente)» |
| Pendientes | Una línea en cursiva: «*Pendiente en las fuentes (§10.3): …*» |

**Redacción de la ficha.** Fármacos en MAYÚSCULAS y negrita con dosis, vía e intervalo (**CEFTRIAXONA 2 g IV cada 12 h**). La atribución va al final de la viñeta o de la celda; si una viñeta reúne varios datos, lleva la unión de sus atribuciones sin inventar rangos ni grados. Sin cursiva, salvo la discrepancia que cambia la acción y la línea de pendientes.

## Reubicación y condensación

- **Un dato, un sitio**: en el cuerpo, cada dato con su atribución aparece una sola vez; en los demás sitios, una remisión «→ §x.y». La ficha es la única excepción.
- **Condensar es quitar prosa**, nunca cifras, rangos, unidades, grados ni atribuciones. Las cifras no se redondean y las unidades no se convierten.
- **Al partir un párrafo**, cada fragmento lleva su atribución. Si no se puede saber a qué fragmento se refería, se marca «[atribución por verificar]» y se lista en §10.3; nunca se adivina.
- **Cursiva**: lo que cambia una decisión en urgencias sale de la cursiva con su atribución; la evidencia, las cifras de rendimiento y las discrepancias se quedan en cursiva.
- **Justificaciones** («*Por qué:*») junto a la acción que justifican, en cursiva y con su fuente.
- **Discrepancias**: en la sección de acción va solo la regla que gana por la pirámide, más una línea en cursiva con la discrepancia esencial y «→ §10.2».
- **Huecos**: no se rellenan con farmacología general ni con datos de otro capítulo (salvo una remisión a un dato idéntico y atribuido): «No consta en las fuentes (§10.3)».
- **Correcciones**: solo las que se deducen del propio repositorio. Las demás se marcan «[por verificar]» y se listan en §10.3.

## Convenciones

- **Fuentes: solo cuatro**, en pirámide: **SEN (2023 urgencias; 2025 residente) → ESCMID (2016 meningitis; 2024 absceso cerebral) → NICE NG240 2024 → SEMES 2012**. Ante una discrepancia manda la de más arriba; lo que no trata se toma de la siguiente. La discrepancia se anota en *cursiva*.
  - Si las dos SEN discrepan, manda la **SEN 2025**.
  - En el **absceso cerebral** manda la **ESCMID 2024**: **ESCMID 2024 → SEN 2025 → SEMES 2012**.
- **Cada dato se atribuye a su fuente** entre paréntesis: la SEN con su año (SEN 2023 o SEN 2025), la NICE con el número de recomendación (p. ej., NICE 1.4.7) y la ESCMID con su año y su grado (A-D en la de 2016; fuerza y certeza GRADE en la de 2024). Si la cabecera del capítulo lo declara, la ESCMID puede ir sin año. Los estudios primarios solo aparecen cuando los recoge alguna de las fuentes, y se citan a través de ella (p. ej., "la ESCMID resume la revisión Cochrane…").
- **Marcadores** para lo que no consta: «[atribución por verificar]», «[año por verificar]», «[sin vía en la fuente]» y «No consta en las fuentes (§10.3)». Todos se listan en §10.3.
- Negrita para conceptos y fármacos clave; MAYÚSCULAS para lo que hay que "ver de un vistazo" en urgencias.
- *Cursiva* = matiz, dato de evidencia, discrepancia o comentario de fondo (prescindible en lectura rápida). No se pone en cursiva lo que cambia una decisión en urgencias.
- Dosis siempre con vía e intervalo (y ajuste en perfusión extendida o a la función renal si la fuente lo da). **Si la fuente no da la vía, la dosis o el intervalo, se dice; no se completa.**
- Cuando la evidencia sea débil, contradictoria o el dato no esté verificado, **se indica explícitamente**.
- **Referencias**: solo las cuatro fuentes, con la cita completa en negrita-cursiva (PMID y DOI cuando existan) y debajo una explicación en *cursiva* de qué nivel ocupa en la pirámide y qué aporta al capítulo. No se dejan citas del tipo "probablemente corresponde a…".

## Formato Markdown

- Un archivo `.md` por capítulo en `apuntes/` (`01_Meningitis_bacteriana.md`, …).
- Título del capítulo con `#`; secciones con `##` y la numeración fija de la plantilla (`## 4. TRATAMIENTO EMPÍRICO EN URGENCIAS`); subapartados con `###` (`### 4.3. Pautas por escenario`); escenarios y entidades con `####`, sin número y con un nombre estable que pueda citarse.
- Numeración real y correlativa (el ejemplo de NAC, exportado desde Word, repite "1." en todas las secciones y tiene restos de `****`; aquí no).
- Listas con `-` o `1.`. Etiquetas de pauta, solo estas cuatro:
  - `- **---> PRIMERA ELECCIÓN:** …`
  - `- **---> ALTERNATIVA (motivo):** …`
  - `- **---> ADYUVANTE:** …`
  - `- **---> PROFILAXIS:** …`
- Algoritmos como `> **ACTUACIÓN (fuente)**:` seguido de una lista numerada con ramas **SÍ** / **NO** de un nivel, o como tablas de decisión.
- Tablas Markdown para comparativas (perfil de LCR, etiología, dosis, destino).
- Remisiones siempre explícitas: «→ §4.3», «capítulo 6, §4.3». Nunca «arriba», «abajo» ni «tabla de arriba».
- Notas clave en bloque de cita `>`; **nada de HTML ni de diagramas Mermaid**.
