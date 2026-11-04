# Permitir reinscripción después de cancelar

Status: ready-for-agent

## Problem Statement

Cancelar hoy es irreversible: la constraint única y el resultado `previously_cancelled` impiden volver a inscribirse en la misma actividad. El alumno que se arrepiente o resuelve un conflicto de horario no puede recuperar su lugar aunque haya cupo, y el sistema trata una decisión reversible como definitiva.

## Solution

La reinscripción crea una inscripción nueva. Las canceladas se conservan como historial y la unicidad se aplica solo entre vigentes, así que el alumno puede cancelar y reinscribirse sin límite mientras la actividad esté habilitada, no haya empezado y tenga cupo. El detalle vuelve a ofrecer el formulario y resume la última cancelación; "Mis inscripciones" y la vista docente muestran el historial completo.

## User Stories

1. Como alumno, quiero volver a inscribirme después de cancelar, para recuperar mi lugar.
2. Como alumno, quiero que la reinscripción exija las mismas condiciones que una primera inscripción, para que las reglas sean predecibles.
3. Como alumno, quiero ver mi nueva inscripción confirmada, para saber que ocupé un cupo.
4. Como alumno, quiero conservar mis cancelaciones anteriores como historial, para no perder mi decisión previa.
5. Como alumno, quiero que el detalle muestre el formulario otra vez y la fecha de la última cancelación, para entender el estado.
6. Como alumno, quiero que "Mis inscripciones" liste todas mis inscripciones, incluidas las cancelaciones, para ver mi recorrido.
7. Como alumno, quiero poder cancelar y reinscribirme repetidas veces, para no quedar trabado por un ciclo.
8. Como alumno, quiero que la nueva inscripción vuelva a ocupar cupo y actualice la disponibilidad, para que el catálogo sea fiel.
9. Como alumno, quiero que sin cupo se me rechace con el mensaje de siempre, para no crear expectativas falsas.
10. Como docente, quiero ver cada cancelación y cada vigente como historial, para auditar la ocupación real.
11. Como docente, quiero que el seed siga respetando la decisión del alumno, para que una demo no la pise.
12. Como docente, quiero que la base impida dos vigentes por alumno y actividad, para confiar en la demo.
13. Como docente, quiero que el README documente el nuevo recorrido, para que la clase siga el cambio.

## Implementation Decisions

- **Modelo**: la reinscripción es una fila nueva. Se reemplaza la constraint total por `UniqueConstraint(fields=["student", "activity"], condition=Q(cancelled_at__isnull=True))`. Migración nueva, sin datos que transformar.
- **Servicio**: `register()` deja de devolver `previously_cancelled`; si no hay fila vigente, evalúa habilitación, inicio y cupo como siempre y crea la fila. Se elimina el mensaje.
- **Resultados**: `previously_cancelled` desaparece. `already_registered` queda solo para una inscripción vigente.
- **Ventana**: la nueva inscripción vigente se cancela con la misma regla de 24 h.
- **Cupo**: sin cambios; ya cuenta solo vigentes.
- **Seed**: sigue verificando existencia sin filtrar estado; cualquier fila existente frena la recreación.
- **HTTP**: sin rutas nuevas; se reutiliza `register` y su `POST` con CSRF.
- **Plantillas**: el detalle sin vigente muestra el formulario cuando corresponde y la fecha de la última cancelación. "Mis inscripciones" y la vista docente listan todas las filas, vigentes primero.
- **Documentación**: ADR-0002, glosario y README.

## Testing Decisions

- Se reemplazan las pruebas de bloqueo por pruebas de reinscripción: fila nueva, cancelada conservada, cupo ocupado, reglas de habilitación/inicio/cupo y ciclos repetidos.
- **HTTP**: el detalle vuelve a ofrecer el formulario; el POST crea la fila y confirma; "Mis inscripciones" y la vista docente muestran el historial.
- **Concurrencia**: dos reinscripciones simultáneas dejan una sola vigente y una carrera cancelar↔reinscribir no produce dos vigentes.
- **Constraint**: prueba de base que rechaza dos vigentes del mismo alumno y actividad.

## Out of Scope

- Límite de ciclos o ventana exclusiva de reinscripción.
- Edición, borrado o exportación del historial.
- Notificaciones o correo.
- Cambios en la ventana de cancelación, cupos u horarios.
- Altas o bajas de inscripciones desde la administración.

## Further Notes

- `docs/adr/0002-la-reinscripcion-crea-una-inscripcion-nueva.md` supersede en parte al ADR-0001.
- El ticket 02 de `cancelar-inscripcion` queda superseded por este spec.
- El conteo de pruebas del README cambia.
