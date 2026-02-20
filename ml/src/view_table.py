import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # ml/
CSV_PATH = os.path.join(BASE_DIR, "data", "events.csv")

print("Looking for CSV at:", CSV_PATH)

if not os.path.exists(CSV_PATH):
    print("ERROR: events.csv NOT FOUND")
    exit(1)

df = pd.read_csv(CSV_PATH)

print("\n===== EVENTS TABLE (first 10 rows) =====\n")
print(df.head(10).to_string(index=False))

print("\nTotal rows:", len(df))
print("Columns:", list(df.columns))