# Situación problema

**Control de Calidad en el Tratamiento Térmico de Piezas Mecánicas**
(modelación del enfriamiento de una pieza mecánica)

En la planta de manufactura de Mecánica Avanzada S.A., se fabrican ejes de acero para transmisiones industriales. Como parte del proceso de templado, las piezas salen del horno a altas temperaturas y se trasladan a una zona de enfriamiento controlado en el taller, donde la temperatura ambiental se mantiene constante a 18 °C.

Para optimizar el ritmo de producción y prevenir accidentes por manipulación de piezas calientes, el departamento de ingeniería necesita determinar el coeficiente de enfriamiento del acero (k) en las condiciones específicas del taller. Con este parámetro, se podrá formular la ecuación diferencial del proceso y predecir el tiempo exacto en que la pieza alcanza una temperatura segura de trabajo (27 °C). A partir de las mediciones de temperatura registradas por un pirómetro óptico durante los primeros 20 minutos, se debe utilizar regresión lineal para determinar el coeficiente k.

## Entregables

a) Tabla de datos registrados — `datos_registrados.csv`
b) Regresión lineal para obtener k — `analysis/`
c) Ecuación diferencial y predicción del tiempo a 27 °C — `analysis/` + `output/`

## Supuestos

- Temperatura ambiente constante: T_amb = 18 °C
- Ley de Enfriamiento de Newton: dT/dt = -k(T - T_amb)
- Datos simulados: decrecientes desde 97 °C hasta ~20 °C en 20 min, con ruido aleatorio realista (±0.2–0.5 °C) sobre una curva exponencial base con k ≈ 0.164 min⁻¹.
