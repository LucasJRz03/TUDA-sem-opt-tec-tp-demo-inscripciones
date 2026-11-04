# 02: La reinscripción crea una inscripción nueva

**What to build:** Un alumno con solo inscripciones canceladas puede volver a inscribirse y recibe una fila nueva, conservando las canceladas. `register()` deja de devolver `previously_cancelled`: si no hay una fila vigente, evalúa habilitación, inicio y cupo como en una primera inscripción y crea la fila. `already_registered` queda reservado a una vigente.

**Blocked by:** 01 (constraint parcial)

**Spec:** ../spec.md

**Status:** ready-for-agent

- [ ] Inscribirse sobre solo canceladas crea una fila nueva y devuelve `registered`.
- [ ] Se elimina el resultado `previously_cancelled` y su mensaje.
- [ ] `already_registered` solo se devuelve cuando ya existe una inscripción vigente.
- [ ] La reinscripción respeta habilitación, inicio y cupo con los mismos resultados que una primera inscripción.
- [ ] Varios ciclos de cancelar y reinscribir conservan todas las filas canceladas.
- [ ] Las pruebas de bloqueo de reinscripción se reemplazan por pruebas de reinscripción.
