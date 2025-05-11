import pandas as pd
import json
import requests

# Load the Excel file
df = pd.read_excel("anki sample.xlsx", sheet_name="Sheet1", header=None)
df.columns = ["Front", "Back"]

# Set deck and model names
deck_name = "Default"
model_name = "Basic"

# Prepare notes
notes = []
for index, row in df.iterrows():
    notes.append({
        "deckName": deck_name,
        "modelName": model_name,
        "fields": {
            "Front": str(row["Front"]),
            "Back": str(row["Back"])
        },
        "options": {
            "allowDuplicate": False
        },
        "tags": ["auto"]
    })

# Send to AnkiConnect
payload = {
    "action": "addNotes",
    "version": 6,
    "params": {
        "notes": notes
    }
}

response = requests.post("http://localhost:8765", data=json.dumps(payload))
print(response.json())
