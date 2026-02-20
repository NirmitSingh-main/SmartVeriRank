import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf(df):
    """
    Converts error_type + message into TF-IDF vectors
    """
    corpus = (
        df["error_type"].fillna("") + " " +
        df["message"].fillna("")
    )

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.9,
        stop_words="english"
    )

    X = vectorizer.fit_transform(corpus)
    return X, vectorizer


