import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

data = pd.read_csv('database/diabetes.csv')
data.shape()
data.describe()
data.info()
# data does not contain any null values
data.isnull().sum()
g = sns.pairplot(data, hue="Outcome")
g.fig.suptitle("Scatterplot and histogram of pairs of variables color coded by Outcome", 
               fontsize = 14, # defining the size of the title
               y=1.05);

# feature columns
x = data.drop(['Outcome'], axis=1)
# taget column
y = data['Outcome']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
from sklearn.ensemble import RandomForestClassifier

rforest = RandomForestClassifier(random_state = 25,oob_score=True)
rforest.fit(X_train, y_train)
y_pred = rforest.predict(X_test)

#print(y_pred)

# out of bag score
print(rforest.oob_score_)

import numpy as np
from sklearn.metrics import accuracy_score 
accuracy_score(y_test, y_pred)
