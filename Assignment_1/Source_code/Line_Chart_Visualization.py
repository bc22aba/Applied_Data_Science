import pandas as pd
import matplotlib.pyplot as plt

'''Data Link: https://data.worldbank.org/indicator/SH.DTH.NMRT'''
def ReadData():
     return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/\
Data_sets/Line_Chart_DataSet.xlsx')
    
'''Main Function definition'''
def MultipleLinePlot(): 
    
   '''Get data'''
   data = ReadData()
   
   ''' X axis Data '''
   x_axis = data['Years']    
   y_axis  = data['UAE']
   y_axis1 = data['CHINA']
   y_axis2 = data['INDIA']
   
   plt.plot(x_axis,y_axis,x_axis,y_axis1,x_axis,y_axis2);
   
   plt.ylabel("Count")
   plt.xlabel('Years')
   plt.title("Neonatal Deaths")
   plt.legend(["UAE","CHINA","INDIA"])
   plt.show()
   return 

'''Main Function calling'''
MultipleLinePlot()