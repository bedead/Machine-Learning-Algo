import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('E:/Projects/Python/PNMS/database/diabetes.csv')
df.head()
df.info()
df.describe()
df.dropna()

x = df.drop(['Outcome'], axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=200)

model = SVC(kernel='linear')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)

print(accuracy_score(y_test, y_pred))
