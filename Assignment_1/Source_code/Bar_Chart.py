import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''Data link: https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS'''
'''Reading Excel file data'''
def ReadData():
   return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/Data_sets/Bar_Chart_DataSet.xlsx')

''' Function definition'''
def BarPlot(): 
    
   '''Get excel file data '''
   Unemployment_data = ReadData()
   
   ''' X axis Data '''   
   x_axis = Unemployment_data['Country Name'];
   
   '''multiple bar's data'''
   bar1 = Unemployment_data['2021'];
   bar2 = Unemployment_data['2020'];
   bar3 = Unemployment_data['2019'];
   
   '''Legend name for each bar respectively'''
   lengendValues =[2021,2020,2019];
   
   '''Generate Multiple Bar'''
   def CreateBar(X, barValues,width=0.9):
       n = len(barValues);
       _xAxis = np.arange(len(X));
       for i in range(n):
           plt.bar(_xAxis - width/3 + i/float(n)*width, barValues[i],
                   width=width/float(n), align="center") 
        
       '''Setting X-axis ticks'''   
       plt.xticks(_xAxis, X)
       
   '''Create a Figure of width = 12 and height = 10'''
   plt.figure(5,figsize=(12,10),facecolor='lightblue')
   
   '''Calling CreateBar function to generate multi bar plot'''   
   CreateBar(x_axis, [bar1,bar2,bar3]);
   
   plt.ylabel("Unemployment Percentage (%)");
   plt.xlabel('Country');
   plt.title("Unemployment, total (% of total labor force)");
   plt.legend(lengendValues);
   plt.show();
   return

'''Function calling'''
BarPlot()