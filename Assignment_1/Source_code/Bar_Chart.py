# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 1:27:11 2023

@author: Cheruku Bhaskar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''Data link: https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS'''

'''Reading Excel file data'''
def ReadData():
    #As Per the PEP-8 guidelines each line should not exceed 79 characters
    #So i have used backslash to separate the code.
   return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/\
Data_sets/Bar_Chart_DataSet.xlsx')
                        
'''Generate Multiple Bar'''
def CreateBar(X, barValues,width=0.9):
    #Returns the length of an array
     n = len(barValues);
     _xAxis = np.arange(len(X));
     for i in range(n):
         #Below snippet is used to draw multiple bars without overlapping 
         #on each other.
         plt.bar(_xAxis - width/3 + i/float(n)*width, barValues[i],
                 width=width/float(n), align="center") 
      
     '''Setting X-axis ticks'''   
     plt.xticks(_xAxis, X)


'''Main Function definition'''
def BarPlot(): 
    
   '''Get excel file data '''
   unemployment_data = ReadData()
   
   ''' X axis Data '''   
   x_axis = unemployment_data['Country Name'];
   
   '''multiple bar's data'''
   bar1 = unemployment_data['2021'];
   bar2 = unemployment_data['2020'];
   bar3 = unemployment_data['2019'];
   
   '''Legend name for each bar respectively'''
   lengendValues =[2021,2020,2019];   
       
   '''Create a Figure of width = 12 and height = 10'''
   plt.figure(5,figsize=(12,10),facecolor='lightblue')
   
   '''Calling CreateBar function to generate multi bar plot'''   
   CreateBar(x_axis, [bar1,bar2,bar3]);
   
   #Y-axis label 
   plt.ylabel("Unemployment Percentage (%)");
   #X-axis label
   plt.xlabel('Country');
   #Bar Plot Title
   plt.title("Unemployment % out of total population year wise");
   ##legend values for each bar plot for a given group
   plt.legend(lengendValues);
   plt.show();
   return

'''Main Function  calling'''
BarPlot()