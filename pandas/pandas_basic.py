import pandas as pd
import numpy as np

srs = pd.Series([10,20,30,40])

print("The series values are\n")
print(srs.values)

print("The series index values are\n")
print(srs.index.values)

gRate = pd.Series([11.2,36.0,16.6,21.8,34.2],index=['China','India','USA','Brazil','Pakistan'])

gRate.name = 'Growth Rate' #set series name
gRate.index.name = 'Country' # set series index name

print("The indexed series values are\n")
print(gRate)

print(gRate.values)
print(gRate.name)

print(gRate.index.values)
print(gRate.index.name)

gRate1 = pd.Series([11.2,36.0,16.6,21.8,34.2], index = ['China','India','Brazil','USA','Pakistan'])
gRate2 = pd.Series([20.3,11.2,36.0,16.6,21.8,8.7], index = ['Africa','China','India','Brazil','USA','Nigeria'])

result = gRate1/gRate2

result.name = "Result"
result.index.name = 'Country'

print(result)

print(pd.isnull(result))

print(pd.notnull(result))

print(result[result == 1.0]) #print indexes that satisfy the condition

print(result[result != 1.0])

# Dataframe

df=pd.DataFrame(np.arange(0,12).reshape(4,3),index=['Row1','Row2','Row3','Row4'],columns=['Col1','Col2','Col3'])
df.head()