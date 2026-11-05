# 04: Vista docente y seed respetan el historial

**What to build:** La vista docente lista todas las filas de cada actividad, vigentes primero, de modo que cada cancelación y cada reinscripción queden auditables. El seed sigue comprobando existencia sin filtrar estado: cualquier fila del alumno en la actividad, vigente o cancelada, impide recrearla.

**Blocked by:** 02 (servicio de reinscripción)

**Spec:** ../spec.md

**Status:** done

- [x] La vista docente muestra todas las filas, incluidas las cancelaciones y las reinscripciones.
- [x] El orden mantiene vigentes primero y luego por fecha de creación.
- [x] El seed no recrea una inscripción si existe cualquier fila del alumno en la actividad, aunque esté cancelada.
- [x] Pruebas de administración y seed cubren el historial y la preservación de la cancelación.

## Comments

La vista docente y el seed ya cumplían el comportamiento en el código existente: el detalle no filtra por estado y ordena vigentes primero, y el seed usa `exists()` sin filtrar `cancelled_at`. Se agregaron pruebas de regresión: historial de reinscripción en el detalle docente con orden vigente primero y luego por fecha de creación, historial de dos filas en la administración con la cancelación preservada, y seed repetido sobre cancelación y reinscripción sin recrear ni una fila más. Suite completa: 76 pruebas OK; `makemigrations --check` sin cambios. Code review: sin violaciones duras; se cerró el hueco de orden secundario señalado por Spec y se consolidó la prueba de seed para evitar duplicación.
