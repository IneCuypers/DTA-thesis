# Emotes in Different Twitch Chats

	This thesis looks at the the influence of streamer Gender, Age, and Genre on sentiment and emotion expressed in emote-containing Twitch chats messages. This repository contains the:

# Repository structure: 
	- 'dataset_9600' - messages annotated with streamer metadata, sentiment, and emotion (excel/csv)
	- 'code/' - notebooks for sentiment and emotion annotation, model evaluation, and RQs logregs
	- 'environment.yml' / 'requirements.txt' - Conda env dependecy file, two options
	- 'twitch_annotator_sentiment_final.py' & 'twitch_annotator_emotion_final.py' - sentiment & emotion GPT-oss annotation prompts
	- README.md - project documentation								


#setting up conda environment: 
- conda env create -f environment.yml
- conda activate your_environment_name

# Data Annotation

The sentiment and emotion annotations were generated using a local LLM (`gpt-oss:20b`) via Ollama. 

## How to reproduce annotations:
1. Ensure you have [Ollama](https://ollama.com/) installed and running locally.
2. Pull the required model:
   ```bash
   ollama pull gpt-oss:20b

python code/twitch_annotator_{sentiment/eemotion}_final.py

# raw chat data collected with: https://github.com/BoringBoredom/Twitch-Chat-Downloader
