import numpy as np
import pandas as pd

df = pd.read_csv('database/diabetes.csv')
df.head(2)
# getting all the features in x and all targets in y
x = df[df.columns[:-1]]
y = df[df.columns[-1]]
# function to return a value between 0 to 1

def findSigmoid(data):
    return 1/(1+np.exp(-data))
parameters = {}
parameters["weight"] = np.zeros(x.shape[1])
parameters['bias'] = 0
parameters

def optimize(x, y, learn_rate, iterVal, parameters):
    size = x.shape[0]
    weight = parameters['weight']
    bias = parameters['bias']
    
    for each in range(iterVal):
        sigma = findSigmoid(np.dot(x, weight) + bias)
        lossval = -1/size * np.sum(y *np.log(sigma)) + (1-y)*np.log(1-sigma)
        
        dW = 1/size * np.dot(x.T, (sigma - y))
        db = 1/size * np.sum(sigma - y)
        weight -= learn_rate*dW
        bias -= learn_rate*db
        
        parameters['weight'] = weight
        parameters['bias'] = bias
        return parameters

def train(x, y, learn_rate, iterVal):
    parameters_out = optimize(x, y, learn_rate, iterVal, parameters)
    
    return parameters_out

parameters_out = train(x,y,learn_rate=0.02,iterVal=500)
parameters_out

output = np.dot(x[:5], parameters_out['weight']) + parameters_out['bias']
predictions = findSigmoid(output) >= 1/2
predictions
# values with True are classified as diabetic
