import pandas as pd
import numpy as np
df = pd.read_csv('E:/Projects/Python/PNMS/database/diabetes.csv')
df.head()
df.shape
df.describe()
df.info()
df.isnull().sum()
# feature columns
x = np.array(df.drop(['Outcome'], axis=1))
# taget column
y = np.array(df['Outcome'])
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=20)
model = LinearRegression().fit(X_train,y_train)
r_sq = model.score(X_train, y_train)

print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"coefficients: {model.coef_}")

y_pred = model.predict(X_test)
print(f"predicted response:\n{y_pred}")
# model accuray
from sklearn import metrics
print(1-(metrics.explained_variance_score(y_test, y_pred)))
