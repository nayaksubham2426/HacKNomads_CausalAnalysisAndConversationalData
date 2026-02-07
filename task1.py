import json
import joblib
from db import save_turn
model = joblib.load("models/outcome_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_event(query):
    X = vectorizer.transform([query])
    return model.predict(X)[0]

def load_data():
    with open("data/Conversational_Transcript_Dataset.json", "r") as f:
        return json.load(f)["transcripts"]

def retrieve_transcripts(event):
    data = load_data()
    return [t for t in data if t["intent"] == event]

def extract_evidence(transcript):
    evidence = []
    keywords = ["never received", "wrong address", "refund", "late", "investigation"]

    for i, turn in enumerate(transcript["conversation"]):
        if any(k in turn["text"].lower() for k in keywords):
            evidence.append({
                "turn_number": i + 1,
                "speaker": turn["speaker"],
                "text": turn["text"]
            })

    return evidence

def generate_explanation(query):
    event = predict_event(query)
    transcripts = retrieve_transcripts(event)

    results = []

    for t in transcripts:
        evidence = extract_evidence(t)
        if evidence:
            results.append({
                "transcript_id": t["transcript_id"],
                "evidence": evidence[:3]
            })
    output={
        "query":query,
        "predicted_event":event,
        "supporting_cases":results[:3]
    }
    save_turn(
        query=query,
        category=event,
        output=output,
        remarks="Intent prediction with supporting evidence"
    )

    return output