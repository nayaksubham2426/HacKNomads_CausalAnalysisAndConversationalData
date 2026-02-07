import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

with open("data/Conversational_Transcript_Dataset.json", "r") as f:
    json_data = json.load(f)

data=json_data["transcripts"]
texts = []
labels = []

for item in data:
    full_text = ""
    for turn in item["conversation"]:
        full_text += f"{turn['speaker']}: {turn['text']} "
    texts.append(full_text)
    labels.append(item["intent"])

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

joblib.dump(model, "models/outcome_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model training complete.")