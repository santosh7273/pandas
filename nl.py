import pandas as pd
pd1=pd.read_csv(r'C:\Users\Santosh\Downloads\nba.csv',index_col='Name')
mp1={
    'Name':['Sk','Tsk','weth'],
    'Roll_no':[12,13,14],
    'Country':['USA','IND','IND']
}
pd2=pd.DataFrame(mp1)
filtered_df = pd2['Roll_no'] >= 12
print(pd2.loc[filtered_df])
li=['IND']
fd2=pd2['Country'].isin(li)
print(pd2.loc[fd2])