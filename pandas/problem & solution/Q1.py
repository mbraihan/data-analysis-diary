import pandas as pd
from pandas import read_excel
import numpy as np

df = pd.read_excel('/run/media/n30/Jarvis/work/learn/data-analysis-diary/pandas/problem & solution/chunk.xlsx')

df_gender = pd.read_excel('/run/media/n30/Jarvis/work/learn/data-analysis-diary/pandas/problem & solution/chunk.xlsx', 'Dataset-student')
df_math = pd.read_excel('/run/media/n30/Jarvis/work/learn/data-analysis-diary/pandas/problem & solution/chunk.xlsx', 'Dataset-student-math')



female_idx = (df.index[df_gender['sex'] == 'F'].tolist())
male_idx = (df.index[df_gender['sex'] == 'M'].tolist())
print(female_idx)
print(male_idx)

m = 0
for l in male_idx:
    a = df_math.loc[l, 'G3']
    m = m + a
print(m)

f = 0
for l in female_idx:
    a = df_math.loc[l, 'G3']
    f = f + a
print(f)

diff = m-f
print(diff)