#https://xlsxwriter.readthedocs.io/working_with_pandas.html#using-xlsxwriter-with-pandas

#probando: https://stackoverflow.com/questions/55220000/exporting-a-matplotlib-chart-directly-to-excel-without-saving-to-file-first
#no sirve... borrar

import pandas as pd
import re, os, xlsxwriter, math

import numpy as np
import matplotlib.pyplot as plt


#import .csv to .xlsx

#load data in variable df
df = pd.read_csv(r'/home/pi/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
#create a Pandas Excel writer using XlsxWriter as the engine(motor)
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
#Convert the data to an XlsxWriter Excel object
df.to_excel(writer,sheet_name='prueba')
#Close the Pandas Excel writer and output the Excel file
#writer.save()

#Accessing AlsxWriter from Pandas

#Get the Xlsxwriter objects from the data writer object
#workbook = xlsxwriter.Workbook('test.xlsx')
#worksheet = workbook.add_worksheet()
workbook = writer.book
worksheet = writer.sheets['prueba']

#Adding Charts to Dataframe output

#Create a chart object
chart = workbook.add_chart({'type':'scatter',#Grafico tipo de dispersion
                            'subtype': 'straight'})
#Set the chart title
chart.set_title({'name': 'Total deaths'})
#Configure the series of chart from the dataframe data
    #Spain
chart.add_series({'name':'=prueba!$C$203',
                  'categories':'=prueba!$F$1:$CN$1',#eje x
                  'values':'=prueba!$F$203:$CQ$203'})#eje y
    #US
chart.add_series({'name':'=prueba!$C$227',
                  'categories':'=prueba!$F$1:$CN$1',#eje x
                  'values':'=prueba!$F$227:$CQ$227'})#eje y
    #Italy
chart.add_series({'name':'=prueba!$C$139',
                  'categories':'=prueba!$F$1:$CN$1',#eje x
                  'values':'=prueba!$F$139:$CQ$139'})#eje y
    #Hubei, China
chart.add_series({'name':'=prueba!$B$64',
                  'categories':'=prueba!$F$1:$CN$1',#eje x
                  'values':'=prueba!$F$64:$CQ$64'})#eje y
# Now add a new worksheet and add chart
#worksheet = workbook.add_worksheet(name='Chart')
#Insert the chart into the worksheet
worksheet.insert_chart('B2',chart)
#Configure the chart axes
chart.set_x_axis({'name':'Time','num_format':'mm/dd/yyyy'})
chart.set_y_axis({'name':'Deaths'})

#Close the Pandas Excel writer and output the Excel file
writer.save()
