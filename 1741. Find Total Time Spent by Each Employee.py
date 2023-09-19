import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['total_time'] = employees['out_time'] - employees['in_time']

    df = employees.groupby(by = ['emp_id', 'event_day'], as_index = False).sum()

    result = df.rename(columns = {'event_day' : 'day'})
    return result[['day', 'emp_id','total_time']]


