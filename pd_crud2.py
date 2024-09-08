import pandas as pd
pd1=pd.read_csv(r'C:\Users\Santosh\Downloads\nba.csv',index_col='Name')
print(pd1)
#inplace=True means it will modify the original DataFram
#axis=1 means column and 0 means row
pd1.drop(['Team','Weight'],inplace=True,axis=1)
print(pd1)
print(pd1.loc['Jae Crowder'])
pd3=pd.DataFrame(pd1)
print(pd3)
pd3.drop(['Raul Neto'],inplace=True)
print(pd3)
print(pd3.loc[['R.J. Hunter','Jeff Withey']])
#frm this to that point
print(pd3.loc['R.J. Hunter':'Jeff Withey'])
print(pd3.loc[["Avery Bradley", "R.J. Hunter"],
                   ["Number", "Position"]])
