from sklearn.metrics.pairwise import cosine_similarity
import os
import joblib
import logging

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(BASE_DIR, "recommend.log"), encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.info("🔁 Loading data...")
try:
    models_dir = os.path.join(BASE_DIR, "..", "models")
    df = joblib.load(os.path.join(models_dir, 'df_cleaned.pkl'))
    tfidf_matrix = joblib.load(os.path.join(models_dir, 'tfidf_matrix.pkl'))
    tfidf = joblib.load(os.path.join(models_dir, 'tfidf_vectorizer.pkl'))
    logging.info("✅ Data and models loaded successfully.")
except Exception as e:
    logging.error("❌ Failed to load required files: %s", str(e))
    raise e


def recommend_songs(song_name, top_n=5):
    logging.info("🎵 Recommending songs for: '%s'", song_name)
    
    # Get the row of the selected song
    song_row = df[df['song'].str.lower() == song_name.lower()]
    if song_row.empty:
        logging.warning("⚠️ Song not found in dataset.")
        return None
        
    idx = song_row.index[0]
    
    # Instead of loading a massive precomputed matrix (800MB+),
    # we calculate similarity for just this one song (very fast and memory efficient)
    song_vector = tfidf_matrix[idx]
    cosine_sim_scores = cosine_similarity(song_vector, tfidf_matrix).flatten()
    
    # Get top similarity scores
    sim_scores = list(enumerate(cosine_sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    
    song_indices = [i[0] for i in sim_scores]
    logging.info("✅ Top %d recommendations ready.", top_n)
    # Create DataFrame with clean serial numbers starting from 1
    result_df = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
    result_df.index = result_df.index + 1  # Start from 1 instead of 0
    result_df.index.name = "S.No."

    return result_df
