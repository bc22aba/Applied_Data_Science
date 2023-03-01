# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 09:44:38 2023

@author: Cheruku Bhaskar
"""
import pandas as pd
import matplotlib.pyplot as plt

'''Data link: https://en.wikipedia.org/wiki/\
              List_of_countries_and_dependencies_by_population'''
              
'''Read Excel file Data using pandas'''
def ReadData():
    #As Per the PEP-8 guidelines each line should not exceed 79 characters
    #So i have used backslash to separate the code.
    return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/\
Data_sets/Pie_Chart_DataSet.xlsx')

'''Main Function Definition to Generate Pie_Chart Plot'''
def PieChart():
    
    '''Get Data from Excel file'''
    population_data = ReadData()
    data = population_data["Population Percentage"]
    labels =population_data["Country Name"]
    
    #Creating Pie chart
    plt.pie(data,labels=labels,autopct='%1.1f%%');
    
    #Title of pie chart
    plt.title("% of World Population")
    plt.show()
    return

'''Main Function Calling to Generate Pie_Chart'''
PieChart()

