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

gRate3 = gRate2.reindex(['China','India','Malaysia','USA','Brazil','Pakistan','England'])
print(gRate3)

gRate4 = gRate2.reindex(['China','India','Malaysia','USA','Brazil','Pakistan','England'],fill_value=0)
print(gRate4)

print(gRate3.ffill())

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
print(df.head())

df.to_csv('Test.csv')
print(df.loc['Row1'])

print(type(df.loc['Row2']))
print(df.iloc[:,:])
print(df.iloc[0:1,0:2])

print(type(df.iloc[0:1,0:2]))
print(df.iloc[:2,:3])
print(df.iloc[1:,:3])

print(df['Col1'])
print(type(df['Col1']))

print(df[['Col1','Col2']])
print(df.iloc[1:,:3].values)

print(type(df.iloc[1:,:3].values))

df.iloc[1:,:3].values.shape
df.isnull()
df.isnull().sum()
df['Col1'].value_counts()
df['Col1'].unique()


Data='{"name":"John", "email":"john@email.com", "job":[{"Title1":"Programmer", "Title2":"Engineer"}]}'
pd.read_json(Data)

arr=np.arange(16).reshape(4,4)
print(arr)

dframe1 = pd.DataFrame(arr, index=['Row1','Row3','Row4','Row5'], columns=['Col1','Col2','Col3','Col4'])
print(dframe1)

dframe2 = dframe1.reindex(['Row1','Row2','Row3','Row4','Row5'])
print(dframe2)

dframe2 = dframe2.reindex(columns=['Col0','Col1','Col2','Col4'])
print(dframe2)

print(dframe2.ffill(axis=0))

dframe2=dframe2.reindex(columns=['Col1','Col2','Col3','Col4'])
print(dframe2)

print(dframe2.ffill(axis=1))