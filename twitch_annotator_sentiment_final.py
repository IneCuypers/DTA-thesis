import requests
from datetime import datetime
import csv
import json

MODEL = "gpt-oss:20b"

def run_model(prompt):
    payload = {
        "model": "gpt-oss:20b",
        "prompt": prompt,
        "temperature": 0.0,
        "stream": False,
        "seed": 42
    }
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )
    return response.json()["response"].strip()

# Base instruction 
base_prompt = """
You are a binary annotation model for Twitch chat messages.
Given a message, you return either positive (2) or negative (0) or neutral (1). 

Some examples are: 
OH NICE hasL hasL hasL hasL hasL hasL, 2
Shoot through 49 walls with lazer, but hit marker with 50cal shroudY shroudY shroud, 2
bombing is part of the process so i hear :), 2
Insane conversation hasBaited hasBaited hasBaited, 0
London is like Gotham city nowadays only fog and criminals ahahah BigSad BigSad LUL LUL LUL BrokeBack, 0

The output should be structures exactly as: 
message1, sentiment

Only return output exactly as specified, do not return any other information. 

"""

# get chat from file
input_csv = "messages_test.csv"

all_messages = []
with open(input_csv, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0].strip():
            all_messages.append(row[0].strip())

print(f"Loaded {len(all_messages)} messages.")

# Initialize the CSV output with header
all_csv_rows = [["message", "sentiment"]]
# Break into batches of 10
batches = [all_messages[i:i+5] for i in range(0, len(all_messages), 5)]

for batch_index, batch in enumerate(batches, start=1):
    print(f"\n=== Processing batch {batch_index}/{len(batches)} ===")

    msg_block = "\n".join([f"- {m}" for m in batch])
    prompt = f"{base_prompt}\nMessages:\n{msg_block}"

    data = run_model(prompt)

    return data