import pandas as pd
pd1=pd.read_csv(r'C:\Users\Santosh\Downloads\nba.csv',index_col='Name')
print(pd1)
print(pd1.iloc[:,2:])
print(pd1.loc[:, ["Team", "Number", "Position"]])