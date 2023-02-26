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
    return pd.read_excel('D:/WorkSpace/Applied_Data_Science/Assignment_1/\
Data_sets/Pie_Chart_DataSet.xlsx')

'''Function Definition to Generate Pie_Chart Plot'''
def PieChart():
    
    '''Get Data from Excel file'''
    population_data = ReadData()
    data = population_data["Population Percentage"]
    labels =population_data["Country Name"]
    plt.pie(data,labels=labels,autopct='%1.1f%%');
    plt.title("% of World Population")
    plt.show()
    return

'''Function Calling to Generate Pie_Chart'''
PieChart()

