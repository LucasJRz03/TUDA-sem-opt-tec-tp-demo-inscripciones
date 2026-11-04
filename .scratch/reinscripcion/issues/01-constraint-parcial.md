# 01: Reemplazar la unicidad total por una parcial sobre inscripciones vigentes

**What to build:** La base permite varias filas por alumno y actividad, pero nunca dos vigentes. Se reemplaza la constraint total `one_registration_per_student_activity` por una `UniqueConstraint` parcial sobre `(student, activity)` con `condition=cancelled_at IS NULL`, con migración nueva y sin transformar datos. La constraint parcial es la que sostiene todo el historial de cancelaciones de la feature.

**Blocked by:** —

**Spec:** ../spec.md

**Status:** done

- [x] `Registration.Meta.constraints` usa una constraint parcial sobre inscripciones vigentes.
- [x] La migración elimina la constraint total y crea la parcial, sin tocar filas existentes.
- [x] Una prueba de base confirma que dos vigentes del mismo alumno y actividad fallan con `IntegrityError`.
- [x] Una prueba de base confirma que una vigente y una cancelada del mismo alumno y actividad conviven.

## Comments

Implementado en `fa8a9f8`. Pruebas de base en `activities/tests/test_models.py`: convivencia vigente+cancelada, historial con varias canceladas y rechazo de dos vigentes. Suite completa: 66 pruebas OK. `makemigrations --check` sin cambios. Code review sin violaciones duras; se mantiene el nombre de la constraint porque el ticket identifica la total reemplazada con ese nombre.
