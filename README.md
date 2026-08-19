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


# raw chat data collected wtith: https://github.com/BoringBoredom/Twitch-Chat-Downloader
