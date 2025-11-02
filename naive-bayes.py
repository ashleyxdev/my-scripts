import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('spam.csv', encoding='latin-1')

df = df[['v1', 'v2']]    # dataset has extra unnamed columns; keep only label+message
df.columns = ['label', 'message']    # rename columns to meaningful names
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})    # convert text labels to numeric labels coz sklean expects numbers

xTrain, xTest, yTrain, yTest = train_test_split(df['message'], df['label_num'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
xTrainCounts = vectorizer.fit_transform(xTrain) # splits the all the messages (combined) into individual words, thus creates a vocb, then creates a matrix of whether a word is present in the message or not (1 present | 0 not present)
xTestCounts = vectorizer.transform(xTest)

model = MultinomialNB()
model.fit(xTrainCounts, yTrain)

yPred = model.predict(xTestCounts)

print("Accuracy:", accuracy_score(yTest, yPred)) 
print("\nConfusion Matrix:\n", confusion_matrix(yTest, yPred))  
print("\nClassification Report:\n", classification_report(yTest, yPred))
