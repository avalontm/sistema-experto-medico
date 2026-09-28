from casos import CASOS_PARTE_3
from sistema_experto import SistemaBase
from sistema_experto.ejecucion import ejecutar


def main():
    resumen = []
    for nombre, sintomas in CASOS_PARTE_3.items():
        print(f"{nombre}: {', '.join(sintomas)}")
        motor = ejecutar(SistemaBase, sintomas)
        resumen.append((nombre, motor.historial or ["Sin diagnóstico"]))
        print()

    print("Resumen")
    for nombre, diagnosticos in resumen:
        print(f"  {nombre}: {' + '.join(diagnosticos)}")


if __name__ == "__main__":
    main()
