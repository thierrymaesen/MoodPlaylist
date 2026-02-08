# MoodPlaylist

Building AI course project

## Summary

MoodPlaylist is a Python-based AI tool that analyzes the sentiment of short diary entries to detect your mood and suggest a matching music playlist genre. Write a few sentences about your day, and let AI pick the perfect soundtrack for your emotions.

## Background

Many people listen to music to match or improve their mood, but choosing the right playlist can be tedious. The problems this project addresses:

* People often struggle to identify their own emotional state clearly
* Manually searching for mood-appropriate music takes time and effort
* Existing music recommendation systems rely on listening history, not on how you actually feel right now

My personal motivation comes from the daily habit of journaling and listening to music. Combining both activities with AI felt like a natural and practical idea. Mood-based recommendations can also support mental well-being by helping people become more aware of their emotions.

## How is it used?

The user opens a simple command-line Python application and types a short text about their day, feelings, or current state of mind. The program analyzes the text using sentiment analysis (NLP) and classifies the mood into categories such as: happy, sad, stressed, calm, or energetic.

Based on the detected mood, the application suggests a playlist genre or ambiance:

* **Happy** → Pop, Dance, Feel-good hits
* **Sad** → Acoustic, Lo-fi, Soft ballads
* **Stressed** → Nature sounds, Ambient, Meditation
* **Calm** → Classical, Jazz, Chill
* **Energetic** → Rock, EDM, Workout beats

Example usage:

```python
python moodplaylist.py

How was your day? Tell me about it:
> Today was amazing! I got a promotion at work and celebrated with friends.

Detected mood: Happy 😊
Suggested playlist: Pop / Feel-good hits 🎶
```

The solution is designed for anyone who journals or wants a quick music suggestion. It can be used at any time of day, on any device with Python installed. It is especially useful for people who use music as a tool for emotional regulation.

## Data sources and AI methods

The project uses the following data and techniques:

* **Text input**: User-provided diary entries (free text)
* **Sentiment analysis**: Using Python's [TextBlob](https://textblob.readthedocs.io/) or [NLTK VADER](https://www.nltk.org/howto/sentiment.html) library for natural language processing
* **Mood classification**: Rule-based mapping from sentiment polarity/subjectivity scores to mood categories
* **Playlist mapping**: A predefined dictionary mapping moods to music genres

| Technique | Purpose |
| ----------- | ----------- |
| NLP (Sentiment Analysis) | Detect emotion from text |
| Rule-based classification | Map sentiment scores to mood categories |
| Dictionary lookup | Suggest playlist genre based on mood |

No external API or paid service is required. Everything runs locally with Python.

## Challenges

This project does not solve the following:

* It cannot detect complex or mixed emotions with high accuracy (e.g., feeling nostalgic yet happy)
* Sarcasm and irony in text are difficult to interpret correctly with basic sentiment analysis
* The playlist suggestions are generic genres, not actual song lists (integration with Spotify API could be a future improvement)
* The system works best in English; multilingual support would require additional NLP models

Ethical considerations: the tool processes personal text entries, so privacy must be ensured. All processing happens locally, and no data is stored or shared.

## What next?

This project could grow in several ways:

* Integrate with the Spotify or YouTube Music API to generate real playlists automatically
* Add a simple web interface using Flask or Streamlit for a better user experience
* Use a more advanced NLP model (like a fine-tuned transformer) for better emotion detection
* Support multiple languages for a wider audience
* Add a mood tracking dashboard that visualizes emotional patterns over time

To move forward, I would need skills in API integration, web development, and possibly deep learning for improved NLP.

## Acknowledgments

* This project was inspired by the Building AI course created by Reaktor Innovations and University of Helsinki
* Sentiment analysis powered by [TextBlob](https://textblob.readthedocs.io/) / [NLTK](https://www.nltk.org/) — open source Python libraries
* Sleeping cat image example from the course template by [Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)h
