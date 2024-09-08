import pandas as pd
pd1=pd.read_csv(r'C:\Users\Santosh\Downloads\nba.csv',index_col='Name')
mp1={
    'Name':['Sk','Tsk','weth'],
    'Roll_no':[12,13,14]
}
pd2=pd.DataFrame(mp1)
filtered_df = pd2[pd2['Roll_no'] > 12]

# Printing the names where Roll_no > 12
print(filtered_df['Name'])