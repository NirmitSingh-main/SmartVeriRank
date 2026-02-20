from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(X):
    """
    Computes cosine similarity between events
    """
    return cosine_similarity(X)
