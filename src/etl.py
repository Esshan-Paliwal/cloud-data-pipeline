import pandas as pd
from cleaning import clean_movie_ratings
from config import LOCAL_TEST_FILE

def main():
    if not LOCAL_TEST_FILE:
        print("Set LOCAL_TEST_FILE to a CSV file path before running.")
        return

    print(f"Reading local file: {LOCAL_TEST_FILE}")
    df = pd.read_csv(LOCAL_TEST_FILE)

    df_clean = clean_movie_ratings(df)
    print("Cleaned Data (first 10 rows):")
    print(df_clean.head(10).to_string(index=False))

if __name__ == "__main__":
    main()
