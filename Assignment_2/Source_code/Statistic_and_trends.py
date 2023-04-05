# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 06:23:16 2023

@author: cheru
"""

import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#import seaborn

'''Function Definition to read CSV file'''
def Read_CSV_File(csvFileName):
    return pd.read_csv(r''+csvFileName+'', skiprows = 3)


'''Function calling to read csv file data'''
file_name = 'D:\WorkSpace\Applied_Data_Science\Assignment_2\Datasets\API_19_DS2_en_csv_v2_5361599.csv'
df = Read_CSV_File(file_name);
df.head(5)

cntry_list = ["CHN", "DEU", "FRA", "GBR", "JPN", "KOR", "MEX", "USA", "ZWE"]
indicator_list = ["AG.LND.FRST.ZS", "EG.ELC.COAL.ZS", "EN.ATM.CO2E.KT", "EN.ATM.METH.KT.CE", "SP.POP.GROW", "EG.ELC.NUCL.ZS", "SP.URB.TOTL.IN.ZS"]
df_cntry = df[df['Country Code'].isin(cntry_list)]
dfc_indicator = df_cntry[df['Indicator Code'].isin(indicator_list)]

data1 = dfc_indicator.drop(dfc_indicator.loc[:,'1960':'1989'].columns, axis = 1)

df_final = data1.loc[:,['Country Name','Indicator Name','1990','1995','2000','2005','2010','2014']]
df_final[['1990','1995','2000','2005','2010','2014']] = df_final[['1990','1995','2000','2005','2010','2014']].astype(float)

# Saving file with Years as Columns
df_final.to_csv('df_final.csv')

# shape from wide to long with melt function in pandas
df2=pd.melt(df_final,id_vars=['Country Name','Indicator Name'],var_name='Year', value_name='values')

# reshape from long to wide in pandas python
df2=df2.pivot(index=['Indicator Name','Year'], columns='Country Name', values='values')
df2.head(5)

# Saving file with Country Name as Columns
df2.to_csv('df2.csv')

# Summary statistics for some of the variables 
# CO2 emissions 
df2_CO2 = df_final[df_final['Indicator Name']=='CO2 emissions (kt)']
df2CO2 = df2_CO2.drop(['Indicator Name'], axis = 1)
df2CO2t = df2CO2.transpose()
CO2 =df2CO2t.rename(columns=df2CO2t.iloc[0]).drop(df2CO2t.index[0])
CO2 = CO2.astype(float)
print("CO2 Emissions (kt) of countries")
CO2.describe()

plt.figure(figsize=(14,8))
plt.plot(CO2)
#add legend
plt.legend(CO2, bbox_to_anchor=(1.04, 0.5), loc="center left")
#add axis labels and a title
plt.ylabel('CO2 Emissions (kt)', fontsize=12)
plt.xlabel('Time Line', fontsize=12)
plt.title('CO2 Emissions (kt) (from 1990 to 2014)', fontsize=12)
plt.show()


# Electricity production from coal sources (% of total) 
df2_EP_COAL = df_final[df_final['Indicator Name']=='Electricity production from coal sources (% of total)']
df2EPCOAL = df2_EP_COAL.drop(['Indicator Name'], axis = 1)
df2EPCOALt = df2EPCOAL.transpose()
EPCOAL =df2EPCOALt.rename(columns=df2EPCOALt.iloc[0]).drop(df2EPCOALt.index[0])
EPCOAL = EPCOAL.astype(float)
print("Electricity production from coal sources (% of total) ")
EPCOAL.describe()

plt.figure(figsize=(14,8))
plt.plot(EPCOAL)
#add legend
plt.legend(EPCOAL, bbox_to_anchor=(1.04, 0.5), loc="center left")
#add axis labels and a title
plt.ylabel('Electricity Production (% of Total)', fontsize=12)
plt.xlabel('Time Line', fontsize=12)
plt.title('Electricity production from coal sources (from 1990 to 2014)', fontsize=12)
plt.show()

# Methane gas emissions 
df2_Methane = df_final[df_final['Indicator Name']=='Methane emissions (kt of CO2 equivalent)']
df2Methane = df2_Methane.drop(['Indicator Name'], axis = 1)
df2Methanet = df2Methane.transpose()
Methane =df2Methanet.rename(columns=df2Methanet.iloc[0]).drop(df2Methanet.index[0])
Methane = Methane.astype(float)

plt.rcParams['figure.figsize'] = [15,8]
Methane.plot.bar()
#add legend
plt.legend(Methane, bbox_to_anchor=(1.04, 0.5), loc="center left")
#add axis labels and a title
plt.ylabel('Methane emissions (kt of CO2 equivalent)', fontsize=12)
plt.xlabel('Time Line', fontsize=12)
plt.title('Methane emissions (kt of CO2 equivalent)(from 1990 to 2014)', fontsize=12)
plt.show()

# Nuclear Power Production 
df2_Nuclear = df_final[df_final['Indicator Name']=='Electricity production from nuclear sources (% of total)']
df2Nuclear = df2_Nuclear.drop(['Indicator Name'], axis = 1)
df2Nucleart = df2Nuclear.transpose()
Nuclear =df2Nucleart.rename(columns=df2Nucleart.iloc[0]).drop(df2Nucleart.index[0])
Nuclear = Nuclear.astype(float)

plt.rcParams['figure.figsize'] = [15,8]
Nuclear.plot.bar()
#add legend
plt.legend(Nuclear, bbox_to_anchor=(1.04, 0.5), loc="center left")
#add axis labels and a title
plt.ylabel('Electricity production from nuclear sources (% of total)', fontsize=12)
plt.xlabel('Time Line', fontsize=12)
plt.title('Electricity production from nuclear sources (% of total)(from 1990 to 2014)', fontsize=12)
plt.show()

# Characteristics of China
CH1 = df_final[df_final['Country Name'] == 'China']
CH1 = CH1.drop(['Country Name'], axis = 1)
CH1t = CH1.transpose()
CH1t = CH1t.rename(columns=CH1t.iloc[0]).drop(CH1t.index[0])
CH1t = CH1t.astype(float)
# Creating the Correlation Matrix 
CH1_corr=CH1t.corr(method='pearson')
# CH1_corr.style.background_gradient(cmap = 'Blues', axis = 1)

# plotting correlation heatmap
dataplot = sb.heatmap(CH1_corr, cmap="YlOrRd", annot=True)
  
# displaying heatmap
plt.show()

# Characteristics of Mexico
MX1 = df_final[df_final['Country Name'] == 'Mexico']
MX1 = MX1.drop(['Country Name'], axis = 1)
MX1t = MX1.transpose()
MX1t = MX1t.rename(columns=MX1t.iloc[0]).drop(MX1t.index[0])
MX1t = MX1t.astype(float)
# Creating the Correlation Matrix 
MX1_corr=MX1t.corr(method='pearson')
# MX1_corr.style.background_gradient(cmap = 'Blues', axis = 1)

# plotting correlation heatmap
dataplot = sb.heatmap(MX1_corr, cmap="YlOrBr", annot=True)
  
# displaying heatmap
plt.show()

# Population Growth 
df2_UP = df_final[df_final['Indicator Name']=='Urban population (% of total population)']
df2UP = df2_UP.drop(['Indicator Name'], axis = 1)
df2UP['% change'] = ((df[['1990', '2014']].pct_change(axis=1)['2014']) * 100).round(2).map(str) + '%'
df2UP[['Country Name','1990','1995','2000','2005','2010','2014','% change']]

