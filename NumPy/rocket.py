import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import pygame

# =============================
# MUSIC SETUP
# =============================
pygame.mixer.init()
pygame.mixer.music.load("NumPy\\python_ui\\music.mp3")  # <-- put your mp3 file here
pygame.mixer.music.play(-1)


# -----------------------------
# INITIAL SETUP
# -----------------------------
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title("Rocket Launch Simulation")

# Rocket starting positions
rocket1 = np.array([20, 10])
rocket2 = np.array([80, 15])

# Moon position
moon = np.array([50, 90])

# Scatter plot objects
rocket1_plot = ax.scatter([], [], color='red', label="Ernest's Rocket")
rocket2_plot = ax.scatter([], [], color='green', label="Kernest's Rocket")
moon_plot = ax.scatter(moon[0], moon[1], color='grey', s=200, label="Moon")

ax.legend()

# -----------------------------
# COUNTDOWN
# -----------------------------
for i in range(3, 0, -1):
    print(f"Launching in {i}...")
    time.sleep(1)
print("LAUNCH!")

# -----------------------------
# MOVEMENT FUNCTION
def move_towards(start, target, speed=0.5):
    direction = target - start
    distance = np.linalg.norm(direction)
    if distance < 1:
        return start
    return start + (direction / distance) * speed


# ANIMATION UPDATE
# -----------------------------
def update(frame):
    global rocket1, rocket2

    # Move rockets
    rocket1 = move_towards(rocket1, moon)
    rocket2 = move_towards(rocket2, moon)

    # Update plot
    rocket1_plot.set_offsets(rocket1)
    rocket2_plot.set_offsets(rocket2)

    # Collision check (rockets)
    if np.linalg.norm(rocket1 - rocket2) < 2:
        ax.set_title(f" ROCKET COLLISION! Mission failed.")
        ani.event_source.stop()

    # Rocket hits moon
    if np.linalg.norm(rocket1 - moon) < 1:
        ax.set_title(f"Ernest's Rocket reached the moon!")
        ani.event_source.stop()
        

    if np.linalg.norm(rocket2 - moon) < 1:
        ax.set_title(f"Kernest's Rocket reached the moon!")
        ani.event_source.stop()

    return rocket1_plot, rocket2_plot

# -----------------------------
# RUN ANIMATION
# -----------------------------
ani = animation.FuncAnimation(fig, update, interval=50)
plt.show()