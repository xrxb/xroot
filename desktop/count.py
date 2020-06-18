import pandas as pd
import re, os, xlsxwriter, math, csv

import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'/home/pi/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

ttl = df.shape
#total = ttl[1] #total columns .csv
total=int(input())
total=total-1
abc="abcdefghijklmnopqrstuvwxyz"
i=0
y=[]
def count(total,i,y):
    print("waiting...")
    print(total,i)
    if total > len(abc):
        total = total - abc
        i=i+1
        if i > len(abc):
            count(total,i)
    y.append(total)
    y.append(i)
    return y

y=count(total,i,y)
total=y[0]
i=y[1]
if i != 0:
    result=abc[i]+abc[total]
else:
    result=abc[total]
print(result)

