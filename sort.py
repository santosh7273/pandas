import pandas as pd
mp1={
    'Name':['Tsk','Psk','Osk','Fis'],
    'Marks':[32,42,12,23],
    'age':[32,33,32,35]
}
pd1=pd.DataFrame(mp1)
pd1.sort_values(by='Marks',inplace=True)
print(pd1)
pd1.sort_index(inplace=True)
print(pd1)
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
print(pd2['roll_no'].mean())
pd10=pd.Series([1,2,3,2,12,3,4])
print(pd10.value_counts())
