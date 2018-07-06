
#Q1
import pandas as pd
import numpy as np
data = {'Name':['vivek','kohli','dhoni','dhawan',],'Age':[20,22,2.1,20],'mail id':['vivek@gmail.com','kohli@gmail.com','dhonih@gmail.com','dhawan@gmail.com'],'Phone Number':[9887745091,9781232345,9887669921,9078765532]}
df=pd.DataFrame(d,index=[1,2,3,4])
print(df)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)



'''
#Q2

import pandas as pd
data=pd.read_csv("datasheet.csv")
df=pd.DataFrame(data)
print(df)

print(df.head(5))

print(df.head(10))

print(df.shape)
print(df.axes)
print(df.sum())
print(df.describe())
print(df.size)
print(df.dtypes)

print(df.tail(5))

print("2nd column MinTemp:")
print(df['MinTemp'])
print(df['MinTemp'].shape)
print(df['MinTemp'].sum())
print(df['MinTemp'].describe())
print(df['MinTemp'].count())
print(df['MinTemp'].axes)
print(df['MinTemp'].mean())
print(df['MinTemp'].size)
print(df['MinTemp'].dtypes)

'''