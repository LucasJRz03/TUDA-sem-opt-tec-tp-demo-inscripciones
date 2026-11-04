# 05: Concurrencia y README

**What to build:** La constraint parcial queda cubierta bajo carreras reales: dos reinscripciones simultáneas del mismo alumno dejan una sola vigente, y una carrera cancelar↔reinscribir nunca produce dos vigentes. El README reemplaza la sección de "no hay reinscripción" por el recorrido de reinscripción, la conservación del historial y el conteo de pruebas actualizado.

**Blocked by:** 01, 02

**Spec:** ../spec.md

**Status:** ready-for-agent

- [ ] Prueba de concurrencia: dos reinscripciones simultáneas del mismo alumno dejan una sola fila vigente.
- [ ] Prueba de concurrencia: cancelar y reinscribir en paralelo nunca deja dos vigentes.
- [ ] El README documenta la reinscripción, el historial conservado y el nuevo conteo de pruebas.
- [ ] La suite completa queda verde y `./scripts/check.sh` pasa.
