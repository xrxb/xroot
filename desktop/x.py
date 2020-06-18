import pandas as pd
import re, os, xlsxwriter, math, csv
import xlrd
import numpy as np
import matplotlib.pyplot as plt

##file_location = '/home/pi/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
file_location = 'test.xlsx'

df = pd.read_excel('test.xlsx','prueba')

