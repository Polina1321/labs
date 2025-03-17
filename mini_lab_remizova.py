import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("датасет-1.csv",sep=';')
print(data.head())
print(data.dtypes)

data["price"] = data["price"].astype(str).str.replace(",", ".").astype(float)

plt.scatter(data["area"], data["price"], color="green")
plt.xlabel("Площадь (кв.м.)")
plt.ylabel("Цена (млн руб.)")
plt.title("Связь между площадью и ценой")
plt.show()

model = LinearRegression()
model.fit(data[['area']], data['price'])

print("Коэффициент наклона (a):", model.coef_[0])
print("Свободный член (b):", model.intercept_)

predicted_price_38 = model.predict([[38]])
predicted_price_200 = model.predict([[200]])

print("Прогнозируемая цена для 38 м²:", predicted_price_38[0])
print("Прогнозируемая цена для 200 м²:", predicted_price_200[0])

data["predicted_price"] = model.predict(data[['area']])
print(data.head())

plt.scatter(data["area"], data["price"], color="green", label="Реальные значения")
plt.plot(data["area"], model.predict(data[['area']]), color="orange", label="Линия регрессии")
plt.xlabel("Площадь (кв.м.)")
plt.ylabel("Цена (млн руб.)")
plt.legend()
plt.show()

prediction_data = pd.read_csv("prediction_price.csv", sep=";")
prediction_data["area"] = prediction_data["area"].astype(float)

predictions = model.predict(prediction_data[['area']])
prediction_data["predicted_price"] = predictions
print(prediction_data.head())

prediction_data.to_excel("new_predictions.xlsx", index=False)
print("Результаты сохранены в файл new_predictions.xlsx")