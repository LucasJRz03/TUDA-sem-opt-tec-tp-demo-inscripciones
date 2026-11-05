# 02: La reinscripción crea una inscripción nueva

**What to build:** Un alumno con solo inscripciones canceladas puede volver a inscribirse y recibe una fila nueva, conservando las canceladas. `register()` deja de devolver `previously_cancelled`: si no hay una fila vigente, evalúa habilitación, inicio y cupo como en una primera inscripción y crea la fila. `already_registered` queda reservado a una vigente.

**Blocked by:** 01 (constraint parcial)

**Spec:** ../spec.md

**Status:** done

- [x] Inscribirse sobre solo canceladas crea una fila nueva y devuelve `registered`.
- [x] Se elimina el resultado `previously_cancelled` y su mensaje.
- [x] `already_registered` solo se devuelve cuando ya existe una inscripción vigente.
- [x] La reinscripción respeta habilitación, inicio y cupo con los mismos resultados que una primera inscripción.
- [x] Varios ciclos de cancelar y reinscribir conservan todas las filas canceladas.
- [x] Las pruebas de bloqueo de reinscripción se reemplazan por pruebas de reinscripción.

## Comments

Implementado en `6dd5ac0`. `register()` busca solo la inscripción vigente: si existe devuelve `already_registered`; si solo hay canceladas evalúa habilitación, inicio y cupo y crea una fila nueva. Se elimina `previously_cancelled` y su mensaje. Las pruebas de servicio cubren fila nueva, cupo, reglas, `already_registered` y ciclos repetidos; las HTTP de bloqueo se reemplazaron por reinscripción real y respeto de reglas. Suite completa: 71 pruebas OK; `makemigrations --check` sin cambios. Code review sin violaciones duras.
