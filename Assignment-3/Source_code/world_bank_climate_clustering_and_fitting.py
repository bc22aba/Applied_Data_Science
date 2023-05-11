# -*- coding: utf-8 -*-
"""World Bank climate Clustering and fitting.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/122y8bdrhVTDKmYWkv5NchWvQyXO8r1TE
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.optimize import curve_fit
from scipy import stats
from errors import err_ranges

# function to read CSV dataset 
def Read_GetData():
    return pd.read_csv("..\Dataset\API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5447781.csv",\
skiprows=4)

'''Main Function Definition'''
def MainFunction():
    # Load climate change data from World Bank API
    '''Read CSV and get data'''
    climate_data = Read_GetData()

    # Remove unnecessary columns
    climate_data = climate_data.drop(columns=['Country Code', \
'Indicator Name', 'Indicator Code','Unnamed: 66'])
    # Transpose the data so that each country is a row and each year is a column
    climate_data = climate_data.set_index('Country Name')

    # Remove rows with missing data
    climate_data = climate_data.dropna()

    # Convert all values to floats
    climate_data = climate_data.astype(float)

    # Normalize the data
    scaler = StandardScaler()
    climate_data_norm = scaler.fit_transform(climate_data)

    # Perform K-means clustering with 4 clusters
    kmeans = KMeans(n_clusters=4, random_state=42).fit(climate_data_norm)

    # Add the cluster labels as a new column to the original data
    climate_data['cluster'] = kmeans.labels_

    # Plot the data colored by cluster membership and with cluster centers marked
    sns.scatterplot(x='2000', y='2016', hue='cluster', data=climate_data)
    sns.scatterplot(x=kmeans.cluster_centers_[:, 16], \
    y=kmeans.cluster_centers_[:, 0], color='black', marker='x', s=200)
    plt.xlabel('CO2 emissions per capita (metric tons)')
    plt.ylabel('CO2 emissions per capita (metric tons)')
    plt.title('K-means clustering of CO2 emissions data')
    plt.show()
    '''
    #  .
    > Create simple model(s) fitting data sets with curve_fit. This could \
    be fits of time series, but also, say, one attribute as a function of \
    another. Keep the model simple.
    (e.g., exponential growth, logistic function, low order polynomials). \
    Use the model for predictions, e.g. values in ten or twenty years time \
    including confidence ranges. Use the attached function err_ranges to \
    estimate lower and upper limits of the confidence range and produce a plot \
    showing the best fitting function and the confidence range.
    '''
    # Extract CO2 emissions per capita data for the United States
    us_co2 = climate_data.loc['United States'][2:-1]

    # Plot the data
    years = np.arange(1960, 2020)
    plt.plot(years, us_co2)
    plt.xlabel('Year')
    plt.ylabel('CO2 emissions per capita (metric tons)')
    plt.title('CO2 emissions per capita in the United States')
    plt.show()

    # Convert all values to floats
    climate_data = climate_data.astype(float)

    # Select the data for a specific country
    country_data = climate_data.loc['United States']

    # Extract the years and GDP per capita values
    years = country_data.astype(int)
    gdp_per_capita = country_data.values

    # Define the polynomial function
    def polynomial(x, a, b, c):
        return a * x**2 + b * x + c

    # Fit the model to the data
    popt, pcov = curve_fit(polynomial, years, gdp_per_capita)

    # Define the function for predictions
    def predict_polynomial(x):
        return polynomial(x, *popt)

    # Make predictions for future years
    future_years = np.arange(2022, 2041)
    predicted_values = predict_polynomial(future_years)

    errs = err_ranges(years, polynomial, popt, 1.96 * np.sqrt(np.diag(pcov)))

    lower_bounds = predict_polynomial(years) - errs[0]
    upper_bounds = predict_polynomial(years) + errs[1]

    # Plot the original data, the best fitting function, and the confidence range
    plt.plot(years, gdp_per_capita, 'bo', label='Data')
    plt.plot(future_years, predicted_values, 'r-', \
label='Best Fitting Function')
    plt.fill_between(years, lower_bounds, upper_bounds, color='gray', \
alpha=0.3, label='Confidence Range')
    plt.xlabel('Year')
    plt.ylabel('GDP per capita')
    plt.title('Polynomial Fit to GDP per capita')
    plt.legend()
    plt.show()

    # Assuming you have performed the clustering analysis and added the cluster \
    # labels as a new column 'cluster' in the climate_data dataframe

    # Separate the data by clusters
    clusters = climate_data.groupby('cluster')

    # Iterate over each cluster
    for cluster_label, cluster_data in clusters:
        print(f"Cluster {cluster_label}:")
    
        # Get the list of countries in the cluster
        countries = cluster_data.index.tolist()
        print("Countries:", countries)
    
        # Plot the trends for each country in the cluster
        for country in countries:
            data = cluster_data.loc[country]
            plt.plot(data.index, data.values, label=country)
    
        plt.xlabel('Year')
        plt.ylabel('CO2 emissions per capita')
        plt.title(f'Cluster {cluster_label} - Trends of CO2 emissions per capita')
        plt.legend()
        plt.show()

    # Compare trends between different clusters
    cluster1_data = clusters.get_group(1)
    cluster2_data = clusters.get_group(2)

    # Plot the trends for a few countries from each cluster
    countries_cluster1 = cluster1_data.sample(n=3).index.tolist()
    countries_cluster2 = cluster2_data.sample(n=3).index.tolist()

    plt.figure(figsize=(10, 5))
    for country in countries_cluster1:
        data = cluster1_data.loc[country]
        plt.plot(data.index, data.values, label=f'Cluster 1: {country}')

    for country in countries_cluster2:
        data = cluster2_data.loc[country]
        plt.plot(data.index, data.values, label=f'Cluster 2: {country}')

    plt.xlabel('Year')
    plt.ylabel('CO2 emissions per capita')
    plt.title('Comparison of CO2 emissions per capita between clusters')
    plt.legend()
    plt.show()
    
'''Main Funtion Calling'''
MainFunction()