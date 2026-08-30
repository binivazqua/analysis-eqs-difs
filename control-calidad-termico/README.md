# Control de Calidad — Tratamiento Térmico de Piezas Mecánicas

Modelación del enfriamiento de una pieza de acero (Ley de Enfriamiento de Newton) para determinar el coeficiente de enfriamiento **k** y predecir el tiempo en que la pieza alcanza una temperatura segura de trabajo (27 °C), a partir de datos registrados por pirómetro óptico durante los primeros 20 minutos.

## Estructura del repositorio

```
control-calidad-termico/
├── documentation/   # Situación problema, datos registrados, notas y referencias
├── analysis/        # Scripts de Python: regresión lineal, cálculo de k, EDO
└── output/          # Resultados generados: gráficas, tablas, modelo final
```

- **documentation/** — enunciado del problema, tabla de datos registrados (pirómetro), bitácora de supuestos.
- **analysis/** — código de análisis: transformación ln(T−T_amb), regresión lineal para obtener k, solución de la EDO.
- **output/** — artefactos generados por los scripts: CSVs de resultados, gráficas (.png), reporte final.

## Datos base

Temperatura ambiente: 18 °C
Rango de datos: 97 °C → ~20 °C, en intervalos de 1 min durante 20 min.

Ver `documentation/datos_registrados.csv`.

## Equipo

_(agregar nombres de los integrantes)_
