#Постановка задачи: реализовать регрессию на python с использованием библиотеки matplotlib
#Вариант 13, степенная функция
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.metrics import mean_squared_error

# 1. Генерация исходных данных
np.random.seed(42)
x_min, x_max, points = 1, 10, 50
x = np.linspace(x_min, x_max, points)

# Истинные параметры (произвольно заданные)
a_true, b_true, c_true = 2.5, 1.8, 3.0
y_true = a_true * x ** b_true + c_true

# Добавление шума
noise = np.random.uniform(-3, 3, size=points)
y = y_true + noise


# 2. Функции для вычисления MSE и частных производных
def power_function(x, a, b, c):
    return a * x ** b + c


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def get_da(x, y, a, b, c):
    y_pred = power_function(x, a, b, c)
    return -2 / len(x) * np.sum((y - y_pred) * x ** b)


def get_db(x, y, a, b, c):
    y_pred = power_function(x, a, b, c)
    return -2 / len(x) * np.sum((y - y_pred) * a * x ** b * np.log(x))


def get_dc(x, y, a, b, c):
    y_pred = power_function(x, a, b, c)
    return -2 / len(x) * np.sum(y - y_pred)


# 3. Градиентный спуск
def fit(x, y, learning_rate=0.0001, epochs=1000):
    # Инициализация параметров
    a = np.random.rand()
    b = np.random.rand()
    c = np.random.rand()

    a_history = [a]
    b_history = [b]
    c_history = [c]
    mse_history = [mse(y, power_function(x, a, b, c))]

    for _ in range(epochs):
        # Вычисление градиентов
        da = get_da(x, y, a, b, c)
        db = get_db(x, y, a, b, c)
        dc = get_dc(x, y, a, b, c)

        # Обновление параметров
        a -= learning_rate * da
        b -= learning_rate * db
        c -= learning_rate * dc

        # Сохранение истории
        a_history.append(a)
        b_history.append(b)
        c_history.append(c)
        mse_history.append(mse(y, power_function(x, a, b, c)))

    return a_history, b_history, c_history, mse_history


# Параметры обучения
learning_rate = 0.0001
epochs = 1000
a_history, b_history, c_history, mse_history = fit(x, y, learning_rate, epochs)

# 4. Визуализация с ползунком
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)

# График данных и регрессии
scatter = ax1.scatter(x, y, color='blue', label='Исходные данные')
line, = ax1.plot(x, power_function(x, a_history[0], b_history[0], c_history[0]),
                 'r-', linewidth=2, label='Регрессия')
ax1.plot(x, y_true, 'g--', label='Истинная функция')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Степенная регрессия: y = axᵇ + c')
ax1.legend()
ax1.grid(True)

# График MSE
mse_line, = ax2.plot(range(len(mse_history)), mse_history, 'b-')
ax2.set_xlabel('Эпоха')
ax2.set_ylabel('MSE')
ax2.set_title('Изменение MSE в процессе обучения')
ax2.grid(True)

# Создание ползунка
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Эпоха', 0, epochs, valinit=0, valstep=1)


# Функция обновления графика
def update(val):
    epoch = int(slider.val)
    a = a_history[epoch]
    b = b_history[epoch]
    c = c_history[epoch]

    line.set_ydata(power_function(x, a, b, c))
    ax1.set_title(f'Степенная регрессия: y = {a:.2f}x^{b:.2f} + {c:.2f} (эпоха {epoch})')

    mse_line.set_data(range(epoch + 1), mse_history[:epoch + 1])
    ax2.set_xlim(0, epoch + 1)
    ax2.set_ylim(0, max(mse_history[:epoch + 1]) * 1.1)

    fig.canvas.draw_idle()


slider.on_changed(update)

plt.show()

# Вывод финальных параметров
final_a = a_history[-1]
final_b = b_history[-1]
final_c = c_history[-1]
final_mse = mse_history[-1]

print(f"Финальные параметры: a = {final_a:.4f}, b = {final_b:.4f}, c = {final_c:.4f}")
print(f"Финальное MSE: {final_mse:.4f}")
print(f"Истинные параметры: a = {a_true}, b = {b_true}, c = {c_true}")
