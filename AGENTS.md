# AGENTS.md

## Worktrees

Cada ticket se implementa en su propio worktree: `scripts/worktree.sh <nombre> [ref-base]` crea la rama `ticket/<nombre>` con el `.venv` del repo enlazado; `--remove <nombre>` lo limpia.

## Guardrails

Hay un hook de `pre-commit` en `.githooks/pre-commit` que corre `scripts/check.sh` (Django `check`, `makemigrations --check` y la suite de tests) solo cuando se toca código, plantillas, scripts, `pyproject.toml` o `uv.lock`. Para activarlo:

```
git config core.hooksPath .githooks
```

Esto se hace una vez por clone de worktree. No se commitea la configuración de git.

## Lógica de dominio

- Reglas de negocio: `activities/services.py` — las operaciones devuelven un código de resultado (`"registered"`, `"busy"`, etc.); las excepciones son solo para fallas inesperadas.
- Modelo de datos: `activities/models.py` (`Activity`, `Registration`).
- Vocabulario del dominio: `GLOSSARY.md` (términos como Inscripción, Cancelación, Reinscripción, Cupo disponible).
- Decisiones de arquitectura: `docs/adr/`.

## Agent skills

### Issue tracker

Issues and specs live as markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Five canonical roles, label strings equal to their names (defaults). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `GLOSSARY.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
