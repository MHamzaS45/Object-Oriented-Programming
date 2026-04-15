import tkinter as tk
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class RotateCubeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.plot()

    def rotate(self, points, ax, ay, az):
        Rx = np.array([[1,0,0],[0,np.cos(ax),-np.sin(ax)],[0,np.sin(ax), np.cos(ax)]])
        Ry = np.array([[np.cos(ay),0,np.sin(ay)],[0,1,0],[-np.sin(ay),0,np.cos(ay)]])
        Rz = np.array([[np.cos(az), -np.sin(az),0],[np.sin(az), np.cos(az),0],[0,0,1]])
        R = Rx @ Ry @ Rz
        return points @ R.T

    def plot(self):
        size = 1
        cube_points = np.array([
            [-size/2,size/2,size/2],[size/2,size/2,size/2],[size/2,-size/2,size/2],[-size/2,-size/2,size/2],
            [-size/2,size/2,-size/2],[size/2,size/2,-size/2],[size/2,-size/2,-size/2],[-size/2,-size/2,-size/2]
        ])
        edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        plt.subplots_adjust(left=0.1, bottom=0.3)

        def update(val):
            ax.clear()
            ax.set_xlim([-1,1]); ax.set_ylim([-1,1]); ax.set_zlim([-1,1])
            rx, ry, rz = np.radians(sX.val), np.radians(sY.val), np.radians(sZ.val)
            rot = self.rotate(cube_points, rx, ry, rz)
            for e in edges:
                ax.plot([rot[e[0],0], rot[e[1],0]],
                        [rot[e[0],1], rot[e[1],1]],
                        [rot[e[0],2], rot[e[1],2]], color='b')
            fig.canvas.draw_idle()

        axcolor = 'lightgoldenrodyellow'
        sX = Slider(plt.axes([0.1,0.2,0.8,0.03], facecolor=axcolor),'X',0,360,valinit=0)
        sY = Slider(plt.axes([0.1,0.15,0.8,0.03], facecolor=axcolor),'Y',0,360,valinit=0)
        sZ = Slider(plt.axes([0.1,0.1,0.8,0.03], facecolor=axcolor),'Z',0,360,valinit=0)

        sX.on_changed(update); sY.on_changed(update); sZ.on_changed(update)
        plt.show()