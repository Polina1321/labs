#Постановка задачи: использовать метод k ближайших соседей для реализации классификации точек в двумерном пространстве
import random
import math
import matplotlib.pyplot as plt

X = []
Y = []

for j in range(50):
    X.append([random.uniform(1, 10), random.uniform(1, 10)])
    Y.append(0)

for j in range(50):
    X.append([random.uniform(5, 15), random.uniform(5, 15)])
    Y.append(1)


def s(X, Y, p):
    TX = []
    TY = []
    TXt = []
    TYt = []

    z = list(range(len(X)))
    random.shuffle(z)

    train_size = int(len(X) * p)

    for l in range(train_size):
        TX.append(X[z[l]])
        TY.append(Y[z[l]])

    for l in range(train_size, len(X)):
        TXt.append(X[z[l]])
        TYt.append(Y[z[l]])

    return TX, TY, TXt, TYt


def c(TX, TY, TXt, k=3):
    res = []

    for u in range(len(TXt)):
        d = []

        for v in range(len(TX)):
            d.append((math.sqrt((TXt[u][0] - TX[v][0]) ** 2 + (TXt[u][1] - TX[v][1]) ** 2), TY[v]))

        d.sort(key=lambda x: x[0])

        V = {}
        for f in range(k):
            if d[f][1] in V:
                V[d[f][1]] += 1
            else:
                V[d[f][1]] = 1

        Cl = max(V, key=V.get)

        res.append(Cl)

    return res


def A(TYt, res):
    a = 0
    for i in range(len(TYt)):
        if TYt[i] == res[i]:
            a += 1
    return a / len(TYt)


TX, TY, TXt, TYt = s(X, Y, 0.8)
res = c(TX, TY, TXt)
acc = A(TYt, res)

print("Предсказанные классы:", res)
print("Истинные классы:", TYt)
print("Точность (accuracy):", acc)

plt.figure(figsize=(10, 6))

for i in range(len(TX)):
    if TY[i] == 0:
        plt.scatter(TX[i][0], TX[i][1], color='blue', marker='o')
    else:
        plt.scatter(TX[i][0], TX[i][1], color='blue', marker='x')

for i in range(len(TXt)):
    if TYt[i] == res[i]:
        if TYt[i] == 0:
            plt.scatter(TXt[i][0], TXt[i][1], color='green', marker='o')
        else:
            plt.scatter(TXt[i][0], TXt[i][1], color='green', marker='x')
    else:
        if TYt[i] == 0:
            plt.scatter(TXt[i][0], TXt[i][1], color='red', marker='o')
        else:
            plt.scatter(TXt[i][0], TXt[i][1], color='red', marker='x')

plt.xlabel("Trait 1")
plt.ylabel("Trait 2")
plt.title("KNN Classification")
plt.grid()
plt.show()
