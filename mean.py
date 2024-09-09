import pandas as pd
s1=pd.Series([1,2,3,4,5])
print(s1.mean())
s2=pd.Series([4,5,None,45,None])
print(s2.mean(skipna=True))
mp1={
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
}
pd3=pd.DataFrame(mp1)
print(pd3.mad(axis=0))
