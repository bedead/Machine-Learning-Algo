import pandas as pd

## getting input from csv
data = pd.read_csv('E:/Projects/Python/PNMS/database/data.csv')

# converting data to nested list
# we could use numpy also here
a = []
for i in range(0, 4):
    a.append(list(data.loc[i]))
a

col_instance = 6
h = [0]*col_instance
h
# find S algo
for j in range(0, 4):
    if (a[j][-1] == 'Yes'):
        for i in range(0, col_instance):
            if (h[i] == 0):
                h[i] = a[j][i]
            elif(h[i] == a[j][i]):
                pass
                print(h)
            else:
                h[i] = '?'
                print(h)

## dataset with good numbers of entitys and features
data2 = pd.read_csv('E:/Projects/Python/PNMS/database/data2.csv')

# extracting required data from dataset
data2 = data2.loc[:,['Hulu','Netflix','Prime Video','Disney+','Type']]
b = []
for i in range(0, len(data2)):
    b.append(list(data2.loc[i]))

col_instance = 4
h_lis = [0]*col_instance
h_lis
# find S algo
for j in range(0, len(data2)):
    if (b[j][-1] == 1):
        for i in range(0, col_instance):
            if (h_lis[i] == 0):
                h_lis[i] = b[j][i]
            elif(h_lis[i] == b[j][i]):
                pass
                print(h_lis)
            else:
                h_lis[i] = '?'
                print(h_lis)
