import numpy as np
import pandas
import statsmodels.api as sm


"""
In this question, you need to:
1) implement the compute_cost() and gradient_descent() procedures
2) Select features (in the predictions procedure) and make predictions.

"""


def predictions(weather_turnstile):
     # Select Features (try different features!)
    features = weather_turnstile[['rain', 'meandewpti', 'Hour', 'meantempi']]
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    features = features.join(dummy_units)
   
   #add weekday to DF
    days = pandas.get_dummies(weather_turnstile['weekday'], prefix='days')
    features = features.join(days)
        
    # Values
    values = weather_turnstile['ENTRIESn_hourly']

    
    model = sm.OLS(values,features)
    result = model.fit()
    prediction = np.dot(features, result.params)
    print result.params    
    return prediction



def compute_r_squared(data, predictions):
    
    mean=np.mean(data["ENTRIESn_hourly"])
    r_squared=1-np.sum((data["ENTRIESn_hourly"]-predictions)**2)/np.sum((data["ENTRIESn_hourly"]-mean)**2)
    return r_squared

weather = pandas.DataFrame.from_csv("C:/Users/Cault/Downloads/turnstile_data_master_with_weather.csv")
weather["weekday"]=pandas.DatetimeIndex(weather["DATEn"]).weekday


print compute_r_squared(weather,predictions(weather))