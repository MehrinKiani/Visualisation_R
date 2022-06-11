# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:27:42 2020

@author: Mehrin Kiani
"""
# %% import libraries
import plotly
import numpy as np 
import pandas 
import geopandas
import matplotlib as plt
#%% Load the data
all_data = pandas.read_csv('WHO-COVID-19-global-data.csv')  

#%%
all_data['date'] = pandas.to_datetime(all_data['Date_reported'])  
data_1July2020 = all_data.loc[all_data.Date_reported == '2020-07-01']

#%%
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
world.boundary.plot();
#%%
centroids = world.copy()
centroids['size'] = centroids['pop_est'] /  1000000  # to get reasonable plotable number
#centroids.geometry = world.centroid
#%%
ax = world.plot(facecolor='w', edgecolor='k')
#%%
centroids.plot(markersize='size', ax=ax)
#%%
