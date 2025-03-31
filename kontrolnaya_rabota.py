#Метод k средних
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.cluster import KMeans


def generate_circle_data(centers, radii, points_per_cluster=20):
    data = []
    for i, (center, radius) in enumerate(zip(centers, radii)):
        for _ in range(points_per_cluster):
            r = radius * np.sqrt(np.random.random())
            angle = 2 * np.pi * np.random.random()
            x = center[0] + r * np.cos(angle)
            y = center[1] + r * np.sin(angle)
            data.append([x, y])
    return np.array(data)


centers = np.array([[2, 3], [8, 10], [5, 15]])
radii = np.array([1.5, 2.0, 2.5])
data = generate_circle_data(centers, radii, points_per_cluster=30)


def kmeans_with_history(X, k=3, max_iter=100, tol=1e-4):
    kmeans = KMeans(n_clusters=k, init='random', max_iter=1, n_init=1, tol=tol)

    history = {'centers': [], 'labels': []}

    for _ in range(max_iter):
        kmeans.fit(X)
        history['centers'].append(kmeans.cluster_centers_.copy())
        history['labels'].append(kmeans.labels_.copy())

        if len(history['centers']) > 1:
            prev_centers = np.array(history['centers'][-2])
            curr_centers = np.array(history['centers'][-1])
            if np.all(np.abs(prev_centers - curr_centers) < tol):
                break

    return history


history = kmeans_with_history(data, k=3, max_iter=100)

fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.25)

scatter = ax.scatter(data[:, 0], data[:, 1], c=history['labels'][0], cmap='viridis')
centers_plot = ax.scatter(history['centers'][0][:, 0], history['centers'][0][:, 1],
                          c='red', marker='X', s=200, label='Центроиды')
ax.set_title('K-means кластеризация (Итерация 0)')
ax.set_xlabel('X координата')
ax.set_ylabel('Y координата')
ax.legend()
ax.grid(True)

ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Итерация', 0, len(history['labels']) - 1, valinit=0, valstep=1)

def update(val):
    iteration = int(slider.val)
    scatter.set_array(history['labels'][iteration])
    centers_plot.set_offsets(history['centers'][iteration])
    ax.set_title(f'K-means кластеризация (Итерация {iteration})')
    fig.canvas.draw_idle()


slider.on_changed(update)

plt.show()