import pandas as pd

SEVERITY_WEIGHT = {
    "WARNING": 1,
    "ERROR": 3
}

def rank_events(df):
    """
    Rank events based on severity and frequency
    """
    df["severity_score"] = df["severity"].map(SEVERITY_WEIGHT).fillna(1)

    freq = df["error_type"].value_counts().to_dict()
    df["frequency_score"] = df["error_type"].map(freq)

    df["priority_score"] = (
        df["severity_score"] * 2 +
        df["frequency_score"]
    )

    ranked = df.sort_values(
        by="priority_score",
        ascending=False
    )

    return ranked
