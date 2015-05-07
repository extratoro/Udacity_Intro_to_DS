# -*- coding: utf-8 -*-
"""
Created on Mon Jan 05 14:46:59 2015

@author: a181990
"""


from pandas import *
from ggplot import *
turnstile_weather = pandas.DataFrame.from_csv("C:/Users/Cault/Downloads/turnstile_data_master_with_weather.csv")


def plot_weather_data(turnstile_weather):
    mod = DataFrame({'ENTRIES' : turnstile_weather.groupby(['Hour'])['ENTRIESn_hourly'].mean()}).reset_index()
 
    plot = ggplot(aes(x='Hour',y='Avg ENTRIES'),data=mod)  + geom_point()+\
                  geom_line(color='blue') +\
                  xlim(0,24) +ylim(0,) +\
            ggtitle("Ridership by hours")

    return plot
    

print plot_weather_data(turnstile_weather)