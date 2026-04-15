# Multi-view Python UI App using Tkinter
# Folder structure suggestion:
# /app
#   main.py
#   db.py
#   views/
#       login.py
#       matrix.py
#       rotate_square.py
#       rotate_cube.py
#       rockets.py

import tkinter as tk

from matplotlib.pylab import square
from views.login import LoginView
from views.matrix import MatrixView
from views.rotate_square import RotateSquareView
from views.rotate_cube import RotateCubeView
from views.rockets import RocketsView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi App")
        self.geometry("400x300")

        from views.login import LoginView
        frame = LoginView(self, self)
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
