import pandas as pd
mp1={
    'Name':['Santosh','Kumar'],
    'Rollno':[1,2]
}
pd1=pd.DataFrame(mp1)
print(pd1)
#Adding new column
add=['rajjevenagar','colony']
pd1['address']=add
print(pd1)