import pandas as pd

def clean_movie_ratings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Make column names lower-case
    df.columns = [c.lower() for c in df.columns]

    # Convert rating column to float if it exists
    if "rating" in df.columns:
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Drop rows missing essential columns
    essential = [col for col in ["userid", "movieid", "rating"] if col in df.columns]
    if essential:
        df = df.dropna(subset=essential)

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df.reset_index(drop=True)
