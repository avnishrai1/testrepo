import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    #firstly delete all the duplicates salary from salary column
    unique = employee['salary'].drop_duplicates()

    #now arrange the salary in the order of high to low 
    sort_unique = unique.sort_values(ascending = False)
    
    #here the comparsion will be done, if the salary Nth is greater then the len of sort unique then it will return none
    if len(sort_unique) < N :
        nth_highest = None

    #otherwise it will return the highest  nth salary
    else :
        nth_highest = sort_unique.iloc[N - 1]
        
    #here create a new column name getHighestSalary and return the highest salry onto it.
    return pd.DataFrame({f'getNthHighestSalary({N})' : [nth_highest]})
   