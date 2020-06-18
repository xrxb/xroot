import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv (r'/home/pi/.git/COVID-19/archived_data/archived_time_series/time_series_19-covid-Deaths_archived_0325.csv')
filename = '/home/pi/.git/COVID-19/archived_data/archived_time_series/time_series_19-covid-Deaths_archived_0325.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:
        if row[8]=='':
            continue
        high = int(row[8])
        highs.append(high)  #appending high temperatures   
    
    #Plot Data
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(highs, c = 'red') #Line 1

    #Format Plot
    plt.title("Daily High Temperatures, 2018", fontsize = 24)
    plt.xlabel('',fontsize = 16)
    plt.ylabel("Temperature (F)", fontsize = 16)
    #plt.tick_params(axis = 'both', which = 'major' , labelsize = 16)
   # plt.show()





##df = pd.read_csv (r'/home/pi/.git/COVID-19/archived_data/archived_time_series/time_series_19-covid-Deaths_archived_0325.csv')


##print (df)
