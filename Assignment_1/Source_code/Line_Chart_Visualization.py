import pandas as pd
import matplotlib.pyplot as plt

'''Data Link: https://data.worldbank.org/indicator/SH.DTH.NMRT'''
def ReadData():
    #As Per the PEP-8 guidelines each line should not exceed 79 characters
    #So i have used backslash to separate the code.
     return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/\
Data_sets/Line_Chart_DataSet.xlsx')
    
''' Main Function definition'''
def MultipleLinePlot(): 
    
   '''Get data'''
   data = ReadData()
   
   # X axis Data
   x_axis = data['Years']   
   
   #Line 1 plot y axis data
   y_axis  = data['UAE']
   #Line 2 plot y axis data
   y_axis1 = data['CHINA']
   #Line 3 plot y axis data
   y_axis2 = data['INDIA']
   
   #Generating multiple line plots
   plt.plot(x_axis,y_axis,x_axis,y_axis1,x_axis,y_axis2);
   
   #Y-axis Label definition
   plt.ylabel("Count")
   
   #X-axis Label definition
   plt.xlabel('Years')
   
   #Plot Title
   plt.title("Neonatal Deaths")
   
   #Legend Values for each line plot
   plt.legend(["UAE","CHINA","INDIA"])
   plt.show()
   return 

'''Main Function calling'''
MultipleLinePlot()