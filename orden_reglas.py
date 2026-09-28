import subprocess
import sys
from collections import Counter

REPETICIONES = 20

CODIGO = (
    "import io, contextlib\n"
    "from casos import CASO_EJERCICIO_2\n"
    "from sistema_experto import SistemaAmpliado\n"
    "from sistema_experto.ejecucion import ejecutar\n"
    "with contextlib.redirect_stdout(io.StringIO()):\n"
    "    motor = ejecutar(SistemaAmpliado, CASO_EJERCICIO_2)\n"
    "print(' -> '.join(motor.historial))\n"
)


def main():
    conteo = Counter()
    for _ in range(REPETICIONES):
        salida = subprocess.run(
            [sys.executable, "-c", CODIGO], capture_output=True, text=True, check=True
        )
        conteo[salida.stdout.strip()] += 1

    print(f"Órdenes observados en {REPETICIONES} ejecuciones independientes:")
    for orden, veces in conteo.most_common():
        print(f"  {orden}: {veces}")


if __name__ == "__main__":
    main()
