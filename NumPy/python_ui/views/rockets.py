import tkinter as tk
import random

import pygame
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import pygame


class RocketsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.run()

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Data-Pipelines\\NumPy\\python_ui\\music.mp3")
        pygame.mixer.music.play(-1)

        fig, ax = plt.subplots()
        ax.set_xlim(0,100); ax.set_ylim(0,100)

        rocket1 = np.array([20,10])
        rocket2 = np.array([80,15])
        moon = np.array([50,90])

        r1 = ax.scatter([],[],color='red')
        r2 = ax.scatter([],[],color='green')
        ax.scatter(moon[0],moon[1],color='grey',s=200)

        def move(start,target,speed=0.5):
            d = target-start
            dist = np.linalg.norm(d)
            if dist<1: return start
            return start + (d/dist)*speed

        def update(frame):
            nonlocal rocket1, rocket2
            rocket1 = move(rocket1, moon)
            rocket2 = move(rocket2, moon)

            if np.linalg.norm(rocket1-rocket2)<2:
                rocket2[0]+=2

            r1.set_offsets(rocket1)
            r2.set_offsets(rocket2)

            if np.linalg.norm(rocket1-moon)<1 or np.linalg.norm(rocket2-moon)<1:
                ax.set_title("Rocket reached the moon!")
                ani.event_source.stop()

            return r1, r2

        ani = animation.FuncAnimation(fig, update, interval=50)
        plt.show()