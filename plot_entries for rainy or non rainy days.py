# -*- coding: utf-8 -*-
"""
Created on Mon Jan 05 14:46:59 2015

@author: a181990
"""


from pandas import *
from ggplot import *
turnstile_weather = pandas.DataFrame.from_csv("C:/Users/Cault/Downloads/turnstile_data_master_with_weather.csv")

def plot_weather_data(turnstile_weather):
    dfrain= turnstile_weather[turnstile_weather['rain']==1].reset_index()
    dfnorain= turnstile_weather[turnstile_weather['rain']==0].reset_index()
    
    plot_log_rain = ggplot(aes(x='ENTRIESn_hourly'),data=dfrain)  +\
            geom_histogram(binwidth=500,fill='blue') + ggtitle('Days with rain') + xlim(0,45000)+\
            scale_y_log10() + ylab("Nb of occurences")

    
    plot_log_nrain = ggplot(aes(x='ENTRIESn_hourly'),data=dfnorain)  +\
            geom_histogram(binwidth=500,fill='red') + ggtitle('Days with no rain') + xlim(0,45000)+\
            scale_y_log10()+ ylab("Nb of occurences")

    plot_rain = ggplot(aes(x='ENTRIESn_hourly'),data=dfrain)  +\
            geom_histogram(binwidth=100,fill='blue') + ggtitle('Days with rain') + xlim(0,5000)+\
            ylab("Nb of occurences") 

    
    plot_nrain = ggplot(aes(x='ENTRIESn_hourly'),data=dfnorain)  +\
            geom_histogram(binwidth=100,fill='red') + ggtitle('Days with no rain') + xlim(0,5000)+\
            ylab("Nb of occurences")


    return plot_log_rain, plot_log_nrain, plot_rain, plot_nrain
    
print plot_weather_data(turnstile_weather)