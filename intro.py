import pandas as pd
data_set1={
    'name':['Santosh','Kiran','Rakesh'],
    'rollno':['22L31A05M5','22L31A0503','22L31A05M57']
}
pd1=pd.DataFrame(data_set1)
print(pd1)
print(pd.__version__)
li=['santosh','kumar','tyada']
pd2=pd.DataFrame(li)
print(pd2)
