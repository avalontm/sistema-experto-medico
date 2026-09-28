# Preguntas de reflexión

## 1. ¿Qué limitaciones observaste en este enfoque durante la práctica?

- **Coincidencia exacta.** Una regla se activa solo si están todos sus síntomas. Con dos de tres síntomas el sistema no diagnostica, aunque el cuadro sea muy sugerente.
- **Sin gradación.** Un síntoma está presente o no. No hay intensidad, duración ni certeza: `tos_leve`, `tos_seca` y `tos_persistente` son símbolos distintos sin relación entre sí, y por eso hubo que declararlos por separado.
- **Conocimiento manual.** Cada enfermedad y cada variante de síntoma requiere escribir una regla a mano. Con cientos de enfermedades el mantenimiento se vuelve inmanejable.
- **Solapamiento entre enfermedades.** Varias comparten síntomas (fiebre, tos, congestión nasal). El sistema no tiene criterio para decidir cuál es más probable.
- **Sin síntomas negativos ni contexto.** No modela "sin fiebre", ni edad, antecedentes o resultados de laboratorio.
- **Orden de ejecución no controlado.** Sin `salience`, el orden de las reglas activadas puede variar entre ejecuciones.
- **Regla de respaldo dependiente del orden.** La regla de respaldo solo funciona correctamente gracias a su `salience` negativa.
- **Uso educativo.** El sistema no es una herramienta clínica; sus recomendaciones son ilustrativas.

## 2. ¿Cómo podría manejarse la incertidumbre en los síntomas?

- **Factores de certeza (estilo MYCIN).** Cada síntoma lleva un valor entre 0 y 1 y cada regla un peso. La certeza de la conclusión se calcula combinando ambos (por ejemplo, el mínimo de los síntomas multiplicado por la confianza de la regla). Se diagnostica por encima de un umbral.
- **Lógica difusa.** Variables como "fiebre" se representan con grados de pertenencia (fiebre alta, moderada, baja) en lugar de booleanos.
- **Razonamiento probabilístico.** Redes bayesianas que estimen P(enfermedad | síntomas) a partir de datos.
- **Coincidencia parcial.** Puntuar cada regla por la fracción de síntomas presentes y sugerir las enfermedades cuya puntuación supere un umbral.
- **Hechos con atributos de grado.** En `experta` se puede declarar `Sintoma(fiebre=0.7)` y usar condiciones con `P(...)` o funciones lambda para comparar contra un umbral.

## 3. En el Ejercicio 2, ¿qué implicaciones tiene para un sistema experto real que se activen varias reglas a la vez?

- **Diagnósticos múltiples o contradictorios.** El sistema emitió Gripe y Alergia sin señalar que son hipótesis en competencia. En medicina eso puede llevar a decisiones erróneas si no se prioriza.
- **Orden no garantizado.** Si las reglas tienen efectos secundarios o dependen unas de otras, un orden variable produce resultados inconsistentes. En esta práctica el orden cambió entre ejecuciones del mismo programa.
- **Necesidad de una estrategia de resolución de conflictos.** Se puede usar `salience` (prioridad), especificidad (preferir la regla con más condiciones), recencia o certeza acumulada.
- **Reproducibilidad y auditoría.** Un sistema real debe dar siempre la misma respuesta ante la misma entrada y poder explicar qué reglas se activaron y por qué.
- **Presentación de resultados.** Conviene devolver una lista ordenada por certeza o urgencia en lugar de imprimir cada diagnóstico por separado.
- **Diagnóstico diferencial y comorbilidad.** Varias reglas activas pueden indicar que el paciente tiene más de una condición a la vez, o que se necesitan pruebas adicionales para distinguirlas.
