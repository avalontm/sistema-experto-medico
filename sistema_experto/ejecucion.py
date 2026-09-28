from .hechos import Sintoma


def ejecutar(clase_motor, sintomas):
    motor = clase_motor()
    motor.reset()
    motor.declare(Sintoma(**{nombre: True for nombre in sintomas}))
    motor.run()
    return motor
