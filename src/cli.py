"""CLI interactiva básica."""
from __future__ import annotations

from .models import PlanDiario
from . import planner, storage


def mostrar_plan(plan: PlanDiario) -> None:
    print(f"\n=== Plan del {plan.fecha} ===")
    if not plan.bloques:
        print("  (sin bloques todavía)")
    for i, b in enumerate(plan.bloques):
        marca = "[x]" if b.completado else "[ ]"
        print(f"  {i}. {marca} ({b.tipo}) {b.titulo} - {b.duracion_min} min")
        for j, item in enumerate(b.checklist):
            m = "[x]" if item.completado else "[ ]"
            print(f"       {j}. {m} {item.texto}")
    hechos, total = planner.progreso(plan)
    print(f"Progreso: {hechos}/{total} | Tiempo total: {planner.tiempo_total(plan)} min\n")


def cargar_o_crear() -> PlanDiario:
    plan = storage.cargar_plan()
    return plan if plan is not None else planner.crear_plan()


def main() -> None:
    plan = cargar_o_crear()
    opciones = {
        "1": "Ver plan",
        "2": "Agregar tarea",
        "3": "Agregar descanso",
        "4": "Completar bloque",
        "5": "Agregar item checklist",
        "6": "Guardar",
        "0": "Salir",
    }
    while True:
        for k, v in opciones.items():
            print(f"{k}. {v}")
        op = input("> ").strip()
        if op == "1":
            mostrar_plan(plan)
        elif op == "2":
            t = input("Título: ")
            d = int(input("Duración (min) [25]: ") or 25)
            planner.agregar_tarea(plan, t, d)
        elif op == "3":
            d = int(input("Duración descanso (min) [5]: ") or 5)
            planner.agregar_descanso(plan, d)
        elif op == "4":
            i = int(input("Índice del bloque: "))
            planner.marcar_bloque(plan, i)
        elif op == "5":
            i = int(input("Índice del bloque: "))
            t = input("Texto del item: ")
            planner.agregar_item_checklist(plan, i, t)
        elif op == "6":
            storage.guardar_plan(plan)
            print("Guardado.")
        elif op == "0":
            storage.guardar_plan(plan)
            break


if __name__ == "__main__":
    main()
