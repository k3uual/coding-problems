# %%
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mp

dict1 = {
    "Name":['a','b','c','d'],
    "Marks" : [12,45,67,23],
    "City" : ['x','y','z','w'],
    "Count" : [100,200,300,400]
}

df = pd.DataFrame(dict1)
print(df)
df.plot()
