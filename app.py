"""
MoodPlaylist - Streamlit Web Interface
Web version of the AI-powered mood-based playlist generator.
Deploy for free on Streamlit Community Cloud.
"""

import streamlit as st
from textblob import TextBlob

# --- Mood-to-playlist mapping (same as CLI version) ---
MOOD_PLAYLISTS = {
      "happy": {
                "emoji": "😊",
                "genres": "Pop, Dance, Feel-good hits",
                "description": "Upbeat and joyful tunes to match your great mood!",
                "color": "#FFD700"
      },
      "sad": {
                "emoji": "😢",
                "genres": "Acoustic, Lo-fi, Soft ballads",
                "description": "Gentle melodies to comfort and accompany your feelings.",
                "color": "#6495ED"
      },
      "stressed": {
                "emoji": "😰",
                "genres": "Nature sounds, Ambient, Meditation",
                "description": "Calming sounds to help you relax and unwind.",
                "color": "#FF6347"
      },
      "calm": {
                "emoji": "😌",
                "genres": "Classical, Jazz, Chill",
                "description": "Smooth and peaceful music for a serene moment.",
                "color": "#90EE90"
      },
      "energetic": {
                "emoji": "⚡",
                "genres": "Rock, EDM, Workout beats",
                "description": "High-energy tracks to fuel your drive!",
                "color": "#FF8C00"
      }
}

# Keywords for hybrid mood detection
SAD_KEYWORDS = ["lonely", "sad", "miss", "cry", "depressed", "heartbroken",
                                "grief", "lost", "alone", "hopeless", "unhappy", "tears"]
STRESS_KEYWORDS = ["stress", "deadline", "pressure", "anxious", "overwhelm",
                                      "worry", "nervous", "panic", "busy", "exhausted", "insomnia", "sleep"]
ENERGY_KEYWORDS = ["gym", "workout", "run", "strong", "power", "energy",
                                      "motivated", "excited", "pumped", "sprint", "training", "active"]
CALM_KEYWORDS = ["peaceful", "quiet", "relax", "serene", "gentle", "meditation",
                                  "calm", "tranquil", "slow", "reading", "rest", "nature"]


def analyze_mood(text):
      blob = TextBlob(text)
      return blob.sentiment.polarity, blob.sentiment.subjectivity


def count_keywords(text, keywords):
      text_lower = text.lower()
      return sum(1 for word in keywords if word in text_lower)


def classify_mood(text, polarity, subjectivity):
      sad_score = count_keywords(text, SAD_KEYWORDS)
      stress_score = count_keywords(text, STRESS_KEYWORDS)
      energy_score = count_keywords(text, ENERGY_KEYWORDS)
      calm_score = count_keywords(text, CALM_KEYWORDS)

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


# --- Streamlit UI ---
st.set_page_config(page_title="MoodPlaylist", page_icon="🎵", layout="centered")

st.title("🎵 MoodPlaylist")
st.subheader("AI-powered mood-based playlist generator")
st.write("Write a few sentences about your day, and let AI pick the perfect soundtrack for your emotions!")

st.divider()

user_input = st.text_area(
      "How was your day? Tell me about it:",
      placeholder="e.g. Today was amazing! I got a promotion at work and celebrated with friends.",
      height=150
)

if st.button("🎶 Analyze my mood", type="primary", use_container_width=True):
      if user_input.strip():
                polarity, subjectivity = analyze_mood(user_input)
                mood = classify_mood(user_input, polarity, subjectivity)
                playlist = MOOD_PLAYLISTS[mood]

          st.divider()

        col1, col2 = st.columns([1, 2])
        with col1:
                      st.markdown(f"<div style='text-align:center;font-size:80px'>{playlist['emoji']}</div>",
                                                          unsafe_allow_html=True)
                  with col2:
                                st.markdown(f"### Detected mood: {mood.capitalize()}")
                                st.markdown(f"**Suggested playlist:** {playlist['genres']} 🎶")
                                st.markdown(f"*{playlist['description']}*")

        st.divider()

        with st.expander("📊 Sentiment analysis details"):
                      col_a, col_b = st.columns(2)
                      with col_a:
                                        st.metric("Polarity", f"{polarity:.2f}", help="Range: -1 (negative) to +1 (positive)")
                                    with col_b:
                          st.metric("Subjectivity", f"{subjectivity:.2f}", help="Range: 0 (objective) to 1 (subjective)")
else:
        st.warning("Please write something about your day first!")

st.divider()
st.caption("Built with Streamlit & TextBlob | Building AI course project | [GitHub](https://github.com/thierrymaesen/MoodPlaylist)")
