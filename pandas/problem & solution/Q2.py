import pandas as pd
from pandas import read_excel
import numpy as np

# df = pd.read_excel('/run/media/n30/Jarvis/work/learn/data-analysis-diary/pandas/problem & solution/chunk.xlsx')

df_gender = pd.read_excel('/pandas/problem & solution/chunk.xlsx', 'Dataset-student')
df_math = pd.read_excel('/pandas/problem & solution/chunk.xlsx', 'Dataset-student-math')

# print(df_math.head())

df_grade = df_math[["G2", "G3"]]

# print(df_grade.head())

df_grade['diff'] = df_grade['G2'] - df_grade['G3']

print(df_grade.head())

female_idx = (df.index[df_grade['diff'] > 0].tolist())
print (female_idx)
# count = 0
# if df_grade['diff'] > 0:
#     count = count + 1

# print(count)