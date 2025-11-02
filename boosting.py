import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
x = iris.data
y = iris.target

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42)

models = {
    'AdaBoost': AdaBoostClassifier(n_estimators=100, random_state=42),
    'GradientBoost': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'XGBoost': XGBClassifier(n_estimators=100, random_state=42)
}


for name, model in models.items():
    model.fit(xTrain, yTrain)
    yPred = model.predict(xTest)
    print(f"\n\n-------------------------- {name} --------------------------")
    print("\nAccuracy: ", accuracy_score(yPred, yTest))
    print("\nConfusion Matrix: \n", confusion_matrix(yPred, yTest))
    print("\nClassification: Report: ", classification_report(yPred, yTest))
