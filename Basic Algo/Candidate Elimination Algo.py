import pandas as pd
import numpy as np

datapd = pd.read_csv('database/data.csv')

# getting sample data to numpy
numpy_data = np.array(datapd.iloc[:])
numpy_data
col_ins = 6
# General Hypothesis
g_hypo = np.array([['?']*col_ins]*col_ins)
g_hypo

# Specific  Hypothesis
s_hypo = np.array([None]*col_ins)
s_hypo

def getSHypo(row):
    for i in range(0, col_ins):
        if (s_hypo[i] == None):
            s_hypo[i] = row[i]
        elif (s_hypo[i] == row[i]):
            pass
        else:
            s_hypo[i] = '?'
            print(s_hypo)
def getGHypo(row):
    for x in range(col_ins):
        if row[x] != s_hypo[x]:
            g_hypo[x][x] = s_hypo[x]
        else:
            g_hypo[x][x] = '?'
            print(g_hypo)

for row in numpy_data:
    if (row[-1] == 'Yes'):
        getSHypo(row)
    else:
        getGHypo(row)

print("Most General Hypothesis : "+'\n',g_hypo)

print("Most Specific Hypothesis : "+'\n',s_hypo)
## dataset with good numbers of entitys and features

datapd2 = pd.read_csv('database/data2.csv')

# extracting required data
numpydata2 = np.array(datapd2.iloc[:,6::])
numpydata2
col_ins = 4

# General Hypothesis
g_hypo = np.array([['?']*col_ins]*col_ins)
g_hypo

# Specific  Hypothesis
s_hypo = np.array([None]*col_ins)
s_hypo
for row in numpydata2:
    if (row[-1] == 1):
        getSHypo(row)
    else:
        getGHypo(row)

print("Most General Hypothesis : "+'\n',g_hypo)
print("Most Specific Hypothesis : "+'\n',s_hypo)
