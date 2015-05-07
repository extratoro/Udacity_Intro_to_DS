import numpy as np
import pandas


"""
In this question, you need to:
1) implement the compute_cost() and gradient_descent() procedures
2) Select features (in the predictions procedure) and make predictions.

"""

def normalize_features(array):
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta): 
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    m = len(values)
    cost_history = []
    for i in range(num_iterations):
        pred=np.dot(features,theta)
        theta=theta+(alpha/m)*np.dot(values-pred,features)
        cost_history.append(compute_cost(features, values, theta))
    return theta, pandas.Series(cost_history)

def predictions(dataframe):

    # Select Features (try different features!)
    features = dataframe[['rain', 'meandewpti', 'Hour', 'meantempi']]
    
    #add weekday to DF
    days = pandas.get_dummies(weather_turnstile['weekday'], prefix='days')
    features = features.join(days)    
    
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    

    
    # Values
    values = dataframe['ENTRIESn_hourly']
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)

    # Set values for alpha, number of iterations.
    alpha = 0.1 # please feel free to change this value
    num_iterations = 100 # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    
    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    #plot = plot_cost_history(alpha, cost_history)

    
    predictions = np.dot(features_array, theta_gradient_descent)
    #print plot
    print features.head()
    print theta_gradient_descent[:12]
    return predictions, plot


def plot_cost_history(alpha, cost_history):
   """This function is for viewing the plot of your cost history.
   You can run it by uncommenting this

       plot_cost_history(alpha, cost_history) 

   call in predictions.
   
   If you want to run this locally, you should print the return value
   from this function.
   """
   cost_df = pandas.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
      geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )



def compute_r_squared(data, predictions):
    
    mean=np.mean(data["ENTRIESn_hourly"])
    r_squared=1-np.sum((data["ENTRIESn_hourly"]-predictions)**2)/np.sum((data["ENTRIESn_hourly"]-mean)**2)
    return r_squared

weather = pandas.DataFrame.from_csv("C:/Users/Cault/Downloads/turnstile_data_master_with_weather.csv")
weather["weekday"]=pandas.DatetimeIndex(weather["DATEn"]).weekday


print compute_r_squared(weather,predictions(weather)[0])