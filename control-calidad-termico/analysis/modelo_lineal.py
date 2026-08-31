from pathlib import Path

import matplotlib
matplotlib.use("Agg") # plugin para generar gráficos localmente, sin abrir pestañas adicionales. 
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Cargar datos registrados del CSV (no relevante para el análisis matemático)
csv_path = Path(__file__).resolve().parents[1] / "documentation" / "datos_registrados.csv"
datos_aleatorios = np.genfromtxt(csv_path, delimiter=",", names=True, dtype=float)

t = datos_aleatorios["t_min"]
T = datos_aleatorios["T_C"]
Tm = 18.0

# 1. Linealización: y = ln(T - Tm) usando el modelo de enfriamiento de Newton visto en clase
""" 
Recordamos que el modelo físico de enfriamiento de Newton 
es EXPONENCIAL, por lo que, algebraicamente, al aplicar un logaritmo natural, 
podemos llegar a la forma y = ln(T - Tm) = ln(C) - k*t, que es una ecuación 
lineal de la forma y = mx + b.
"""
y_lin = np.log(T - Tm) # equivalente a y = ln(T - Tm)

# 2. Regresión lineal por mínimos cuadrados usando librería scipy
m, intercepto, r, p, error_estandar = stats.linregress(t, y_lin) # este comando crea un modelo lineal a partir de la transformación previa, creando un ajuste lineal de la forma y = mx + b.
# equivalentes matemáticos al linealizar:
k_num = -m 
C_num = np.exp(intercepto)
r_cuadrada = r**2

# 3. Cálculo del tiempo para alcanzar la temperatura segura (27°C)
T_segura = 27.0
t_segura = (np.log(T_segura - Tm) - intercepto) / m # reemplazar datos reales en nuestro modelo

# 4. Visualización de la relación lineal
plt.figure(figsize=(8, 5))
plt.scatter(t, y_lin, color="tab:blue", label="Datos linealizados")
plt.plot(t, intercepto + m * t, color="tab:red", linewidth=2, label="Ajuste lineal")
plt.xlabel("Tiempo (min)")
plt.ylabel("ln(T - Tm)")
plt.title("Regresión lineal para enfriamiento")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parents[1] / "output" / "regresion_lineal.png", dpi=200)

print(f"--- RESULTADOS TÉCNICOS ---")
print(f"Ecuación linealizada: y = {m:.5f}t + {intercepto:.5f}")
print(f"Coeficiente k determinado: {k_num:.5f}")
print(f"Constante C numérica: {C_num:.5f} (T0 estimado = {C_num + Tm:.2f}°C)")
print(f"Coeficiente R²: {r_cuadrada:.5f}")
print(f"Tiempo seguro de trabajo (a 27°C): {t_segura:.2f} minutos")