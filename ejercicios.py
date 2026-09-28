from casos import CASO_EJERCICIO_2, CASOS_EJERCICIO_1
from sistema_experto import SistemaAmpliado
from sistema_experto.ejecucion import ejecutar


def ejercicio_1():
    print("Ejercicio 1: sistema ampliado")
    for enfermedad, sintomas in CASOS_EJERCICIO_1.items():
        print(f"Prueba {enfermedad}: {', '.join(sintomas)}")
        ejecutar(SistemaAmpliado, sintomas)
        print()


def ejercicio_2():
    print("Ejercicio 2: conflicto de reglas")
    print(f"Síntomas: {', '.join(CASO_EJERCICIO_2)}")
    motor = ejecutar(SistemaAmpliado, CASO_EJERCICIO_2)
    print()
    print(f"Diagnósticos generados: {len(motor.diagnosticos())}")
    print(f"Orden de ejecución: {' -> '.join(motor.historial)}")


if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
