# Sistema experto de diagnóstico médico

Sistema experto basado en reglas con encadenamiento hacia adelante (forward chaining), construido con la librería `experta`. Dado un conjunto de síntomas, el motor de inferencia activa las reglas que coinciden, declara un diagnóstico y muestra una recomendación.

## Estructura

```
.
├── main.py                      Ejecuta los 5 casos de prueba de la Parte 3
├── ejercicios.py                Ejercicio 1 (reglas nuevas) y Ejercicio 2 (conflictos)
├── orden_reglas.py              Mide el orden de ejecución en varias corridas
├── casos.py                     Síntomas de cada caso de prueba
├── reflexion.md                 Respuestas a las preguntas de reflexión
├── requirements.txt
└── sistema_experto/
    ├── compat.py                Compatibilidad de experta con Python 3.10+
    ├── hechos.py                Hechos: Sintoma, Diagnostico
    ├── motor_base.py            SistemaBase: 4 enfermedades + regla de respaldo
    ├── motor_ampliado.py        SistemaAmpliado: COVID-19, resfriado, bronquitis, sinusitis
    └── ejecucion.py             Crea el motor, lo reinicia, declara síntomas y lo ejecuta
```

## Instalación

Requiere Python 3.x.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py            # Parte 3: los 5 casos de prueba
python ejercicios.py      # Ejercicio 1 y Ejercicio 2
python orden_reglas.py    # Orden de activación en 20 ejecuciones
```

## Reglas

| Enfermedad | Síntomas requeridos |
|---|---|
| Gripe | fiebre, tos, dolor_garganta |
| Migraña | fiebre, dolor_cabeza, nauseas |
| Alergia | estornudos, congestion_nasal, picazon_ojos |
| Gastroenteritis | dolor_estomago, diarrea, vomitos |
| COVID-19 | fiebre, tos_seca, perdida_olfato |
| Resfriado común | congestion_nasal, estornudos, tos_leve |
| Bronquitis | tos_persistente, flema, dificultad_respiratoria |
| Sinusitis (propia) | congestion_nasal, dolor_facial, secrecion_espesa |
| Respaldo | se activa solo si no existe ningún hecho `Diagnostico` |

La regla de respaldo usa `NOT(Diagnostico())` y una `salience` negativa para ejecutarse al final.

## Resultados de los casos de prueba

| Caso | Síntomas | Resultado |
|---|---|---|
| 1 | fiebre, tos, dolor de garganta | Gripe |
| 2 | estornudos, congestión nasal, picazón en los ojos | Alergia |
| 3 | dolor de estómago, diarrea, vómitos | Gastroenteritis |
| 4 | cansancio, mareo | Sin diagnóstico (regla de respaldo) |
| 5 | fiebre, tos, dolor de garganta, estornudos, congestión nasal, picazón en los ojos | Gripe + Alergia |

Nota sobre el Caso 5: con los síntomas del enunciado (sin `picazon_ojos`) solo se activaría la regla de gripe, porque la alergia exige los tres síntomas. Se añadió `picazon_ojos` para que realmente se activen dos reglas a la vez.

## Ejercicio 2: conflicto de reglas

Con los síntomas del Caso 5:

- Se generan **2 diagnósticos**, Gripe y Alergia; ambas reglas se ejecutan siempre.
- El **orden es no determinista**: cambia entre ejecuciones del programa (`python orden_reglas.py` muestra la distribución).
- El resultado **no depende del orden de definición** de las reglas en la clase. `experta` recupera las reglas con `inspect.getmembers`, que las ordena alfabéticamente, y el orden final de las activaciones varía entre procesos. Una versión con las reglas definidas en orden inverso produjo la misma mezcla de órdenes.
- Para controlar el orden de forma explícita se debe usar `salience` en el decorador `@Rule`.

## Compatibilidad

`experta 1.9.4` depende de `frozendict 1.2`, que falla en Python 3.10+ por usar `collections.Mapping`. `sistema_experto/compat.py` restaura esos alias antes de importar la librería, así que basta con `pip install -r requirements.txt`.
