#Метод k средних
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.cluster import KMeans


circles = [[[2, 6], 1.5],[[5, 2], 1.2],[[8, 7], 1.0]]


points = []
for (x, y), r in circles:
    for _ in range(35):
        corner = np.random.uniform(0, 2 * np.pi)
        radius = r * np.sqrt(np.random.uniform(0, 1))
        points.append([x + radius * np.cos(corner), y + radius * np.sin(corner)])

X = np.array(points)
def run_kmeans(X, n_clusters=3, max_iter=100):
    history = []


    kmeans = KMeans(n_clusters=n_clusters, init='random', max_iter=1, n_init=1)
    kmeans.fit(X)
    history.append((kmeans.cluster_centers_.copy(), kmeans.labels_.copy()))


    for _ in range(max_iter):
        prev_labels = kmeans.labels_.copy()
        kmeans.max_iter += 1
        kmeans.fit(X)
        history.append((kmeans.cluster_centers_.copy(), kmeans.labels_.copy()))
        if np.array_equal(prev_labels, kmeans.labels_):
            break

    return history


history = run_kmeans(X, n_clusters=3, max_iter=100)


fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.25)


scatter = ax.scatter(X[:, 0], X[:, 1], c=history[0][1], cmap='rainbow')
centers_scatter = ax.scatter(history[0][0][:, 0], history[0][0][:, 1],
                             c='black', marker='X', s=100)


ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Итерация', 0, len(history) - 1, valinit=0, valfmt='%d')



def update(val):
    iteration = int(slider.val)
    centers, labels = history[iteration]
    scatter.set_array(labels)
    centers_scatter.set_offsets(centers)
    fig.canvas.draw_idle()


slider.on_changed(update)

plt.title(f'K-means кластеризация')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
