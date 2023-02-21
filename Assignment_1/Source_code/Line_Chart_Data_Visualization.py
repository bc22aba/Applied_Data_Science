import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def ReadCSVData():
    import pandas as pd
    return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/Data_sets/covid_worldwide.xlsx',nrows=8)
    
''' Function definition'''
def LicenCHart(): 
   df = ReadCSVData()
   x_axis= df['Country']
   y_axis=df['Total Deaths'].astype(int)
   plt.plot(x_axis,y_axis);
   plt.ylabel("Count")
   plt.xlabel('Country')
   plt.title("COVID CASES")
   plt.legend("Total Deaths")
   ''' plt.set_ylim(100000,999999999,100000)'''
   plt.show()
   return 

'''Function calling'''
LicenCHart()