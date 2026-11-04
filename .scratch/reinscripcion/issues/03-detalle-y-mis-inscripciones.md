# 03: Detalle y "Mis inscripciones" muestran la reinscripción

**What to build:** Después de cancelar, el detalle vuelve a ofrecer el formulario cuando la actividad está habilitada, no empezó y tiene cupo, y muestra la fecha de la última cancelación. "Mis inscripciones" lista todas las filas del alumno, incluidas cada cancelación y la nueva vigente, de más reciente a más antigua.

**Blocked by:** 02 (servicio de reinscripción)

**Spec:** ../spec.md

**Status:** ready-for-agent

- [ ] El detalle sin vigente ofrece el formulario si las reglas lo permiten.
- [ ] El detalle muestra la fecha de la última cancelación cuando existe.
- [ ] "Mis inscripciones" lista todas las inscripciones, incluidas las cancelaciones, sin ocultar historial.
- [ ] Reinscribirse desde el detalle confirma la nueva inscripción y actualiza el cupo.
- [ ] Pruebas HTTP cubren el formulario, la fecha de última cancelación y el historial en "Mis inscripciones".
