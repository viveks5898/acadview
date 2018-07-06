import pandas as pd
import numpy as np

d={'Name':['vivek','Ayush','Balwant','Rakesh'],'Age':[20,20,22,21],'Email':['vivek30@gmail.com','ayushbhatia668@gmail.com','Balwant.rawat@gmail.com','rakeshkumar@@gmail.com'],
'Phonen':[2300002300,1975444390,2349678321,4123767476]}
df=pd.DataFrame(d,index=[1,2,3,4])
print(df)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)



#Question 2

import pandas as pd
import numpy as np
df=pd.read_csv('data.csv')
print([df.head(n=5)])  #First 5 rows of the dataframe
print([df.head(n=10)]) #First 10 rows of the dataframe

print("describe",df.describe())
print(df.tail(n=10)) # last 5 rows of the dataframe
print(df['MinTemp'].describe())


print("Count ",df['MinTemp'].count())  #basic statistics on the particular dataset.
print("Min ",df['MinTemp'].min())
print("Max ",df['MinTemp'].max())
print("Mean ",df['MinTemp'].mean())
print("Median ",df['MinTemp'].median())
print("Mode ",df['MinTemp'].mode())
