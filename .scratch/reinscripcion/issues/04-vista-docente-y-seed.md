# 04: Vista docente y seed respetan el historial

**What to build:** La vista docente lista todas las filas de cada actividad, vigentes primero, de modo que cada cancelación y cada reinscripción queden auditables. El seed sigue comprobando existencia sin filtrar estado: cualquier fila del alumno en la actividad, vigente o cancelada, impide recrearla.

**Blocked by:** 02 (servicio de reinscripción)

**Spec:** ../spec.md

**Status:** ready-for-agent

- [ ] La vista docente muestra todas las filas, incluidas las cancelaciones y las reinscripciones.
- [ ] El orden mantiene vigentes primero y luego por fecha de creación.
- [ ] El seed no recrea una inscripción si existe cualquier fila del alumno en la actividad, aunque esté cancelada.
- [ ] Pruebas de administración y seed cubren el historial y la preservación de la cancelación.
