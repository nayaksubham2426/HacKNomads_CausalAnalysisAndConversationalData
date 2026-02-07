# Grahak Mitra-Conversational Causal Analysis System

> From simple event detection to causal analysis and interactive reasoning over multi-turn conversational transcripts.

---

##  Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [Team](#team)
- [License](#license)

---

## About

Grahak Mitra is a large-scale conversational system that generates extensive collections of multi-turn dialogue transcripts between agents and customers.Some conversations are associated with explicitly labeled outcome events such as escalations, complaints, refunds, or other operationally significant events.

Why Grahak Mitra ?

Traditional systems record that an event occurred, but they do not identify:

- Which specific dialogue turns contributed to the event  
- How conversational patterns evolved prior to the event  
- Recurring conversational structures linked to similar outcomes  
- Evidence-backed explanations grounded in transcript data  

This project aims to move beyond simple event detection and build a system capable of:

- Identifying causal dialogue spans  
- Producing interpretable explanations  
- Supporting interactive reasoning  
- Maintaining contextual consistency across multiple user queries  

---

## Features

###  Causal Event Detection
- Detects outcome events in conversations  
- Identifies dialogue turns contributing to events  
- Scores causal spans with confidence values  

###  Conversational Pattern Analysis
- Tracks multi-turn conversational evolution  
- Identifies recurring escalation structures  
- Detects systematic behavioral triggers  

###  Interpretable Explanations
- Provides traceable evidence from transcripts  
- Highlights relevant dialogue turns  
- Ensures transparency and explainability  

###  Interactive Reasoning
- Allows follow-up analytical queries  
- Maintains conversation memory  
- Supports multi-turn contextual reasoning  

---

## Tech Stack

### Backend
- Python 3.14.2
- Flask 
- Scikit-learn
- NLTK
- Scipy
- Pandas
- joblib  

### Frontend
- Html
- Css

### Database
- mysql

### Dataset
- JSON-based storage

---

## Getting Started

### Prerequisites

- Python 3.14+
- Git

##  Getting Started

### Create Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

##  Project Structure

```
conversational-causal-analysis/
│
|___ data/
|  |___Conversational_Transcript_dataset.json
|___models
   |__outcome_model.pkl
   |__vectorizer.pkl
├── templates
   |___index.html
|___task1.py
|___task2.py
|___train.py
|___app.py
|___db.py
|___queries.csv
   |____queries.csv
|
|___ requirements.txt
|
└── README.md
|
|__ technical_report.pdf

```

## Usage Guide

1.Load conversational transcript dataset
2.Run preprocessing script
   python scripts/preprocess.py
3.Train models
   python scripts/train.py
4.Run inference
   python scripts/infer.py --conversation_id conv_001
5.View causal spans and explanations

## API Documentation

### Base URL

http://localhost:8000/api

### Analyze Conversation

POST /analyze
Request:
Json
{
  "conversation_id": "conv_001",
  "event_type": "escalation"
}

Response:
Json
{
  "success": true,
  "causal_spans": [
    {
      "turn_index": 4,
      "text": "This issue has still not been resolved.",
      "score": 0.91
    }
  ],
  "confidence": 0.88,
  "explanation": "Escalation triggered by repeated unresolved complaints."
}


## Contributing

We welcome contributions! Here's how you can help:
1.Fork the repository
2.Create a new branch
  git checkout -b feature/your-feature
3.Commit changes
  git commit -m "Add new feature"
4.Push to branch
  git push origin feature/your-feature
5.Open a Pull Request

## Team

Team
Team Name: HackNomads
Subham Nayak – Frontend
B.Vineet Patro – Backend & NLP
Mohapatra S.H Gargi – Model Development
Nikita – Deployment & Testing

## License
This project is licensed under the MIT License.
