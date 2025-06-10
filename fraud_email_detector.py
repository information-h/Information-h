import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('dataset.csv')
df.dropna(inplace=True)
x = df['text']
y = df['label']
vectorizer = TfidfVectorizer(stop_word='english')
x_vectoized = vectorizer.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x_vectoized, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

def detect_fraud_email(email_text):
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)[0]
    return "Fraudulent" if prediction == 1 else "Legitimate"

test_email = "Important! update yor bank details immediately."
print("\nTest Email:", test_email)
print("Result:", detect_fraud_email(test_email))