import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores.sort_values(by = 'score', ascending = False)

    df['rank'] = df['score'].rank(method = 'dense', ascending = False)
    result = df[['score', 'rank']]

    return result



