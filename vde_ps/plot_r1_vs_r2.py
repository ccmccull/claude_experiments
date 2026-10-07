"""Plot R_1 vs. R_2 for a loaded voltage divider:

    R_2 * (V_in - V_out) = R_1 * (V_out + R_2 * i_3)

Solving for R_1:

    R_1 = R_2 * (V_in - V_out) / (V_out + R_2 * i_3)

As R_2 -> infinity, R_1 approaches (V_in - V_out) / i_3.

Two operating conditions are plotted. Each is a curve of (R_2, R_1) pairs that
satisfy it; the single divider that satisfies both is where they cross.
"""

import matplotlib.pyplot as plt
import numpy as np

V_in = 12.0  # V

# Operating conditions: (V_out [V], i_3 [A])
condition_a = (5.0, 0.05)
condition_b = (4.9, 0.055)


def r1_from_r2(r2, v_out, i_3):
    return r2 * (V_in - v_out) / (v_out + r2 * i_3)


def crossing(cond_1, cond_2):
    """Non-zero R_2 where both conditions give the same R_1.

    Setting the two R_1 expressions equal and cancelling R_2 leaves
    (V_in - v1) * (v2 + R_2 i2) = (V_in - v2) * (v1 + R_2 i1), linear in R_2.
    """
    (v1, i1), (v2, i2) = cond_1, cond_2
    d1, d2 = V_in - v1, V_in - v2
    r2 = (d2 * v1 - d1 * v2) / (d1 * i2 - d2 * i1)
    return r2, r1_from_r2(r2, v1, i1)


# Symbols rendered with real subscripts (matplotlib mathtext)
R1, R2 = r"$R_1$", r"$R_2$"
VIN, VOUT, I3 = r"$V_\mathrm{in}$", r"$V_\mathrm{out}$", r"$i_3$"

CURVES = ((condition_a, "#2a6fdb"), (condition_b, "#e07b24"))

r2_x, r1_x = crossing(condition_a, condition_b)
zoom_lo, zoom_hi = 38.0, 42.0  # Ω, R_2 range of the right panel

fig, (ax_full, ax_zoom) = plt.subplots(1, 2, figsize=(12, 5))


def style(ax):
    ax.grid(True, which="major", color="#e6e6e6", linewidth=0.6)
    ax.grid(True, which="minor", color="#f3f3f3", linewidth=0.4)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.set_ylabel(f"{R1} (Ω)")


def mark_design_point(ax, xytext):
    ax.plot(r2_x, r1_x, "o", markersize=8, color="#222222",
            markeredgecolor="white", markeredgewidth=2, zorder=5)
    ax.annotate(
        f"design point\n{R2} = {r2_x:.2f} Ω\n{R1} = {r1_x:.2f} Ω",
        xy=(r2_x, r1_x), xytext=xytext, textcoords="offset points",
        ha="center", va="bottom", fontsize=9,
        arrowprops=dict(arrowstyle="-", color="#555555", linewidth=0.8),
    )


# Left panel: full curves
R_2 = np.linspace(0, 200, 1001)  # Ω
for (v_out, i_3), color in CURVES:
    label = f"{VOUT} = {v_out:g} V at {I3} = {i_3:g} A"
    ax_full.plot(R_2, r1_from_r2(R_2, v_out, i_3), color=color,
                 linewidth=2, label=label)

ax_full.axvspan(zoom_lo, zoom_hi, color="#888888", alpha=0.12, linewidth=0)
mark_design_point(ax_full, (70, -10))
ax_full.set_xlim(R_2[0], R_2[-1])
ax_full.set_ylim(bottom=0)
ax_full.set_xlabel(f"{R2} (Ω)")
ax_full.legend(loc="lower right", frameon=False)
style(ax_full)

# Right panel: linear zoom around the design point
r2_zoom = np.linspace(zoom_lo, zoom_hi, 400)
for (v_out, i_3), color in CURVES:
    ax_zoom.plot(r2_zoom, r1_from_r2(r2_zoom, v_out, i_3), color=color, linewidth=2)
mark_design_point(ax_zoom, (-40, 30))
ax_zoom.set_xlim(zoom_lo, zoom_hi)
ax_zoom.set_xlabel(f"{R2} (Ω)")
style(ax_zoom)

fig.suptitle(f"{R1} vs. {R2} for a loaded divider ({VIN} = {V_in:g} V)")


fig.tight_layout()
fig.savefig("r1_vs_r2.png", dpi=150)
plt.show()
