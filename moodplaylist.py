"""
MoodPlaylist - AI-powered mood-based playlist generator
Building AI course project - University of Helsinki

This prototype analyzes the sentiment of a short diary entry
and suggests a music playlist genre based on detected mood.
Uses TextBlob for Natural Language Processing (sentiment analysis).

Install dependencies:
    pip install textblob

First-time setup (download NLTK corpora):
    python -m textblob.download_corpora
"""

from textblob import TextBlob


# Mood-to-playlist mapping
MOOD_PLAYLISTS = {
    "happy": {
        "emoji": "😊",
        "genres": "Pop, Dance, Feel-good hits",
        "description": "Upbeat and joyful tunes to match your great mood!"
    },
    "sad": {
        "emoji": "😢",
        "genres": "Acoustic, Lo-fi, Soft ballads",
        "description": "Gentle melodies to comfort and accompany your feelings."
    },
    "stressed": {
        "emoji": "😰",
        "genres": "Nature sounds, Ambient, Meditation",
        "description": "Calming sounds to help you relax and unwind."
    },
    "calm": {
        "emoji": "😌",
        "genres": "Classical, Jazz, Chill",
        "description": "Smooth and peaceful music for a serene moment."
    },
    "energetic": {
        "emoji": "⚡",
        "genres": "Rock, EDM, Workout beats",
        "description": "High-energy tracks to fuel your drive!"
    }
}


def analyze_mood(text):
    """
    Analyze the sentiment of a text using TextBlob.
    Returns polarity (-1 to 1) and subjectivity (0 to 1).
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity


def classify_mood(polarity, subjectivity):
    """
    Classify mood based on sentiment polarity and subjectivity scores.

    Rules:
    - Very positive (polarity > 0.5) and subjective -> happy
    - Positive (polarity > 0.1) and less subjective -> energetic
    - Very negative (polarity < -0.3) -> sad
    - Slightly negative and subjective -> stressed
    - Near neutral -> calm
    """
    if polarity > 0.5:
        return "happy"
    elif polarity > 0.1 and subjectivity < 0.5:
        return "energetic"
    elif polarity > 0.1:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    elif polarity < 0:
        return "stressed"
    else:
        return "calm"


def suggest_playlist(mood):
    """
    Return playlist suggestion based on the detected mood.
    """
    return MOOD_PLAYLISTS.get(mood, MOOD_PLAYLISTS["calm"])


def main():
    """
    Main function: ask the user for a diary entry,
    analyze sentiment, detect mood, and suggest a playlist.
    """
    print("=" * 50)
    print("  🎵 MoodPlaylist - AI Mood-Based Playlist Generator")
    print("=" * 50)
    print()

    # Get user input
    print("How was your day? Tell me about it:")
    user_input = input("> ")
    print()

    # Analyze sentiment
    polarity, subjectivity = analyze_mood(user_input)

    # Classify mood
    mood = classify_mood(polarity, subjectivity)

    # Get playlist suggestion
    playlist = suggest_playlist(mood)

    # Display results
    print("-" * 50)
    print(f"  Detected mood: {mood.capitalize()} {playlist['emoji']}")
    print(f"  Suggested playlist: {playlist['genres']} 🎶")
    print(f"  {playlist['description']}")
    print("-" * 50)
    print()
    print(f"  [Sentiment details: polarity={polarity:.2f}, subjectivity={subjectivity:.2f}]")
    print()


if __name__ == "__main__":
    main()
