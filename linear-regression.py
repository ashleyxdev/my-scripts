import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

x = df[['bmi']]
y = df['target']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(xTrain, yTrain)
yPred = model.predict(xTest)

mse = mean_squared_error(yTest, yPred)
r2 = r2_score(yTest, yPred)

print('Mean Squared Error: ', mse)
print(r2)
print(model.coef_)
print(model.intercept_)

plt.scatter(x, y, label='Actual Data')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.xlabel('BMI')
plt.ylabel('Target')
plt.legend()
plt.show()
