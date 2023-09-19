import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
#firstly filter out only those employee id and name based on the given condition
    
    employees['bonus'] = employees[(employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))]['salary']

#secondly fill the missing gaps with zero
    employees['bonus'] = employees['bonus'].fillna(0)


#finally return the sorted values
    return employees[['employee_id', 'bonus']].sort_values(by = 'employee_id')


