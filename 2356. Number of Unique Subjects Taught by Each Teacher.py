import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    df1 = df.rename(columns = {'subject_id' : 'cnt'})
    return df1[['teacher_id', 'cnt']]
