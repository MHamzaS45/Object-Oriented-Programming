import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import cm

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
 
# Create the supa cool grid
theta = np.linspace(0, 2*np.pi, 200)
w = np.linspace(-0.5, 0.5, 50)
theta, w = np.meshgrid(theta, w)

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

def update(frame):
    ax.clear()

    # Animating the twist of the Möbius strip
    twist = np.sin(frame * 0.1)

    r = 1 + w * np.cos(theta / 2 + twist)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = w * np.sin(theta / 2 + twist)

    # Color based on height
    norm = (z - z.min()) / (z.max() - z.min())
    colors = cm.viridis(norm)

    ax.plot_surface(x, y, z, facecolors=colors, rstride=1, cstride=1,
                    linewidth=0, antialiased=True, shade=True)

    # Rotate view
    ax.view_init(elev=30, azim=frame)

    # Clean look
    ax.set_axis_off()
    ax.set_title(" Möbius Strip JOJO PART 6 -- Hamza", fontsize=14)

ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False, vmin = -10, vmax = 10)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()