import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
      author_viewed = views[views['author_id'] == views['viewer_id']] 
      author_unique = author_viewed['author_id'].unique()
      author_unique = sorted(author_unique)

      df = pd.DataFrame({'id' : author_unique})
      return df


