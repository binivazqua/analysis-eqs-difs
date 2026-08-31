# Reporte Técnico: Control de Calidad en el Tratamiento Térmico de Piezas Mecánicas

## A. Datos de Identificación

* **Institución:** Tecnológico de Monterrey
* **Unidad de Formación:** Modelación Matemática con Ecuaciones Diferenciales
* **Organización:** Mecánica Avanzada S.A.
* **Integrantes del Equipo:**
  * Biniza Verónica Vázquez Moreno (A01737294)
  * Joaquín Rosales González (A01771481)
  * Flor Denisse Hinojosa Hernández

---

## B. Introducción y Contextualización

### Descripción del Fenómeno Real
En la planta de manufactura de Mecánica Avanzada S.A., se fabrican ejes de acero para transmisiones industriales. Durante el proceso de templado, los componentes se calientan a elevadas temperaturas y posteriormente se trasladan a una zona de enfriamiento controlado en el taller. Para asegurar la calidad del material, optimizar la productividad y evitar riesgos por manipulación de piezas calientes, se requiere predecir con exactitud el comportamiento térmico del acero y determinar el tiempo necesario para alcanzar una temperatura segura de trabajo ($27 ^\circ\text{C}$).

### Definición Formal de Variables y Parámetros
* **Variable independiente:** Tiempo de enfriamiento, $t$, expresado en minutos ($\text{min}$).
* **Variable dependiente:** Temperatura de la pieza, $T(t)$, expresada en grados Celsius ($^\circ\text{C}$).
* **Parámetro ambiental de frontera:** Temperatura ambiente del taller, $T_{\text{amb}} = 18.0 ^\circ\text{C}$ (se asume constante).
* **Parámetro del sistema:** Coeficiente de enfriamiento del acero, $k$, expresado en $\text{min}^{-1}$, el cual depende de las propiedades físicas del material y las condiciones convectivas de la zona.
* **Condición inicial:** Temperatura medida al salir del horno en $t_0 = 0 \text{ min}$, $T(0) = T_0 = 97.0 ^\circ\text{C}$.

### Explicación del Método de Linealización
La dinámica de enfriamiento sigue un comportamiento exponencial. Como las herramientas de regresión por mínimos cuadrados procesan relaciones de primer grado, se aplica una transformación logarítmica para convertir la curva diferencial en una ecuación lineal.

Partiendo de la solución física de la Ley de Enfriamiento de Newton:
$$T(t) - T_{\text{amb}} = C e^{-kt}$$

Aplicando logaritmo natural a ambos lados de la igualdad:

$$\ln(T(t) - T_{\text{amb}}) = \ln(C e^{-kt})$$

Por propiedades algebraicas de los logaritmos ($\ln(a \cdot b) = \ln(a) + \ln(b)$ y $\ln(e^x) = x$):

$$\ln(T(t) - T_{\text{amb}}) = \ln(C) - kt$$

Al mapear esta estructura a la forma de una recta $y = mx + b$:
* **Variable ordenada ($y$):** $y = \ln(T(t) - T_{\text{amb}})$
* **Variable abscisa ($x$):** $x = t$
* **Pendiente ($m$):** $m = -k \implies k = -m$
* **Intersección ($b$):** $b = \ln(C) \implies C = e^b$

---

## C. Desarrollo

### 1. Modelación Numérica por Regresión Lineal
A partir de las mediciones del pirómetro óptico registradas en `documentation/datos_registrados.csv` durante los primeros 20 minutos, se calculó la serie linealizada $y_i = \ln(T_i - 18.0)$. Mediante el script `analysis/modelo_lineal.py` y la función `scipy.stats.linregress`, se ajustó la recta por mínimos cuadrados:

$$\ln(T - 18.0) = -0.16421 t + 4.36938$$

* **Pendiente ajustada ($m$):** $-0.16421 \text{ min}^{-1}$
* **Intersección con el eje $y$ ($b$):** $4.36938$
* **Coeficiente de determinación ($R^2$):** $> 0.998$ (alta precisión del ajuste)

Transformando los coeficientes numéricos a las constantes físicas:

$$k_{\text{num}} = -m = 0.16421 \text{ min}^{-1}$$

$$C_{\text{num}} = e^b = e^{4.36938} \approx 78.995 ^\circ\text{C}$$

El modelo empírico de temperatura estimado resulta:

$$T_{\text{num}}(t) = 18.0 + 78.995 e^{-0.16421 t}$$

---

### 2. Modelación Matemática Formal (EDO) y Solución Analítica

#### Planteamiento de la Ecuación Diferencial
La tasa de cambio de la temperatura del cuerpo es proporcional a la diferencia entre su temperatura actual y la del ambiente:

$$\frac{dT}{dt} = -k(T - T_{\text{amb}})$$

#### Solución por Separación de Variables

**Paso 1: Separación de términos**
$$\frac{dT}{T - T_{\text{amb}}} = -k \, dt$$

**Paso 2: Integración indefinida en ambos miembros**
$$\int \frac{1}{T - T_{\text{amb}}} \, dT = \int -k \, dt$$

$$\ln|T - T_{\text{amb}}| = -kt + C_1$$

**Paso 3: Despeje de $T(t)$**

$$|T - T_{\text{amb}}| = e^{-kt + C_1} = e^{C_1} e^{-kt}$$

Considerando $T(t) > T_{\text{amb}}$, se retira el valor absoluto y se define $C = e^{C_1}$:

$$T(t) = T_{\text{amb}} + C e^{-kt}$$

**Paso 4: Evaluación de la condición inicial $T(0) = 97.0^\circ\text{C}$ con $T_{\text{amb}} = 18.0^\circ\text{C}$**

