import numpy as np
import matplotlib.pyplot as plt


def gradient_descent(func, diff_func, x0=3.0, learning_rate=0.01, epochs=100):
    x_list = []
    y_list = []
    x = x0

    for _ in range(epochs):
        x_list.append(x)
        y_list.append(func(x))
        x = x - learning_rate * diff_func(x)

    return x_list, y_list



def f(x):
    return np.exp(-x**2 / 10) * (np.sin(2 * x) + 0.1 * x**2)


def df(x):
    term1 = np.exp(-x ** 2 / 10) * (2 * np.cos(2 * x) + 0.2 * x)
    term2 = (x / 5) * np.exp(-x**2 / 10) * (np.sin(2 * x) + 0.1 * x**2)
    return term1 - term2



x0 = 3.0
learning_rate = 0.05
epochs = 100
x_list, y_list = gradient_descent(f, df, x0, learning_rate, epochs)


x_vals = np.linspace(-5, 5, 500)
y_vals = f(x_vals)

plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals, label=r'$f(x) = e^{-x^2/10} \cdot (\sin(2x) + 0.1x^2)$', color='blue')
plt.scatter(x_list, y_list, color='red', label='Точки градиентного спуска')
plt.plot(x_list, y_list, '--', color='orange', alpha=0.5, label='Траектория')
plt.scatter([x_list[0]], [y_list[0]], color='green', s=100, label='Старт ($x_0$=3)')
plt.scatter([x_list[-1]], [y_list[-1]], color='black', s=100, label=f'Финал (x≈{x_list[-1]:.2f})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Градиентный спуск на сложной функции')
plt.legend()
plt.grid(True)
plt.show()

def find_critical_speed(func, diff_func, x0=3.0, epochs=100, target_min=-1.5, tol=0.1):
    low, high = 0.0, 1.0
    for _ in range(20):
        mid = (low + high) / 2
        x_list, _ = gradient_descent(func, diff_func, x0, mid, epochs)
        if abs(x_list[-1] - target_min) < tol:
            high = mid
        else:
            low = mid
    return (low + high) / 2

critical_speed = find_critical_speed(f, df)
print(f"Граничное значение learning_rate: {critical_speed:.4f}")


print(f"Найденный минимум: x = {x_list[-1]:.4f}, f(x) = {y_list[-1]:.4f}")
