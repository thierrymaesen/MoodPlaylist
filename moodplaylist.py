"""
MoodPlaylist - AI-powered mood-based playlist generator
Building AI course project - University of Helsinki

This prototype analyzes the sentiment of a short diary entry
and suggests a music playlist genre based on detected mood.
Uses TextBlob for NLP (sentiment analysis) combined with
keyword detection for improved accuracy (hybrid approach).

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

# Keywords to boost mood detection beyond simple polarity
SAD_KEYWORDS = ["lonely", "sad", "miss", "cry", "depressed", "heartbroken",
                "grief", "lost", "alone", "hopeless", "unhappy", "tears"]
STRESS_KEYWORDS = ["stress", "deadline", "pressure", "anxious", "overwhelm",
                   "worry", "nervous", "panic", "busy", "exhausted", "insomnia", "sleep"]
ENERGY_KEYWORDS = ["gym", "workout", "run", "strong", "power", "energy",
                   "motivated", "excited", "pumped", "sprint", "training", "active"]
CALM_KEYWORDS = ["peaceful", "quiet", "relax", "serene", "gentle", "meditation",
                 "calm", "tranquil", "slow", "reading", "rest", "nature"]


def analyze_mood(text):
    """
    Analyze the sentiment of a text using TextBlob.
    Returns polarity (-1 to 1) and subjectivity (0 to 1).
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity


def count_keywords(text, keywords):
    """Count how many mood keywords appear in the text."""
    text_lower = text.lower()
    return sum(1 for word in keywords if word in text_lower)


def classify_mood(text, polarity, subjectivity):
    """
    Classify mood using a hybrid approach:
    1. Check for mood-specific keywords in the text
    2. Use sentiment polarity as a secondary signal
    This improves accuracy over pure sentiment analysis.
    """
    sad_score = count_keywords(text, SAD_KEYWORDS)
    stress_score = count_keywords(text, STRESS_KEYWORDS)
    energy_score = count_keywords(text, ENERGY_KEYWORDS)
    calm_score = count_keywords(text, CALM_KEYWORDS)

    # Keyword-boosted classification
    if sad_score >= 2 or (sad_score >= 1 and polarity < 0):
        return "sad"
    if stress_score >= 2 or (stress_score >= 1 and polarity < 0.1):
        return "stressed"
    if polarity > 0.4:
        return "happy"
    if energy_score >= 2 or (energy_score >= 1 and polarity > 0):
        return "energetic"
    if calm_score >= 2 or (calm_score >= 1 and abs(polarity) < 0.2):
        return "calm"
    if polarity > 0.1:
        return "happy"
    if polarity < -0.2:
        return "sad"
    if polarity < 0:
        return "stressed"
    return "calm"


def suggest_playlist(mood):
    """Return playlist suggestion based on the detected mood."""
    return MOOD_PLAYLISTS.get(mood, MOOD_PLAYLISTS["calm"])


def main():
    """
    Main function: ask the user for a diary entry,
    analyze sentiment, detect mood, and suggest a playlist.
    """
    print("=" * 55)
    print("  🎵 MoodPlaylist - AI Mood-Based Playlist Generator")
    print("=" * 55)
    print()

    # Get user input
    print("How was your day? Tell me about it:")
    user_input = input("> ")
    print()

    # Analyze sentiment
    polarity, subjectivity = analyze_mood(user_input)

    # Classify mood (hybrid: sentiment + keywords)
    mood = classify_mood(user_input, polarity, subjectivity)

    # Get playlist suggestion
    playlist = suggest_playlist(mood)

    # Display results
    print("-" * 55)
    print(f"  Detected mood: {mood.capitalize()} {playlist['emoji']}")
    print(f"  Suggested playlist: {playlist['genres']} 🎶")
    print(f"  {playlist['description']}")
    print("-" * 55)
    print()
    print(f"  [Sentiment details: polarity={polarity:.2f}, subjectivity={subjectivity:.2f}]")
    print()


if __name__ == "__main__":
    main()
