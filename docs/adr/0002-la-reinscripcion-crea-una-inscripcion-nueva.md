# La reinscripción crea una inscripción nueva

Status: accepted

El ADR-0001 conserva las inscripciones canceladas como historial y, por eso, bloqueaba la reinscripción. Ahora el alumno puede volver a inscribirse: cada reinscripción crea una fila nueva y la unicidad se aplica solo entre inscripciones vigentes (constraint parcial `student + activity where cancelled_at is null`). Así cada cancelación queda como registro histórico y el alumno puede cancelar y reinscribirse repetidas veces sin perder ninguna decisión previa.

## Considered Options

- **Reactivar la misma fila.** Menos cambios, pero borra el instante de la cancelación anterior y contradice el motivo por el que el ADR-0001 conserva las filas.
- **Reactivar + tabla de historial.** Conserva todo, pero agrega una entidad y un join para un dato que una fila ya puede representar.
- **Filas múltiples con unicidad parcial.** Elegida: el historial es la tabla misma y la base sigue impidiendo dos vigentes.

## Consequences

- `previously_cancelled` desaparece: reinscribirse devuelve `registered`.
- La constraint total `one_registration_per_student_activity` se reemplaza por una parcial; migración sin transformar datos.
- "Mis inscripciones" y la vista docente muestran todas las filas; el detalle resume la última cancelación.
- El seed sigue respetando cualquier fila existente, vigente o cancelada.
- Se mantiene la conservación de canceladas del ADR-0001; solo se levanta el bloqueo de reinscripción.
