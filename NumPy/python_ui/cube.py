import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ---------------- CUBE DATA ----------------
size = 1
cube_points = np.array([
    [-size/2,  size/2,  size/2],
    [ size/2,  size/2,  size/2],
    [ size/2, -size/2,  size/2],
    [-size/2, -size/2,  size/2],
    [-size/2,  size/2, -size/2],
    [ size/2,  size/2, -size/2],
    [ size/2, -size/2, -size/2],
    [-size/2, -size/2, -size/2]
])

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

# ---------------- ROTATION FUNCTION ----------------
def rotate(points, ax, ay, az):
    Rx = np.array([
        [1,0,0],
        [0,np.cos(ax),-np.sin(ax)],
        [0,np.sin(ax), np.cos(ax)]
    ])
    Ry = np.array([
        [np.cos(ay),0,np.sin(ay)],
        [0,1,0],
        [-np.sin(ay),0,np.cos(ay)]
    ])
    Rz = np.array([
        [np.cos(az), -np.sin(az),0],
        [np.sin(az), np.cos(az),0],
        [0,0,1]
    ])
    R = Rx @ Ry @ Rz
    return points @ R.T

# ---------------- PLOT ----------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.1, bottom=0.3)

# initial rotation
rot_points = rotate(cube_points, 0, 0, 0)

# plot lines
lines = []
for e in edges:
    line, = ax.plot([rot_points[e[0],0], rot_points[e[1],0]],
                    [rot_points[e[0],1], rot_points[e[1],1]],
                    [rot_points[e[0],2], rot_points[e[1],2]], color='b')
    lines.append(line)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])

# ---------------- SLIDERS ----------------
axcolor = 'lightgoldenrodyellow'
axX = plt.axes([0.1, 0.2, 0.8, 0.03], facecolor=axcolor)
axY = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)
axZ = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor=axcolor)

sX = Slider(axX, 'X', 0, 360, valinit=0)
sY = Slider(axY, 'Y', 0, 360, valinit=0)
sZ = Slider(axZ, 'Z', 0, 360, valinit=0)

def update(val):
    ax.clear()
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])
    rx = np.radians(sX.val)
    ry = np.radians(sY.val)
    rz = np.radians(sZ.val)
    rot = rotate(cube_points, rx, ry, rz)
    for e in edges:
        ax.plot([rot[e[0],0], rot[e[1],0]],
                [rot[e[0],1], rot[e[1],1]],
                [rot[e[0],2], rot[e[1],2]], color='b')
    fig.canvas.draw_idle()

sX.on_changed(update)
sY.on_changed(update)
sZ.on_changed(update)

plt.show()