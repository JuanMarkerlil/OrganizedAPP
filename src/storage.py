"""Persistencia del plan en JSON."""
from __future__ import annotations

import json
from pathlib import Path

from .models import PlanDiario

RUTA_POR_DEFECTO = Path(__file__).resolve().parent.parent / "data" / "plan.json"


def guardar_plan(plan: PlanDiario, ruta: Path = RUTA_POR_DEFECTO) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(plan.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")


def cargar_plan(ruta: Path = RUTA_POR_DEFECTO) -> PlanDiario | None:
    if not ruta.exists():
        return None
    data = json.loads(ruta.read_text(encoding="utf-8"))
    return PlanDiario.from_dict(data)
