import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    cooperate = actor_director.groupby(['actor_id','director_id']).size().reset_index(name = 'total')

    cooperate = cooperate[cooperate['total'] >= 3]

    return cooperate[['actor_id', 'director_id']]




