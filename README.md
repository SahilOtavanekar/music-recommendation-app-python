# Music Recommendation System

## Overview

This project is a Python-based Music Recommendation System that suggests songs to users based on textual similarity of song lyrics. It uses Natural Language Processing (NLP) and Machine Learning techniques to analyze lyrics and generate recommendations.
The project was developed as part of an academic learning process and demonstrates practical use of NLP, feature extraction, and similarity-based recommendation systems.

## Features

1.Text preprocessing and cleaning of song lyrics
2.TF-IDF vectorization for feature extraction
3.Cosine similarity for song recommendation
4.WordCloud visualization for lyrics analysis
5.Modular and reproducible project structure

## Tech Stack

-Python
-Pandas, NumPy
-Scikit-learn
-NLTK
-Matplotlib
-WordCloud

## How It Works
Song lyrics are preprocessed (lowercasing, cleaning, stopword removal).
TF-IDF is applied to convert text into numerical vectors.
Cosine similarity is used to compute similarity between songs.
The system recommends songs with the highest similarity scores.

## Setup Instructions

Clone the repository:

git clone https://github.com/SahilOtavanekar/music-recommendation-app-python.git


Create and activate a virtual environment:

python -m venv .venv
source .venv/Scripts/activate


Install dependencies:

pip install -r requirements.txt


Run the notebook or scripts from the src folder.

## Dataset

The project uses a publicly available song lyrics dataset (downloaded via Kaggle).
Dataset files are not included in the repository to keep it lightweight.

## Academic Relevance

Demonstrates NLP-based recommendation systems

Applies similarity metrics in real-world data

Suitable for Data Science and Machine Learning coursework

## Author

Sahil Otavanekar
MSc Data Science

## License

This project is intended for educational and academic use.
