import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = 0
    average = 0
    high = 0

    for salary in accounts['income'] :
        
        if salary < 20000 :
            low = low + 1

        elif salary >= 20000 and salary <= 50000 :
            average = average + 1

        elif salary > 50000 :
            high = high + 1

    df = pd.DataFrame({'category' : ['High Salary', 'Low Salary', 'Average Salary'],'accounts_count' : [high,low, average]})

    return df