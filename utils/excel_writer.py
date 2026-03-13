from datetime import date


def append_recommendations(df, recommendations):
    
    col_name = f"CS Recommendation {date.today()}"
    df[col_name] = recommendations

    return df