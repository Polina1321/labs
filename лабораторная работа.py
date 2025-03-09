import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
#Постановка задачи: использовать метод k ближайших соседей для реализации классификации точек в двумерном пространстве

def generate_points(num_points, x_range, y_range, category):
    points = [[random.uniform(x_range[0], x_range[1]), random.uniform(y_range[0], y_range[1])] for _ in range(num_points)]
    categories = [category] * num_points
    return points, categories

def split_data(x, y, train_ratio=0.8):
    data = list(zip(x, y))
    random.shuffle(data)
    split_index = int(len(data) * train_ratio)
    train_data, test_data = data[:split_index], data[split_index:]
    return list(zip(*train_data)), list(zip(*test_data))

def distance(point1, point2):
    return (((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5)

def knn_predict(x_train, y_train, x_test, k=3):
    predictions = []
    for test_point in x_test:
        neighbors = sorted(zip(x_train, y_train), key=lambda train_point: distance(test_point, train_point[0]))[:k]
        predicted_class = Counter(y for _, y in neighbors).most_common(1)[0][0]
        predictions.append(predicted_class)
    return predictions

x0,y0 = generate_points(50, (0, 2), (0, 2), 0)
x1,y1 = generate_points(50, (7, 12), (7, 12), 1)

x = x0 + x1
y = y0 + y1

(x_train, y_train), (x_test, y_test) = split_data(x, y)

k = 3
pr = knn_predict(x_train, y_train, x_test, k)
colors = ['blue', 'red']

for l in set(y_train):
    train_points = [x for x, y in zip(x_train, y_train) if y == l]
    plt.scatter(*zip(*train_points), color=colors[l], label=f"Class {l} (train)", alpha=0.6)

for i, point in enumerate(x_test):
    plt.scatter(*point, color=colors[pr[i]], edgecolors='black', marker="x", s=100)

plt.legend()
plt.xlabel('X')
plt.ylabel("Y")
plt.show()
