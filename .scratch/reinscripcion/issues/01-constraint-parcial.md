# 01: Reemplazar la unicidad total por una parcial sobre inscripciones vigentes

**What to build:** La base permite varias filas por alumno y actividad, pero nunca dos vigentes. Se reemplaza la constraint total `one_registration_per_student_activity` por una `UniqueConstraint` parcial sobre `(student, activity)` con `condition=cancelled_at IS NULL`, con migración nueva y sin transformar datos. La constraint parcial es la que sostiene todo el historial de cancelaciones de la feature.

**Blocked by:** —

**Spec:** ../spec.md

**Status:** ready-for-agent

- [ ] `Registration.Meta.constraints` usa una constraint parcial sobre inscripciones vigentes.
- [ ] La migración elimina la constraint total y crea la parcial, sin tocar filas existentes.
- [ ] Una prueba de base confirma que dos vigentes del mismo alumno y actividad fallan con `IntegrityError`.
- [ ] Una prueba de base confirma que una vigente y una cancelada del mismo alumno y actividad conviven.
