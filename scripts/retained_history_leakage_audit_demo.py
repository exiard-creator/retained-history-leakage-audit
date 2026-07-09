import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

# Dimensionless audit model.
# Gamma_target is retained internal history.
# J_out is leakage across the target boundary.
# D_observer is accumulated observer data obtained from leakage.
t_max = 30.0
dt = 0.01
t = np.arange(0.0, t_max + dt, dt)

gamma = np.zeros_like(t)
data = np.zeros_like(t)
amplitude = np.zeros_like(t)
leak = np.zeros_like(t)
leak_rate = np.zeros_like(t)

# Parameters chosen for a clear conceptual demonstration, not a fit.
gamma[0] = 0.25
amplitude[0] = 0.25
input_rate = 0.11
consolidation = 0.08
baseline_leak = 0.035
erase_rate = 0.018
observer_gain = 0.92
amp_pump = 0.08
amp_damping = 0.025

# A measurement/coupling window forces extra leakage.
measurement_center = 15.0
measurement_width = 1.6
measurement_strength = 0.24
measurement_profile = measurement_strength * np.exp(-0.5 * ((t - measurement_center) / measurement_width) ** 2)

for idx in range(len(t) - 1):
    leak_rate[idx] = baseline_leak + measurement_profile[idx]
    leak[idx] = leak_rate[idx] * gamma[idx]

    dgamma = input_rate + consolidation * amplitude[idx] - leak[idx] - erase_rate * gamma[idx]
    ddata = observer_gain * leak[idx]
    damped_leak = 0.35 * leak_rate[idx] * amplitude[idx]
    damplitude = amp_pump - amp_damping * amplitude[idx] - damped_leak

    gamma[idx + 1] = max(gamma[idx] + dt * dgamma, 0.0)
    data[idx + 1] = data[idx] + dt * ddata
    amplitude[idx + 1] = max(amplitude[idx] + dt * damplitude, 0.0)

leak_rate[-1] = baseline_leak + measurement_profile[-1]
leak[-1] = leak_rate[-1] * gamma[-1]

target_asset = gamma
target_liability = leak
observer_asset = np.gradient(data, dt)
observer_opacity = gamma

fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True)

axes[0, 0].plot(t, gamma, label=r"retained history $\Gamma_{target}$", color="#1f77b4")
axes[0, 0].plot(t, amplitude, label=r"coherent amplitude $A$", color="#2ca02c")
axes[0, 0].set_ylabel("target retained structure")
axes[0, 0].legend(frameon=False)
axes[0, 0].set_title("Target-side assets")

axes[0, 1].plot(t, leak, label=r"leakage $J_{out}$", color="#d62728")
axes[0, 1].plot(t, measurement_profile, label="measurement coupling", color="#9467bd", linestyle="--")
axes[0, 1].set_ylabel("target loss channel")
axes[0, 1].legend(frameon=False)
axes[0, 1].set_title("Target-side liability")

axes[1, 0].plot(t, data, label=r"observer data $D_{observer}$", color="#ff7f0e")
axes[1, 0].plot(t, observer_asset, label="instantaneous data gain", color="#8c564b", alpha=0.8)
axes[1, 0].set_xlabel("time")
axes[1, 0].set_ylabel("observer record")
axes[1, 0].legend(frameon=False)
axes[1, 0].set_title("Observer-side asset")

axes[1, 1].plot(t, target_asset - target_asset[0], label=r"$\Delta\Gamma_{target}$", color="#1f77b4")
axes[1, 1].plot(t, data - data[0], label=r"$\Delta D_{observer}$", color="#ff7f0e")
axes[1, 1].axvline(measurement_center, color="black", lw=1, alpha=0.35)
axes[1, 1].set_xlabel("time")
axes[1, 1].set_ylabel("audit change")
axes[1, 1].legend(frameon=False)
axes[1, 1].set_title("Boundary sign reversal")

for ax in axes.ravel():
    ax.grid(alpha=0.25)

fig.suptitle("Retained-history/leakage audit: target loss becomes observer data", y=0.995)
fig.tight_layout()
fig.savefig(OUT / "retained_history_leakage_audit_demo.png", dpi=200)

summary = {
    "t_max": float(t_max),
    "dt": float(dt),
    "initial_gamma": float(gamma[0]),
    "final_gamma": float(gamma[-1]),
    "initial_observer_data": float(data[0]),
    "final_observer_data": float(data[-1]),
    "max_leakage": float(leak.max()),
    "measurement_center": float(measurement_center),
    "measurement_strength": float(measurement_strength),
    "interpretation": "target retained history is an asset for the target; leakage is a loss for the target but a data gain for the observer",
}
(OUT / "retained_history_leakage_audit_demo.json").write_text(json.dumps(summary, indent=2))