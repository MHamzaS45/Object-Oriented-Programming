import tkinter as tk
import numpy as np

class MatrixView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Matrix Calculator").pack()

        self.a = tk.Entry(self)
        self.b = tk.Entry(self)
        self.a.pack()
        self.b.pack()

        tk.Button(self, text="Add", command=self.add).pack()
        tk.Button(self, text="Subtract", command=self.sub).pack()
        tk.Button(self, text="Multiply", command=self.mul).pack()
        tk.Button(self, text="Back to Login", command=lambda: controller.show_frame("LoginView")).pack()
        tk.Button(self, text="Go to Rotate Square", command=lambda: controller.show_frame("RotateSquareView")).pack()

        self.result = tk.Label(self, text="")
        self.result.pack()

    def parse(self, text):
        return np.array(eval(text))

    def add(self):
        self.result.config(text=str(self.parse(self.a.get()) + self.parse(self.b.get())))

    def sub(self):
        self.result.config(text=str(self.parse(self.a.get()) - self.parse(self.b.get())))

    def mul(self):
        self.result.config(text=str(self.parse(self.a.get()) @ self.parse(self.b.get())))