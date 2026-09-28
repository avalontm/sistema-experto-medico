from experta import Rule

from .hechos import Sintoma
from .motor_base import SistemaBase


class SistemaAmpliado(SistemaBase):
    @Rule(Sintoma(fiebre=True), Sintoma(tos_seca=True), Sintoma(perdida_olfato=True))
    def covid19(self):
        self._diagnosticar(
            "COVID-19",
            "Aislarse, realizarse una prueba y vigilar la dificultad respiratoria.",
        )

    @Rule(Sintoma(congestion_nasal=True), Sintoma(estornudos=True), Sintoma(tos_leve=True))
    def resfriado_comun(self):
        self._diagnosticar(
            "Resfriado común",
            "Reposo, líquidos calientes y control de síntomas con medicación de venta libre.",
        )

    @Rule(Sintoma(tos_persistente=True), Sintoma(flema=True), Sintoma(dificultad_respiratoria=True))
    def bronquitis(self):
        self._diagnosticar(
            "Bronquitis",
            "Evitar irritantes como el humo, mantenerse hidratado y consultar a un médico.",
        )

    @Rule(Sintoma(congestion_nasal=True), Sintoma(dolor_facial=True), Sintoma(secrecion_espesa=True))
    def sinusitis(self):
        self._diagnosticar(
            "Sinusitis",
            "Lavados nasales con solución salina, compresas tibias y consulta médica si dura más de 10 días.",
        )
