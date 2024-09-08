import pandas as pd
pd1=pd.read_csv(r'C:\Users\Santosh\Downloads\nba.csv')
print(pd1)
print(pd1.describe())
pd2=pd1['Name']
print(pd2.describe())