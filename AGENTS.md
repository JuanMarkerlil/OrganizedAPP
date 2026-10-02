```
# Instrucciones para Agentes (agents.md)

## Contexto del Proyecto
Aplicación CLI "OrganizedApp" para la gestión y planificación de rutinas diarias (tareas, descansos, checklists y métricas de progreso) [1, 2].

## Stack Técnico y Estructura
- Python 3.14 utilizando exclusivamente la librería estándar (sin dependencias externas) [1].
- `main.py` — Punto de entrada interactivo [1].
- `src/models.py` — Modelos de datos (`PlanDiario`, `Bloque`, `ChecklistItem` mediante `dataclasses`) [1].
- `src/planner.py` — Lógica de negocio reutilizable (`crear_plan`, `agregar_tarea`, `marcar_bloque`, `progreso`, etc.) [1, 2].
- `src/storage.py` — Persistencia local en formato JSON (`data/plan.json`) [1].
- `src/cli.py` — Interfaz de usuario por consola / menú interactivo [1].
- `INFORME.md` / `memory.md` — Registro de decisiones, cambios y estado del MVP [1].

## Normas y Convenciones
- Mantener modularidad estricta: la lógica de negocio debe residir en `src/planner.py` y no en la CLI ni en `main.py` [1].
- Usar `dataclasses` para estructurar la información en `src/models.py` [1].
- Asegurar que la persistencia mantenga el autoguardado y recarga limpia desde `data/plan.json` [1, 2].

## Límites y Prohibiciones (Lo que NO debes hacer)
- NUNCA instalar ni requerir librerías de terceros (`pip install`) [1].
- NUNCA modificar la estructura JSON existente en `data/plan.json` sin migración o compatibilidad retroactiva [1].
- NUNCA realizar cambios estructurales grandes sin pasar previamente por el modo Plan [1, 3].

## Flujo de Trabajo y Memoria
- Al iniciar cualquier tarea, consulta `INFORME.md` (o la memoria persistente) para revisar el estado actual y los commits recientes [1, 4, 5].
- Al finalizar cada tarea, actualiza `INFORME.md` con los avances, funciones agregadas o ajustes realizados [1, 6].

```

---