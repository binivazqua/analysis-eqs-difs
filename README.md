# Control de calidad en el tratamiento térmico de piezas mecánicas

Repositorio del equipo para la materia **Modelación Matemática con Ecuaciones Diferenciales (MA1033.106)** — Tecnológico de Monterrey.

El problema: un eje de acero sale del horno de templado a 97 °C y se deja enfriar en un taller a 18 °C. Con 21 mediciones de un pirómetro óptico (una por minuto, durante 20 minutos) estimamos el coeficiente de enfriamiento *k* resolviendo la ecuación diferencial de la Ley de Enfriamiento de Newton, y con eso determinamos el momento en que la pieza alcanza la temperatura segura de manipulación (27 °C).

## El reporte

El documento entregable está en:

**[`control-calidad-termico/output/reporte_control_calidad_termico.pdf`](control-calidad-termico/output/reporte_control_calidad_termico.pdf)**

Incluye portada, índice, planteamiento del modelo, solución de la EDO por separación de variables, la comprobación numérica con regresión lineal, el análisis de un segundo escenario (taller a 24 °C) y la fundamentación analítica de los resultados.

## Guía de archivos

Todo el trabajo vive en `control-calidad-termico/`:

| Archivo | Contenido |
|---------|-----------|
| `documentation/situacion_problema.md` | Enunciado del problema y planteamiento de la situación |
| `documentation/datos_registrados.csv` | Las 21 mediciones de temperatura del pirómetro |
| `documentation/reporte.md` | Bitácora del proceso: supuestos, metodología y referencias |
| `analysis/modelo_lineal.py` | Linealización ln(T−T_amb), regresión por mínimos cuadrados y cálculo de *k* |
| `analysis/graficar_escenarios.py` | Comparación de los dos escenarios de temperatura ambiente (18 °C y 24 °C) |
| `output/` | Gráficas generadas por los scripts y el PDF del reporte |
| `report/main.tex` | Fuente LaTeX del reporte |

## Resultados principales

- El coeficiente de enfriamiento obtenido de los datos es *k* = 0.1667 min⁻¹.
- Con el modelo numérico (regresión lineal), la pieza alcanza 27 °C a los **13.14 minutos**; la solución exacta de la EDO da **13.03 minutos**. La diferencia de ~6 segundos se explica en el reporte por el sesgo que introduce la linealización.
- Si el taller estuviera a 24 °C, el tiempo requerido sube a **19.15 minutos**.

## Equipo

| Integrante | Matrícula |
|------------|-----------|
| Biniza Verónica Vázquez Moreno | A01737294 |
| Joaquín Rosales González | A01771481 |
| Flor Denisse Hinojosa Hernández | A00843678 |