$$97.0 = 18.0 + C e^{-k(0)} \implies C = 97.0 - 18.0 = 79.0^\circ\text{C}$$

**Paso 5: Solución particular analítica exacta**

$$T_{\text{analítico}}(t) = 18.0 + 79.0 e^{-k t}$$

**Paso 5: Solución particular analítica exacta**
$$T_{\text{analítico}}(t) = 18.0 + 79.0 e^{-k t}$$

#### Predicción del Tiempo para Alcanzar la Temperatura Segura ($27.0^\circ\text{C}$)

Sustituyendo $T(t) = 27.0^\circ\text{C}$ y el coeficiente $k = 0.16421\text{ min}^{-1}$:

$$27.0 = 18.0 + 79.0 e^{-0.16421 t}$$

$$9.0 = 79.0 e^{-0.16421 t}$$

$$\frac{9.0}{79.0} = e^{-0.16421 t}$$

Aplicando logaritmo natural:

$$\ln\left(\frac{9}{79}\right) = -0.16421 t$$

$$-2.17215 = -0.16421 t$$

$$t = \frac{-2.17215}{-0.16421} \approx 13.23\text{ minutos}$$

La pieza alcanza la temperatura segura de trabajo a los **13.23 minutos** ($\approx 13$ minutos y 14 segundos).
---

### 3. Explicación de Discrepancias entre lo Numérico y lo Analítico
Al comparar la constante teórica $C = 79.0 ^\circ\text{C}$ con la constante numérica del código $C_{\text{num}} \approx 78.995 ^\circ\text{C}$ (que sugiere un $T(0)$ numérico de $96.995 ^\circ\text{C}$), se observan pequeñas discrepancias originadas por:
* **Ruido aleatorio de medición:** Los datos del pirómetro incorporan fluctuaciones realistas ($\pm 0.2 - 0.5 ^\circ\text{C}$).
* **Ajuste global vs. Condición inicial puntual:** El modelo analítico exige la condición inicial exacta en $t = 0$ ($T_0 = 97.0$). En cambio, la regresión por mínimos cuadrados minimiza el error cuadrático acumulado global de los 21 puntos, promediando las desviaciones térmicas y suavizando ligeramente la intersección.

---

### 4. Análisis de Escenario: Cambio de Temperatura Ambiente a $24.0 ^\circ\text{C}$

Si la temperatura ambiental del taller aumenta a $T_{\text{amb}} = 24.0 ^\circ\text{C}$:

#### Solución Analítica

**Paso 1: Nueva EDO**
$$\frac{dT}{dt} = -k(T - 24.0)$$

**Paso 2: Estructura de la solución**
$$T(t) = 24.0 + C_{\text{nuevo}} e^{-kt}$$

**Paso 3: Determinación de $C_{\text{nuevo}}$ con $T(0) = 97.0 ^\circ\text{C}$**

$$97.0 = 24.0 + C_{\text{nuevo}} \implies C_{\text{nuevo}} = 73.0 ^\circ\text{C}$$

**Paso 4: Nueva función de temperatura**
$$T(t) = 24.0 + 73.0 e^{-0.16421 t}$$

#### Cálculo del nuevo tiempo para alcanzar los $27.0 ^\circ\text{C}$:

$$27.0 = 24.0 + 73.0 e^{-0.16421 t}$$

$$3.0 = 73.0 e^{-0.16421 t}$$

$$\ln\left(\frac{3}{73}\right) = -0.16421 t$$

$$-3.19184 = -0.16421 t$$

$$t = \frac{-3.19184}{-0.16421} \approx 19.44 \text{ minutos}$$

Al subir la temperatura ambiente a $24.0 ^\circ\text{C}$, el gradiente térmico disminuye, extendiendo el tiempo para alcanzar los $27.0 ^\circ\text{C}$ de **13.23 minutos a 19.44 minutos**.

---

## D. Conclusión e Interpretación

### Interpretación y Comportamiento Asintótico
El comportamiento cualitativo de la función cuando el tiempo tiende a infinito valida la coherencia física de la solución:

$$\lim_{t \to \infty} T(t) = \lim_{t \to \infty} \left(T_{\text{amb}} + C e^{-kt}\right) = T_{\text{amb}} + C(0) = T_{\text{amb}}$$

Independientemente del valor inicial $T_0$, el cuerpo se aproxima asintóticamente al equilibrio térmico con el entorno. Para el caso base, $\lim_{t \to \infty} T(t) = 18.0 ^\circ\text{C}$, y para el escenario alterado, $\lim_{t \to \infty} T(t) = 24.0 ^\circ\text{C}$.

### Recomendación Industrial
Con la constante $k = 0.16421 \text{ min}^{-1}$ validada, se recomienda a la planta programar el retiro seguro de las piezas de acero a los **14 minutos** en condiciones operativas normales ($18 ^\circ\text{C}$). En periodos donde la temperatura ambiental se eleve a $24 ^\circ\text{C}$, el protocolo de maniobra debe posponerse hasta haber transcurrido al menos **20 minutos**.

---

## E. Referencias (Estilo APA)

* Boyce, W. E., DiPrima, R. C., & Meade, D. B. (2021). *Elementary Differential Equations and Boundary Value Problems* (12th ed.). John Wiley & Sons.
* Incropera, F. P., DeWitt, D. P., Bergman, T. L., & Lavine, A. S. (2017). *Fundamentals of Heat and Mass Transfer* (8th ed.). John Wiley & Sons.
* Zill, D. G. (2018). *Ecuaciones diferenciales con problemas con valores en la frontera* (9.ª ed.). Cengage Learning.
