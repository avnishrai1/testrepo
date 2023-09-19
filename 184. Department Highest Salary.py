import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    merge_col = employee.merge(department, left_on = 'departmentId', right_on = 'id')

    rename_col = merge_col.rename(columns = {'name_x' : 'Employee','name_y' : 'Department', 'salary' : 'Salary'})[['Department', 'Employee', 'Salary']]

    data = rename_col

    data = data[data['Salary'] == data.groupby('Department')['Salary'].transform(max)]

    return data



