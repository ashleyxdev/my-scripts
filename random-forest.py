import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('car_evaluation.csv')
print('Dataset Shape: ', df.shape)
print(df.head())

le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

print("Encoded Dataset:\n", df.head())

x = df.drop('unacc', axis=1)
y = df['unacc']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(xTrain, yTrain)
yPred = model.predict(xTest)

print('\nAccuracy: ', accuracy_score(yPred, yTest))
print('\nConfusion Matrix: \n', confusion_matrix(yPred, yTest))
print('\nClassification Report: ', classification_report(yPred, yTest))
