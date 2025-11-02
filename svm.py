import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv('emails.csv')
x = df.drop(columns=['Email No.', 'Prediction'])
y = df['Prediction']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearSVC(max_iter=5000)
model.fit(xTrain, yTrain)
yPred = model.predict(xTest)

# ... (rest of your code is correct) ...

print("\nAccuracy:", accuracy_score(yTest, yPred))
print("\nConfusion Matrix:\n", confusion_matrix(yTest, yPred))
print("\nClassification Report:\n", classification_report(yTest, yPred))
