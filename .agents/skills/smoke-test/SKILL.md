---
name: smoke-test
description: Ejecuta una prueba de humo (smoke test) del MVP de OrganizedApp antes de hacer commit. Úsala cuando el usuario pida verificar que la app funciona después de cambios en src/.
---

# Skill: smoke-test

Objetivo: validar rápidamente que el MVP de OrganizedApp sigue funcionando tras cambios en el código.

## Pasos

1. Ejecutar desde la raíz del proyecto (`C:\Users\USUARIO\Desktop\OrganizedApp`):
   ```
   python -c "from src import planner, storage; p = planner.crear_plan(); planner.agregar_tarea(p, 'Prueba', 25); planner.agregar_descanso(p, 5); planner.agregar_item_checklist(p, 0, 'Item'); planner.marcar_bloque(p, 0); planner.marcar_item(p, 0, 0); print('progreso:', planner.progreso(p)); print('tiempo_total:', planner.tiempo_total(p))"
   ```
2. Verificar persistencia sin tocar los datos reales del usuario: usar una ruta temporal para `guardar_plan`/`cargar_plan` (por ejemplo en la carpeta temp del sistema) y confirmar que el plan recargado coincide.
3. NO modificar `data/plan.json` — ese archivo contiene datos del usuario.
4. Reportar el resultado:
   - Si todas las funciones corren y la persistencia funciona → "Smoke test OK".
   - Si algo falla → mostrar el error completo y sugerir qué archivo revisar (`models.py`, `planner.py`, `storage.py`).

## Reglas

- Usar solo la librería estándar de Python; no instalar nada.
- No commitear ni hacer push desde esta skill.
