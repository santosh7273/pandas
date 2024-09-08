import pandas as pd
import numpy as np
li=['sk','pk',123]
pd1=pd.Series(li,index=[1,2,3])
print(pd1)
pd2=pd.DataFrame(li,index=['a','b','c'])
print(pd2)
np1=np.array([1,2,3])
pd3=pd.Series(data=np1*100,index=['e','f','g'])
print(pd3)
np2=np.arange(10,20)
pd4=pd.Series(np2)
print(pd4)
np4,ad=np.linspace(0,20,5,retstep=True)
print(np4)
pd5=pd.Series(np4)
print(pd5)
pd6=pd.Series(range(1,55,2))
print(pd6)