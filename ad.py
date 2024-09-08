import pandas as pd
pd1=pd.read_csv(r'C:\Users\Santosh\Downloads\nba.csv')
print(pd1)
print(pd1.head(5))
se1=pd1['Name']
print(se1.head(10))
print(se1)
print(pd1.tail())
print(pd1.tail(10))