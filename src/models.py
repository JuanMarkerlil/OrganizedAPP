"""Modelos de datos de la app."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import List


@dataclass
class ChecklistItem:
    texto: str
    completado: bool = False


@dataclass
class Bloque:
    """Bloque de tiempo: tarea, descanso o libre."""
    titulo: str
    tipo: str = "tarea"  # "tarea" | "descanso"
    duracion_min: int = 25
    completado: bool = False
    checklist: List[ChecklistItem] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Bloque":
        data = dict(data)
        data["checklist"] = [ChecklistItem(**item) for item in data.get("checklist", [])]
        return cls(**data)


@dataclass
class PlanDiario:
    fecha: str
    bloques: List[Bloque] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"fecha": self.fecha, "bloques": [b.to_dict() for b in self.bloques]}

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDiario":
        return cls(fecha=data["fecha"], bloques=[Bloque.from_dict(b) for b in data.get("bloques", [])])
