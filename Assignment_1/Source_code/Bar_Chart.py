import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''Reading Excel file data'''
def ReadData():
   return pd.read_excel('C:/Users/chrag/Downloads/Bar_Chart_DataSet.xlsx')

''' Function definition'''
def BarPlot(): 
    
   '''Get data'''
   Unemployment_data = ReadData()
   
   ''' X axis Data '''
   cols =["2021","2020","2019"]
   plt.figure(5,figsize=(12,10),facecolor='lightblue')
   plt.subplot(1, 1, 1)
   
   width1 = 0.4
   plt.bar(Unemployment_data['Country Name'],Unemployment_data['2021'],width=width1)
   plt.bar(Unemployment_data['Country Name'],Unemployment_data['2020'],width=width1)
  
   plt.ylabel("Percentage (%)")
   plt.xlabel('Country')
   plt.title("Unemployment, total (% of total labor force)")
   plt.legend(["2021","2020"])
   plt.show()
   return

'''Function calling'''
BarPlot()