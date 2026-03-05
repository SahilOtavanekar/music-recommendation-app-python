# 🎵 Music Recommendation System

A content-based music recommender system built using Python, Scikit-Learn, and Streamlit. The application uses TF-IDF vectorization and Cosine Similarity to find similar songs based on their lyrical content.

## 📝 Overview

This project suggests songs based on textual similarity of lyrics, utilizing NLP and Machine Learning techniques. It demonstrates the practical application of feature extraction and similarity metrics in a real-world context.

## 🚀 Features

- **Lyric-Based Recommendations**: Finds songs with similar themes and vocabulary.
- **Interactive UI**: Easy-to-use dropdown menu to select songs.
- **Fast Performance**: Precomputed similarity matrices for instant suggestions.
- **Clean Architecture**: Organized structure following industry best practices.
- **Visualizations**: WordCloud support for lyrics analysis.

## 🛠️ Tech Stack

- **Python 3.13**
- **Streamlit**: Web interface
- **Pandas & NumPy**: Data manipulation
- **Scikit-Learn**: TF-IDF and Cosine Similarity
- **NLTK**: Natural language preprocessing
- **Joblib**: Model serialization
- **Matplotlib & WordCloud**: Data visualization

## 📂 Project Structure

```text
├── data/               # Raw and processed datasets (ignored by git)
├── models/             # Serialized models and similarity matrices (ignored by git)
├── notebooks/          # Jupyter notebooks for experimentation
├── src/                # Source code
│   ├── main.py         # Streamlit application entry point
│   ├── preprocess.py   # Script for data cleaning and model building
│   └── recommend.py    # Logic for generating recommendations
├── requirements.txt    # Project dependencies
└── .env.example        # Template for environment variables
```

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/SahilOtavanekar/music-recommendation-app-python.git
cd music-recommendation-app-python
```

### 2. Create a virtual environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Data Preparation
Place your `spotify_millsongdata.csv` in the `data/` directory. Then run the preprocessing script to generate the models:
```bash
python src/preprocess.py
```

## 🖥️ Usage

To launch the Streamlit application:
```bash
streamlit run src/main.py
```
The app will be available at `http://localhost:8501`.

## 📂 Dataset

The project uses a publicly available song lyrics dataset. Dataset files are excluded from the repository to keep it lightweight; please ensure the `data/` directory is correctly populated before running simulation scripts.

## 🎓 Academic Relevance

Developed by **Sahil Otavanekar** (MSc Data Science), this project applies similarity metrics suitable for Data Science and Machine Learning coursework.

## 📝 License

This project is open-source and available under the MIT License.
