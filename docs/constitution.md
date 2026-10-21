# Constitución de OrganizedApp

> **Versión:** 0.1 (borrador base)
> **Última revisión:** 2026-10-01
> **Propósito:** Este documento es la *base* sobre la que se gobierna el proyecto.
> No es un texto cerrado: crece con la app. Cada mejora o lección aprendida puede
> convertirse en un artículo nuevo o en una enmienda (ver Proceso de Enmienda).

---

## Preámbulo

OrganizedApp nace como una aplicación CLI en Python para planificar rutinas
diarias: tareas, descansos, checklists y métricas de progreso. Su valor está en
la **simplicidad, la claridad y la constancia**. Todo lo que se agregue al
proyecto debe reforzar esas tres ideas y nada más.

---

## Artículo I — Principios fundamentales

1. **Simplicidad sobre complejidad.** Si una funcionalidad puede resolverse con
   la librería estándar, se resuelve con la librería estándar.
2. **Un solo propósito por módulo.** Cada archivo de `src/` tiene una
   responsabilidad clara y acotada.
3. **La lógica de negocio vive en `planner.py`.** La CLI y el almacenamiento son
   *adaptadores*, nunca el corazón del sistema.
4. **Los datos del usuario son sagrados.** Nada debe corromper ni perder
   `data/plan.json`.
5. **Todo cambio es trazable.** Cada avance se registra en `INFORME.md` y en el
   historial de Git.

---

## Artículo II — Reglas técnicas innegociables

1. Python 3.14 y **únicamente** librería estándar. Prohibido `pip install`.
2. Modelos de datos expresados con `dataclasses` en `src/models.py`.
3. La persistencia en JSON debe sobrevivir a cambios de versión: cualquier
   modificación del esquema exige migración o compatibilidad retroactiva.
4. Los archivos de datos del usuario (`data/plan.json`) nunca se trackean en Git.
5. Ninguna estructura grande cambia sin pasar antes por el **modo Plan**.

---

## Artículo III — Calidad y verificación

1. Antes de cada commit, ejecutar el smoke test de `src/` (skill `smoke-test`).
2. Ninguna función nueva se da por terminada sin haberse ejecutado al menos una
   vez en un caso real.
3. Los errores se manejan con mensajes claros en español; nunca con fallos
   silenciosos.
4. El código se lee antes de optimizarse. Legibilidad primero.

---

## Artículo IV — Flujo de trabajo

1. **Consultar** el estado del proyecto (`INFORME.md`, commits recientes) antes
   de empezar cualquier tarea.
2. **Planear** cambios no triviales antes de escribir código.
3. **Construir** siguiendo la modularidad existente.
4. **Verificar** con el smoke test.
5. **Registrar** el avance en `INFORME.md` y hacer commit con mensaje claro.

---

## Artículo V — Evolución de esta Constitución

Esta Constitución es un documento **vivo**. Su fuerza no está en quedar intacta,
sino en acompañar el crecimiento del proyecto sin perder su núcleo.

### Proceso de Enmienda

1. **Propuesta.** Se anota la mejora como nueva entrada en el *Historial de
   Enmiendas* (abajo), con fecha y justificación.
2. **Redacción.** Se edita el artículo correspondiente o se agrega uno nuevo,
   manteniendo el estilo conciso y accionable.
3. **Aprobación.** Todo cambio debe quedar registrado en `INFORME.md` en la
   sesión en que se realiza.
4. **Revisión.** Al menos una vez al mes (o tras un hito importante), revisar la
   Constitución completa y retirar lo que ya no aplique.

### Reglas de calidad para una enmienda

- Cada artículo debe ser **accionable** (decir qué hacer, no solo qué pensar).
- Nunca más de **7 subpuntos por artículo**; si crece, se divide en un artículo
  nuevo.
- Si un principio entra en conflicto con otro, **gana el Preámbulo** (simplicidad,
  claridad y constancia).

### Historial de Enmiendas

| # | Fecha | Artículo | Cambio | Motivo |
|---|-------|----------|--------|--------|
| 0 | 2026-10-01 | Todos | Creación de la versión base 0.1 | Punto de partida del proyecto |

---

## Checklist de revisión periódica

- [ ] ¿Los artículos siguen reflejando cómo trabaja realmente el proyecto?
- [ ] ¿Ha aparecido alguna lección aprendida que deba incorporarse?
- [ ] ¿Algún artículo quedó obsoleto por un cambio técnico?
- [ ] ¿`INFORME.md` refleja los últimos avances?
