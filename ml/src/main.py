import pandas as pd
import os
import sys

# Ensure package imports work from both relative and direct execution
try:
    from features.text_features import build_tfidf
    from models.similarity import compute_similarity
    from ranking.ranker import rank_events
except ImportError:
    from ml.src.features.text_features import build_tfidf
    from ml.src.models.similarity import compute_similarity
    from ml.src.ranking.ranker import rank_events

# Determine data path relative to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "events.csv")

df = pd.read_csv(data_path)

X, vectorizer = build_tfidf(df)
sim_matrix = compute_similarity(X)

ranked = rank_events(df)

print("\n==== TOP 10 PRIORITY EVENTS ====\n")
print(ranked.head(10)[
    ["run_id", "severity", "error_type", "priority_score"]
].to_string(index=False))

if __name__ == "__main__":
    print("\nML Pipeline completed successfully!")
