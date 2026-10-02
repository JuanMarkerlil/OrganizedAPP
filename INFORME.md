# INFORME.md

## 2026-10-01 — Creación de la base del MVP

**Stack:** Python 3.14, sin dependencias externas.

**Estructura creada:**
```
OrganizedApp/
├── main.py          # Punto de entrada
├── INFORME.md       # Este archivo
└── src/
    ├── __init__.py
    ├── models.py    # PlanDiario, Bloque, ChecklistItem (dataclasses)
    ├── planner.py   # Lógica de negocio reutilizable
    ├── storage.py   # Persistencia en JSON (data/plan.json)
    └── cli.py       # Menú interactivo
```

**Funciones reutilizables (src/planner.py):**
- `crear_plan()`, `agregar_tarea()`, `agregar_descanso()`
- `agregar_item_checklist()`, `marcar_bloque()`, `marcar_item()`
- `tiempo_total()`, `progreso()`

**MVP funcional:** agregar tareas y descansos con duración, checklist por bloque, marcar completados, progreso y tiempo total, guardado automático en JSON.

**Prueba:** smoke test OK (crear plan, agregar bloques, guardar y recargar).

**Cómo ejecutar:** `python main.py`

## 2026-10-01 — Primer commit

- Repo Git inicializado (rama `master`), commit raíz `b9ea455`: "Estructuración y planeación".
- Agregado `.gitignore` (excluye `__pycache__/` y `data/plan.json`).
