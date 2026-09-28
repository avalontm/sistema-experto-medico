from experta import NOT, KnowledgeEngine, Rule

from .hechos import Diagnostico, Sintoma


class SistemaBase(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.historial = []

    def diagnosticos(self):
        return [h["enfermedad"] for h in self.facts.values() if isinstance(h, Diagnostico)]

    def _diagnosticar(self, enfermedad, recomendacion):
        self.historial.append(enfermedad)
        self.declare(Diagnostico(enfermedad=enfermedad))
        print(f"  Diagnóstico: {enfermedad}")
        print(f"  Recomendación: {recomendacion}")

    @Rule(Sintoma(fiebre=True), Sintoma(tos=True), Sintoma(dolor_garganta=True))
    def gripe(self):
        self._diagnosticar(
            "Gripe",
            "Reposo, abundantes líquidos y antipiréticos. Consulte a un médico si la fiebre persiste.",
        )

    @Rule(Sintoma(fiebre=True), Sintoma(dolor_cabeza=True), Sintoma(nauseas=True))
    def migrana(self):
        self._diagnosticar(
            "Migraña",
            "Descansar en un lugar oscuro y silencioso, hidratarse y evitar desencadenantes conocidos.",
        )

    @Rule(Sintoma(estornudos=True), Sintoma(congestion_nasal=True), Sintoma(picazon_ojos=True))
    def alergia(self):
        self._diagnosticar(
            "Alergia",
            "Evitar el alérgeno y considerar un antihistamínico previa consulta médica.",
        )

    @Rule(Sintoma(dolor_estomago=True), Sintoma(diarrea=True), Sintoma(vomitos=True))
    def gastroenteritis(self):
        self._diagnosticar(
            "Gastroenteritis",
            "Hidratación con suero oral, dieta blanda y consulta médica si hay deshidratación.",
        )

    @Rule(NOT(Diagnostico()), salience=-100)
    def sin_diagnostico(self):
        print("  No se pudo determinar un diagnóstico.")
        print("  Recomendación: consulte a un médico.")
