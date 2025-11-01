# LLM PROMPT

## Prompt

    OK, so let's do that –always keeping in mind the course's academic honesty policy. I want to use FastAPI, SQLAlchemy, and React to make an audio focused web app. I would love to also integrate ML/Data science, concepts and libraries to the application. List the ideas. Don't write "modules", task lists or further design the application. 

## Answer

    Acknowledged. We are operating within the constraints of the CS50 academic honesty policy. The goal is to "amplify" your learning by brainstorming concepts, not "supplant" your design work by providing architecture.

    Here are several audio-focused project ideas. Each concept identifies a core ML/Data Science task that naturally integrates with your chosen tech stack (FastAPI, SQLAlchemy, React).

    ---

    ### 1. Automatic Genre Classifier

    * **The Concept:** A user uploads a song or audio clip. The application analyzes the file and presents a prediction of its musical genre (e.g., "Rock," "Classical," "Electronic").
    * **The ML/Data Science Angle:** This is a **classification** problem. Your backend would use a library like `librosa` to perform **feature extraction** (e.g., MFCCs, spectral contrast, tempo) from the audio. You would use these features to train a model (using `scikit-learn`) to predict the genre. SQLAlchemy would store the user's upload history and the model's predictions.

    ---

    ### 2. "Query by Example" Sound Finder

    * **The Concept:** A user has a large library of sounds. They upload one *new* sound (e.g., a snare drum hit), and the application finds the 10 "most similar" sounds *already in their library*.
    * **The ML/Data Science Angle:** This is a **nearest-neighbor search** or "content-based retrieval" problem. Your backend would pre-process all of a user's uploaded files into numerical **feature vectors** (using `librosa`) and store them. When the user uploads a query sound, it is also converted into a vector, and your application (using `scikit-learn`) calculates the **Euclidean distance** or **cosine similarity** to find the closest matches.

    ---

    ### 3. Unsupervised Drum Sample Sorter

    * **The Concept:** A musician uploads a folder containing 100 random, unlabeled drum samples. The application automatically groups them into logical categories (e.g., "kicks," "snares," "hi-hats").
    * **The ML/Data Science Angle:** This is an **unsupervised clustering** problem. You would again use `librosa` for **feature extraction** on all files. Then, you would use a `scikit-learn` algorithm like **KMeans** to sort these files into *k* distinct clusters based on their sonic properties. The React frontend would then display these groups, which the user could name and organize.

    ---

    ### 4. Audio "Mood" or Key Detector

    * **The Concept:** A user uploads a piece of music. The app analyzes it and returns data on its "mood" (e.g., "Happy," "Sad," "Energetic" – often derived from valence and arousal) or its musical key (e.g., "C Minor").
    * **The ML/Data Science Angle:** This combines **feature extraction** with **classification** or **DSP**. `librosa` has functions to extract features that correlate with key (chromagrams) and energy/tempo. You could either use built-in `librosa` functions for key detection or train a simple `scikit-learn` model to predict mood based on features like tempo, energy, and spectral brightness.

    All these ideas leave the core architectural design and implementation—how the API is built, how the database is structured, and how the React components are managed—entirely to you.

    Do any of these concepts serve as a good starting point for your project?
