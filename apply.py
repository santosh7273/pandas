import pandas as pd
def fun(pd1):
    return pd1['A']+pd1['B']+pd1['C']
mp1={
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
}
pd1=pd.DataFrame(mp1)
print(pd1)
pd3=pd1.apply(fun,axis=1)
print(pd3)
