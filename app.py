import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Streamlit UI Setup

st.set_page_config(page_title="Movie Recommender System", layout="wide")
st.title("Movie Recommender System")
st.write("Find similar movies instantly based on genres, cast, keywords, and more!")


# Load & Prepare Data

@st.cache_data
def load_data():
    movies = pd.read_csv("movies_metadata.csv", low_memory=False)
    credits = pd.read_csv("credits.csv")

    #  Fix: convert 'id' columns to numeric safely 
    movies['id'] = pd.to_numeric(movies['id'], errors='coerce')
    credits['id'] = pd.to_numeric(credits['id'], errors='coerce')

    # Drop rows where id is missing
    movies.dropna(subset=['id'], inplace=True)
    credits.dropna(subset=['id'], inplace=True)

    # Convert to int for merging
    movies['id'] = movies['id'].astype(int)
    credits['id'] = credits['id'].astype(int)

    # Merge datasets
    df = movies.merge(credits, on='id', how='left')

    # Keep relevant columns (some may not exist in credits)
    keep_cols = [c for c in ['title', 'overview', 'genres', 'cast', 'crew', 'keywords'] if c in df.columns]
    df = df[keep_cols]
    df.dropna(subset=['overview'], inplace=True)

    #  Combine all text columns into one 
    def parse_text(x):
        try:
            data = eval(x.replace("'", '"'))
            if isinstance(data, list):
                return " ".join(d.get("name", "") for d in data if isinstance(d, dict))
            else:
                return ""
        except:
            return ""

    for col in ['genres', 'cast', 'crew', 'keywords']:
        if col in df.columns:
            df[col] = df[col].apply(parse_text)
        else:
            df[col] = ""

    df['tags'] = (
        df['overview'] + " " +
        df['genres'] + " " +
        df['cast'] + " " +
        df['crew'] + " " +
        df['keywords']
    )

    df = df[['title', 'tags']].drop_duplicates(subset='title').reset_index(drop=True)
    return df


# st.info("Loading and preparing data...")
df = load_data()
# st.success("Data loaded successfully!")


# Build Lightweight Model

@st.cache_resource
def build_vectorizer(df):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(df['tags'])
    return cv, vectors

# st.info("Building model (this may take a moment)...")
cv, vectors = build_vectorizer(df)
# st.success("Model ready!")


# Recommendation Function

def recommend(movie_title, n=5):
    titles = df['title'].str.lower().fillna('')
    matches = df[titles == movie_title.lower()]

    if matches.empty:
        st.warning("Movie not found in database.")
        return []

    idx = matches.index[0]
    movie_vec = vectors[idx]
    sim_scores = cosine_similarity(movie_vec, vectors).flatten()
    sim_indices = sim_scores.argsort()[-n-1:-1][::-1]
    return df.iloc[sim_indices]['title'].values.tolist()


# Streamlit Interaction

st.subheader("Search for a Movie")
movie_name = st.text_input("Enter movie name", "")

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name first!")
    else:
        st.info("Finding similar movies...")
        recommendations = recommend(movie_name, n=10)
        if recommendations:
            st.success("Here are your recommendations:")
            for i, title in enumerate(recommendations, start=1):
                st.write(f"{i}.**{title}**")
        else:
            st.error("No recommendations found.")

st.markdown("---")
st.caption("Developed by Aarya")
