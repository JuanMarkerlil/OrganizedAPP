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

## 2026-10-01 — Sincronización con GitHub

- Remoto `origin` configurado: `https://github.com/JuanMarkerlil/OrganizedAPP.git`.
- Borradas credenciales cacheadas de `juanRodriguex`; push exitoso a la cuenta `JuanMarkerlil`.
- Identidad Git (local y global) unificada: `JuanMarkerlil / juandiegocedeu@gmail.com`.
- Historial reescrito con `git filter-branch` para atribuir ambos commits a JuanMarkerlil y force-push aplicado.

## 2026-10-01 — App en uso

- Comando de ejecución verificado: `python main.py` (desde la carpeta del proyecto).
