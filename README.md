<div align="center">

🇬🇧 [English version](#english) | 🇫🇷 [Version française](#french)

</div>

---

<a name="english"></a>

# MoodPlaylist

Building AI course project

<img src="moodplaylist_v2.png" alt="MoodPlaylist" width="600">

## Summary

MoodPlaylist is a Python-based AI tool that analyzes the sentiment of short diary entries to detect your mood and suggest a matching music playlist genre. Write a few sentences about your day, and let AI pick the perfect soundtrack for your emotions.

## Background

Many people listen to music to match or improve their mood, but choosing the right playlist can be tedious. The problems this project addresses:

* People often struggle to identify their own emotional state clearly
* * Manually searching for mood-appropriate music takes time and effort
  * * Existing music recommendation systems rely on listening history, not on how you actually feel right now
   
    * My personal motivation comes from the daily habit of journaling and listening to music. Combining both activities with AI felt like a natural and practical idea. Mood-based recommendations can also support mental well-being by helping people become more aware of their emotions.
   
    * ## How is it used?
   
    * The user opens a simple command-line Python application and types a short text about their day, feelings, or current state of mind. The program analyzes the text using sentiment analysis (NLP) and classifies the mood into categories such as: happy, sad, stressed, calm, or energetic.
   
    * Based on the detected mood, the application suggests a playlist genre or ambiance:
   
    * * **Happy** → Pop, Dance, Feel-good hits
      * * **Sad** → Acoustic, Lo-fi, Soft ballads
        * * **Stressed** → Nature sounds, Ambient, Meditation
          * * **Calm** → Classical, Jazz, Chill
            * * **Energetic** → Rock, EDM, Workout beats
             
              * Example usage:
             
              * ```
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
                * * **Sentiment analysis**: Using Python's [TextBlob](https://textblob.readthedocs.io/) or [NLTK VADER](https://www.nltk.org/howto/sentiment.html) library for natural language processing
                  * * **Mood classification**: Rule-based mapping from sentiment polarity/subjectivity scores to mood categories
                    * * **Playlist mapping**: A predefined dictionary mapping moods to music genres
                     
                      * | Technique | Purpose |
                      * |-----------|---------|
                      * | NLP (Sentiment Analysis) | Detect emotion from text |
                      * | Rule-based classification | Map sentiment scores to mood categories |
                      * | Dictionary lookup | Suggest playlist genre based on mood |
                     
                      * No external API or paid service is required. Everything runs locally with Python.
                     
                      * ## Challenges
                     
                      * This project does not solve the following:
                     
                      * * It cannot detect complex or mixed emotions with high accuracy (e.g., feeling nostalgic yet happy)
                        * * Sarcasm and irony in text are difficult to interpret correctly with basic sentiment analysis
                          * * The playlist suggestions are generic genres, not actual song lists (integration with Spotify API could be a future improvement)
                            * * The system works best in English; multilingual support would require additional NLP models
                             
                              * Ethical considerations: the tool processes personal text entries, so privacy must be ensured. All processing happens locally, and no data is stored or shared.
                             
                              * ## What next?
                             
                              * This project could grow in several ways:
                             
                              * * Integrate with the Spotify or YouTube Music API to generate real playlists automatically
                                * * Add a simple web interface using Flask or Streamlit for a better user experience
                                  * * Use a more advanced NLP model (like a fine-tuned transformer) for better emotion detection
                                    * * Support multiple languages for a wider audience
                                      * * Add a mood tracking dashboard that visualizes emotional patterns over time
                                       
                                        * To move forward, I would need skills in API integration, web development, and possibly deep learning for improved NLP.
                                       
                                        * ## Acknowledgments
                                       
                                        * * This project was inspired by the Building AI course created by Reaktor Innovations and University of Helsinki
                                          * * Sentiment analysis powered by [TextBlob](https://textblob.readthedocs.io/) / [NLTK](https://www.nltk.org/) — open source Python libraries
                                            * * Sleeping cat image example from the course template by [Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
                                             
                                              * ---
                                             
                                              * <a name="french"></a>

                                              # MoodPlaylist

                                              Projet du cours Building AI

                                              <img src="moodplaylist_v2.png" alt="MoodPlaylist" width="600">

                                              ## Résumé

                                              MoodPlaylist est un outil IA basé sur Python qui analyse le sentiment de courtes entrées de journal intime pour détecter votre humeur et suggérer un genre de playlist musicale correspondant. Écrivez quelques phrases sur votre journée et laissez l'IA choisir la bande-son parfaite pour vos émotions.

                                              ## Contexte

                                              Beaucoup de gens écoutent de la musique pour accompagner ou améliorer leur humeur, mais choisir la bonne playlist peut être fastidieux. Les problèmes que ce projet aborde :

                                              * Les gens ont souvent du mal à identifier clairement leur propre état émotionnel
                                              * * Chercher manuellement de la musique adaptée à son humeur prend du temps et de l'énergie
                                                * * Les systèmes de recommandation musicale existants se basent sur l'historique d'écoute, pas sur ce que vous ressentez réellement en ce moment
                                                 
                                                  * Ma motivation personnelle vient de l'habitude quotidienne d'écrire un journal et d'écouter de la musique. Combiner les deux activités avec l'IA m'a semblé être une idée naturelle et pratique. Les recommandations basées sur l'humeur peuvent aussi soutenir le bien-être mental en aidant les gens à mieux prendre conscience de leurs émotions.
                                                 
                                                  * ## Comment l'utiliser ?
                                                 
                                                  * L'utilisateur ouvre une application Python en ligne de commande et tape un court texte sur sa journée, ses sentiments ou son état d'esprit actuel. Le programme analyse le texte à l'aide de l'analyse de sentiment (NLP) et classe l'humeur en catégories telles que : joyeux, triste, stressé, calme ou énergique.
                                                 
                                                  * En fonction de l'humeur détectée, l'application suggère un genre de playlist ou une ambiance :
                                                 
                                                  * * **Joyeux** → Pop, Dance, Tubes feel-good
                                                    * * **Triste** → Acoustique, Lo-fi, Ballades douces
                                                      * * **Stressé** → Sons de la nature, Ambient, Méditation
                                                        * * **Calme** → Classique, Jazz, Chill
                                                          * * **Énergique** → Rock, EDM, Musique d'entraînement
                                                           
                                                            * Exemple d'utilisation :
                                                           
                                                            * ```
                                                              python moodplaylist.py
                                                              Comment s'est passée votre journée ? Racontez-moi :
                                                              > Aujourd'hui était incroyable ! J'ai eu une promotion au travail et j'ai fêté ça avec des amis.
                                                              Humeur détectée : Joyeux 😊
                                                              Playlist suggérée : Pop / Tubes feel-good 🎶
                                                              ```

                                                              La solution est conçue pour tous ceux qui tiennent un journal ou veulent une suggestion musicale rapide. Elle peut être utilisée à tout moment de la journée, sur n'importe quel appareil avec Python installé. Elle est particulièrement utile pour les personnes qui utilisent la musique comme outil de régulation émotionnelle.

                                                              ## Sources de données et méthodes IA

                                                              Le projet utilise les données et techniques suivantes :

                                                              * **Entrée texte** : Entrées de journal fournies par l'utilisateur (texte libre)
                                                              * * **Analyse de sentiment** : Utilisation de [TextBlob](https://textblob.readthedocs.io/) ou [NLTK VADER](https://www.nltk.org/howto/sentiment.html) de Python pour le traitement du langage naturel
                                                                * * **Classification de l'humeur** : Mappage basé sur des règles depuis les scores de polarité/subjectivité vers des catégories d'humeur
                                                                  * * **Mappage des playlists** : Un dictionnaire prédéfini associant les humeurs aux genres musicaux
                                                                   
                                                                    * | Technique | Objectif |
                                                                    * |-----------|----------|
                                                                    * | NLP (Analyse de Sentiment) | Détecter l'émotion à partir du texte |
                                                                    * | Classification basée sur des règles | Associer les scores de sentiment aux catégories d'humeur |
                                                                    * | Recherche dans un dictionnaire | Suggérer un genre de playlist selon l'humeur |
                                                                   
                                                                    * Aucune API externe ou service payant n'est requis. Tout fonctionne localement avec Python.
                                                                   
                                                                    * ## Défis
                                                                   
                                                                    * Ce projet ne résout pas les problèmes suivants :
                                                                   
                                                                    * * Il ne peut pas détecter les émotions complexes ou mixtes avec une grande précision (par ex., se sentir nostalgique et heureux à la fois)
                                                                      * * Le sarcasme et l'ironie dans le texte sont difficiles à interpréter correctement avec une analyse de sentiment basique
                                                                        * * Les suggestions de playlists sont des genres génériques, pas des listes de chansons réelles (l'intégration de l'API Spotify pourrait être une amélioration future)
                                                                          * * Le système fonctionne mieux en anglais ; le support multilingue nécessiterait des modèles NLP supplémentaires
                                                                           
                                                                            * Considérations éthiques : l'outil traite des entrées de texte personnelles, la confidentialité doit donc être assurée. Tout le traitement se fait localement et aucune donnée n'est stockée ou partagée.
                                                                           
                                                                            * ## Et ensuite ?
                                                                           
                                                                            * Ce projet pourrait évoluer de plusieurs façons :
                                                                           
                                                                            * * Intégration avec l'API Spotify ou YouTube Music pour générer automatiquement de vraies playlists
                                                                              * * Ajout d'une interface web simple avec Flask ou Streamlit pour une meilleure expérience utilisateur
                                                                                * * Utilisation d'un modèle NLP plus avancé (comme un transformer fine-tuné) pour une meilleure détection des émotions
                                                                                  * * Support de plusieurs langues pour un public plus large
                                                                                    * * Ajout d'un tableau de bord de suivi de l'humeur qui visualise les tendances émotionnelles au fil du temps
                                                                                     
                                                                                      * Pour aller plus loin, j'aurais besoin de compétences en intégration d'API, développement web, et éventuellement en deep learning pour améliorer le NLP.
                                                                                     
                                                                                      * ## Remerciements
                                                                                     
                                                                                      * * Ce projet a été inspiré par le cours Building AI créé par Reaktor Innovations et l'Université de Helsinki
                                                                                        * * Analyse de sentiment propulsée par [TextBlob](https://textblob.readthedocs.io/) / [NLTK](https://www.nltk.org/) — bibliothèques Python open source
                                                                                          * * Image du chat endormi exemple du template du cours par [Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
