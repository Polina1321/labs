#1.	Напишите программу, строящую график функции. Коэффициенты a,b,c и диапазон задаются с клавиатуры.
# Проведите проверку решения задачи в Excel.

import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def graphic_func():
    a = 8
    b = 4
    x = np.linspace(-10, 10, 100)
    y = a * (x**2) + b
    ax.clear()
    ax.plot(x, y)
    ax.grid()
    canvas.draw()

root = tk.Tk()


fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

graphic_func()
root.mainloop()