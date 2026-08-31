from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


K = 0.166700
T_INICIAL = 97.0
T_SEGURA = 27.0
T_AMBIENTE_BASE = 18.0
T_AMBIENTE_ALTERNATIVA = 24.0


def temperatura(t: np.ndarray, ambiente: float) -> np.ndarray:
    return ambiente + (T_INICIAL - ambiente) * np.exp(-K * t)


def tiempo_seguro(ambiente: float) -> float:
    return np.log((T_INICIAL - ambiente) / (T_SEGURA - ambiente)) / K


t = np.linspace(0, 30, 601)
t_base = tiempo_seguro(T_AMBIENTE_BASE)
t_alternativa = tiempo_seguro(T_AMBIENTE_ALTERNATIVA)

fig, ax = plt.subplots(figsize=(9, 5.4))
ax.plot(t, temperatura(t, T_AMBIENTE_BASE), linewidth=2.2, label="Ambiente a 18 °C")
ax.plot(t, temperatura(t, T_AMBIENTE_ALTERNATIVA), linewidth=2.2, label="Ambiente a 24 °C")
ax.axhline(T_SEGURA, color="tab:red", linestyle="--", linewidth=1.5, label="Temperatura segura: 27 °C")
ax.scatter([t_base, t_alternativa], [T_SEGURA, T_SEGURA], color="tab:red", zorder=3)
ax.vlines(
    [t_base, t_alternativa],
    ymin=15,
    ymax=T_SEGURA,
    colors=["tab:blue", "tab:orange"],
    linestyles=":",
    linewidth=1.4,
)
ax.annotate(f"{t_base:.2f} min", (t_base, T_SEGURA), xytext=(-38, 12), textcoords="offset points")
ax.annotate(f"{t_alternativa:.2f} min", (t_alternativa, T_SEGURA), xytext=(8, 12), textcoords="offset points")
ax.set(xlabel="Tiempo (min)", ylabel="Temperatura (°C)", xlim=(0, 30), ylim=(15, 100))
ax.set_title("Comparación del enfriamiento según la temperatura ambiente")
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()

output_path = Path(__file__).resolve().parents[1] / "output" / "comparacion_escenarios.png"
fig.savefig(output_path, dpi=200)

print(f"Tiempo analítico con ambiente a 18 °C: {t_base:.2f} min")
print(f"Tiempo analítico con ambiente a 24 °C: {t_alternativa:.2f} min")
print(f"Gráfica guardada en: {output_path}")
