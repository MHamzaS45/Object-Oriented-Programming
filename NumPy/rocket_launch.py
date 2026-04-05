import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pygame

# =============================
# MUSIC
# =============================
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# =============================
# CONSTANTS (FROM PROJECT 1)
# =============================
G = 6.674e-11
M_earth = 5.972e24
M_moon = 7.347e22

R_earth = 6.371e6
R_moon = 1.737e6
moon_distance = 384400e3

dt = 2
moon_ang_vel = 2.66e-6

# =============================
# ROCKET CLASS (PHYSICS)
# =============================
class Rocket:
    def __init__(self, pos, vel, color, name):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.color = color
        self.name = name
        self.alive = True

    def gravity(self, moon_pos):
        r = np.linalg.norm(self.pos)
        gE = -G * M_earth * self.pos / r**3

        r_vec_m = moon_pos - self.pos
        rM = np.linalg.norm(r_vec_m)
        gM = G * M_moon * r_vec_m / rM**3

        return gE + gM

    def update(self, moon_pos):
        if not self.alive:
            return
        a = self.gravity(moon_pos)
        self.vel += a * dt
        self.pos += self.vel * dt

# =============================
# INITIAL CONDITIONS
# =============================
r0 = R_earth + 200e3
v0 = np.sqrt(G * M_earth / r0)

rocket1 = Rocket([r0, 0], [0, v0], 'red', "Ernest")
rocket2 = Rocket([r0, 1000], [0, v0*1.02], 'green', "Kernest")

rockets = [rocket1, rocket2]

# =============================
# COUNTDOWN
# =============================
for i in range(3, 0, -1):
    print(f"🚀 Launch in {i}...")
    time.sleep(1)
print("🔥 LAUNCH!\n")

# =============================
# PLOT SETUP
# =============================
fig, ax = plt.subplots(figsize=(8,8))

earth = plt.Circle((0,0), R_earth, color='blue')
moon_circle = plt.Circle((0,0), R_moon, color='gray')

ax.add_patch(earth)
ax.add_patch(moon_circle)

r1_plot, = ax.plot([], [], 'ro', label="Ernest")
r2_plot, = ax.plot([], [], 'go', label="Kernest")

trail1, = ax.plot([], [], 'r-', lw=1)
trail2, = ax.plot([], [], 'g-', lw=1)

ax.legend()

ax.set_xlim(-4e8, 4e8)
ax.set_ylim(-4e8, 4e8)
ax.set_aspect('equal')

traj1, traj2 = [], []

# =============================
# UPDATE FUNCTION
# =============================
def update(frame):
    time_sim = frame * dt

    # Moon motion
    theta = moon_ang_vel * time_sim
    moon_pos = np.array([
        moon_distance * np.cos(theta),
        moon_distance * np.sin(theta)
    ])

    moon_circle.center = moon_pos

    # Update rockets
    for r in rockets:
        r.update(moon_pos)

    # =============================
    # COLLISION PREVENTION (IMPROVED)
    # =============================
    dist = np.linalg.norm(rocket1.pos - rocket2.pos)
    if dist < 5000:
        direction = rocket1.pos - rocket2.pos
        direction = direction / np.linalg.norm(direction)
        rocket1.vel += direction * 20
        rocket2.vel -= direction * 20

    # =============================
    # MOON HIT DETECTION (UI STYLE)
    # =============================
    for r in rockets:
        if r.alive:
            if np.linalg.norm(r.pos - moon_pos) < R_moon:
                r.alive = False
                ax.set_title(f"🌕 {r.name}'s Rocket reached the Moon!")
                print(f"🌕 {r.name}'s Rocket reached the Moon!")

    # Store trajectory
    traj1.append(rocket1.pos.copy())
    traj2.append(rocket2.pos.copy())

    # Update visuals
    r1_plot.set_data(rocket1.pos[0], rocket1.pos[1])
    r2_plot.set_data(rocket2.pos[0], rocket2.pos[1])

    trail1.set_data([p[0] for p in traj1], [p[1] for p in traj1])
    trail2.set_data([p[0] for p in traj2], [p[1] for p in traj2])

    return r1_plot, r2_plot, trail1, trail2, moon_circle

# =============================
# ANIMATION (FIXED)
# =============================
ani = animation.FuncAnimation(
    fig,
    update,
    frames=10000,
    interval=30,
    blit=False
)

plt.title("🚀 Two Rockets Mission to the Moon 🌕")
plt.tight_layout()
plt.show()