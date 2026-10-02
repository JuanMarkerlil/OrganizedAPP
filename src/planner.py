"""Lógica de negocio reutilizable."""
from __future__ import annotations

from datetime import date

from .models import Bloque, ChecklistItem, PlanDiario


def crear_plan(fecha: str | None = None) -> PlanDiario:
    return PlanDiario(fecha=fecha or date.today().isoformat())


def agregar_tarea(plan: PlanDiario, titulo: str, duracion_min: int = 25) -> Bloque:
    bloque = Bloque(titulo=titulo, tipo="tarea", duracion_min=duracion_min)
    plan.bloques.append(bloque)
    return bloque


def agregar_descanso(plan: PlanDiario, duracion_min: int = 5, titulo: str = "Descanso") -> Bloque:
    bloque = Bloque(titulo=titulo, tipo="descanso", duracion_min=duracion_min)
    plan.bloques.append(bloque)
    return bloque


def agregar_item_checklist(plan: PlanDiario, indice_bloque: int, texto: str) -> ChecklistItem:
    item = ChecklistItem(texto=texto)
    plan.bloques[indice_bloque].checklist.append(item)
    return item


def marcar_bloque(plan: PlanDiario, indice: int, completado: bool = True) -> None:
    plan.bloques[indice].completado = completado


def marcar_item(plan: PlanDiario, indice_bloque: int, indice_item: int, completado: bool = True) -> None:
    plan.bloques[indice_bloque].checklist[indice_item].completado = completado


def tiempo_total(plan: PlanDiario) -> int:
    return sum(b.duracion_min for b in plan.bloques)


def progreso(plan: PlanDiario) -> tuple[int, int]:
    """Devuelve (completados, total) de bloques."""
    total = len(plan.bloques)
    hechos = sum(1 for b in plan.bloques if b.completado)
    return hechos, total
