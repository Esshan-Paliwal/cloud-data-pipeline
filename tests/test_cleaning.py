import pandas as pd
from src.cleaning import clean_movie_ratings

def test_basic_cleaning():
    df = pd.DataFrame({
        "userId": [1, 2, 2],
        "movieId": [10, 20, 20],
        "rating": ["4", "3.0", "3.0"]
    })
    out = clean_movie_ratings(df)
    # duplicates removed -> 2 rows expected
    assert out.shape[0] == 2
