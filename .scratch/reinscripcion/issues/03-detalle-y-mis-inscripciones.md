# 03: Detalle y "Mis inscripciones" muestran la reinscripción

**What to build:** Después de cancelar, el detalle vuelve a ofrecer el formulario cuando la actividad está habilitada, no empezó y tiene cupo, y muestra la fecha de la última cancelación. "Mis inscripciones" lista todas las filas del alumno, incluidas cada cancelación y la nueva vigente, de más reciente a más antigua.

**Blocked by:** 02 (servicio de reinscripción)

**Spec:** ../spec.md

**Status:** done

- [x] El detalle sin vigente ofrece el formulario si las reglas lo permiten.
- [x] El detalle muestra la fecha de la última cancelación cuando existe.
- [x] "Mis inscripciones" lista todas las inscripciones, incluidas las cancelaciones, sin ocultar historial.
- [x] Reinscribirse desde el detalle confirma la nueva inscripción y actualiza el cupo.
- [x] Pruebas HTTP cubren el formulario, la fecha de última cancelación y el historial en "Mis inscripciones".

## Comments

Implementado en `8a77a08`. El detalle separa la inscripción vigente de la última cancelación: sin vigente vuelve a ofrecer el formulario si la actividad está habilitada, no empezó y tiene cupo, y muestra la fecha de la última cancelación. "Mis inscripciones" sigue listando todas las filas, vigente y canceladas, de más reciente a más antigua. Pruebas HTTP nuevas cubren el formulario, la fecha de última cancelación, la confirmación con cupo actualizado y el historial. Suite completa: 74 pruebas OK; `makemigrations --check` sin cambios. Code review: sin violaciones duras; se corrigió la prueba de historial para no leer `response.context`.
