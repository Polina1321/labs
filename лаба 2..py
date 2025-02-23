#2.	Напишите программу построения графика по имеющемуся дискретному набору известных значений.
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def read_dan(a):
    with open(a, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    x = [float(num) for num in lines[0].strip().split(',')]
    y = [float(num) for num in lines[1].strip().split(',')]
    return x, y


def graphic_func():
    x, y = read_dan('C:/Users/Mi/Desktop/лаба 2..txt')

    ax.clear()
    ax.plot(x, y, marker='o', linestyle='-', color='b')
    ax.grid()
    canvas.draw()


root = tk.Tk()

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

graphic_func()
root.mainloop()