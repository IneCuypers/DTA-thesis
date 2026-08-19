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
You are a multi-label annotation model for Twitch chat messages.
Given a message, you return all the emotions expressed in that message. 
The emotions are: 
	- anger (also annoyance, rage)
	- anticipation (also interest, vigilance)
	- disgust  (also disintrest, dislike, loathing)
	- fear (also apprehension, anxiety, terror)
	- joy (also serenity, ecstacy)
	- love (also affection)
	- optimism (also hopefulness, confidence)
	- pessimism (also cynicism, no confidence)
	- sadness (also pensiveness, grief)
	- surprise (also distraction, amazement)
	- trust (also acceptance, liking, admiration)

Some examples are: 
PoroSad oh NYOO NOT ANXIETYYY, fear, sadness
OH NICE hasL hasL hasL hasL hasL hasL, joy, love, trust
new plaqueboyLogo emote??, anticipation, surprise
Jay Z? imtexpSmile TheIlluminati, surprise, joy, anticipation
Shoot through 49 walls with lazer but hit marker with 50cal shroudY shroudY shroudY, anger, disgust, pessimism

The output should be structures exactly as the following: 
message1, emotion1, emotion2, emotion3,...
message2, emotion1

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

# Break into batches of 5
batches = [all_messages[i:i+5] for i in range(0, len(all_messages), 5)]

for batch_index, batch in enumerate(batches, start=1):
    print(f"\n=== Processing batch {batch_index}/{len(batches)} ===")

    msg_block = "\n".join([f"- {m}" for m in batch])
    prompt = f"{base_prompt}\nMessages:\n{msg_block}"

    data = run_model(prompt)

    return data