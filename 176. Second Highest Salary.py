import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique = employee['salary'].drop_duplicates()
    sort_unique = unique.sort_values(ascending = False)

    if len(sort_unique) > 1 :
        second_highest = sort_unique.iloc[1]

    else :
        second_highest = None

    return pd.DataFrame({'SecondHighestSalary' : [second_highest]})