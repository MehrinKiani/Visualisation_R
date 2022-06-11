# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:03:55 2020

@author: Mehrin Kiani
"""
#%% import libraries
import plotly
import plotly.graph_objects as go
from plotly.offline import plot
import plotly.express as px
import numpy as np 
import pandas 
import matplotlib as plt

#%% Load the data
all_data = pandas.read_csv('WHO-COVID-19-global-data.csv')  
#all_data['date'] = pandas.to_datetime(all_data['Date_reported'])  
data_1July2020 = all_data.loc[all_data.Date_reported == '2020-07-01']
data_1July2020 = data_1July2020.rename({' Country': 'country', ' Cumulative_cases': 'all_cases', ' Cumulative_deaths':'all_deaths'}, axis=1)
#%%
fig = go.Figure(go.Scattergeo())
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
plot(fig, filename='worldmap')

#%%
world_data = px.data.gapminder().query("year==2007")
# fig = px.scatter_geo(world_data, locations="iso_alpha", color="continent",
#                      hover_name="country", size="pop",
#                      projection="natural earth")
# plot(fig, filename='worldmap')

#%%
world_data['country'] = world_data.country.astype('category')
data_1July2020['country'] = data_1July2020.country.astype('category')
#pd.merge(left, right, how='left', on=['key1', 'key2'])
merge_country_covid = pandas.merge(left=world_data,
                     right=data_1July2020,
                     how='left',
                     on=('country'))
                     
#%%new_large
#fig1 = go.Figure(go.Scattergeo())
#fig1.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig1 = px.scatter_geo(merge_country_covid, locations="iso_alpha", color="continent",
                     hover_name="country", size="all_cases",
                     projection="natural earth")
plot(fig1, filename='worldmap1')
