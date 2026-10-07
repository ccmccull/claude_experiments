"""Plot the linear relationship y = 2x for x in [-1, 1]."""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 201)
y = 2 * x

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, color="#2a6fdb", linewidth=2)

# Recessive reference lines through the origin
ax.axhline(0, color="#b0b0b0", linewidth=0.8, zorder=0)
ax.axvline(0, color="#b0b0b0", linewidth=0.8, zorder=0)
ax.grid(True, color="#e6e6e6", linewidth=0.6)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)

ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y = 2x, for -1 ≤ x ≤ 1")

fig.tight_layout()
fig.savefig("linear_y_equals_2x.png", dpi=150)
plt.show()
