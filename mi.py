import pandas as pd
mp2={
    'Name':['hi','are','tu'],
    'roll_no':[1,2,3]
}
pd2=pd.DataFrame(mp2)
pd2.set_index('Name',inplace=True)
print(pd2)
pd2.reset_index(inplace=True)
print(pd2)
pd2.sort_values(by=['Name' and 'roll_no'],inplace=True)
print(pd2)
print(pd2)
fil=pd2['roll_no']>=2
pd2.drop(index=pd2[fil].index,inplace=True)
print(pd2)