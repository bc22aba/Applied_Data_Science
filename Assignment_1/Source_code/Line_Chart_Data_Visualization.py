import pandas as pd
import matplotlib.pyplot as plt

def ReadData():
    return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/Data_sets/covid_worldwide.xlsx',nrows=8)
    
''' Function definition'''
def MultiplePlot(): 
    
   '''Get data'''
   data = ReadData()
   
   ''' X axis Data '''
   x_axis = data['Country'] 
   
   y_axis  = data['Total Cases']
   y_axis1 = data['Total Deaths']
   y_axis2 = data['Total Recovered']
   y_axis3 = data['Active Cases']
   
   plt.plot(x_axis,y_axis,x_axis,y_axis1,x_axis,y_axis2,x_axis,y_axis3);
   
   plt.ylabel("Count")
   plt.xlabel('Country')
   plt.title("COVID CASES")
   plt.legend(["Total Cases","Total Deaths","Total Recovered","Active Cases"])
   plt.show()
   return 

'''Function calling'''
MultiplePlot()