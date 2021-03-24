import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split
import seaborn as sns
from scipy import stats

print("----------------Read Data-----------------")

data=pd.read_excel("unioncarbide.xls")
print(data.head())

data.info()

print("----------------Outliers-----------------")

z=np.abs(stats.zscore(data))
print(z)

print(sns.boxplot(x=data['X']))

print(sns.boxplot(y=data['Y']))

f_data=data[(z<3).all(axis=1)]
print(f_data.head())

df=data
for i in df:
  q=df[i].quantile(0.99)
  df[df[i]<q]
  q_low=df[i].quantile(0.01)
  q_hi=df[i].quantile(0.99)
  df_filtered=df[(df[i]<q_hi)&(df[i]>q_low)]
print(df_filtered.head())

data=df_filtered
print(len(data))
print(len(df_filtered))
if(len(data)==len(df_filtered)):
  print('No outliers')

print("----------------Normalisation-----------------")

data_n=data.copy()
data_n=(data_n-data_n.min())/(data_n.max()-data_n.min())
print(data_n.head())


print("----------------Split Data-----------------")

train_data,test_data=train_test_split(data_n,test_size=0.1)

print(len(train_data))
print(train_data.head())

x=np.array(train_data['X'])
y=np.array(train_data['Y'])

print("----------------Train Data-----------------")

m=1
c=-1
l=0.1   # learning rate
d_m=1
d_c=1
err=[]
epochs=100  #epochs
def derive(m,c,x,y):
  m_d=-1*(y-m*x-c)*x
  c_d=-1*(y-m*x-c)
  return m_d,c_d
for i in range(epochs):
  er=0
  for j in range(len(x)):
    er+=((y[j]-(m*x[j])-c))**2
    pm=m
    pc=c
    d_m,d_c=derive(pm,pc,x[j],y[j])
    d_m=-l*d_m
    d_c=-l*d_c
    m=m+d_m  #Gradiant descent
    c=c+d_c  #Gradiant descent
    er=(1/(2*len(train_data['X'])))*(er)
    err.append(er)
print("The local minimum occurs at m = %.2f"%(m),", c = %.2f"%(c))

print("----------------RMSE for Training data-----------------")

train_data_pred=m*train_data['X']+c

yp=[]
for i in range(len(x)):
  p=(m*x[i])+c
  yp.append(p)
print("Predicted values (yp) : ",yp)

sum=0
for i in range(len(x)):
  sum+=(y[i]-yp[i])**2
  mse=sum/len(x)
print("Mean Square Error (MSE) : ",mse)

plt.plot(np.array(train_data['X']),np.array(train_data_pred),'green')
plt.scatter(np.array(train_data['X']),np.array(train_data['Y']),color='red')
plt.title("Predicted data vs Actual data")

iters=np.arange(epochs*len(x))
plt.plot(iters,err,'green')
plt.title("Error graph for training data")
plt.xlabel("iteration count")
plt.ylabel("error")
plt.grid()

print("----------------Test data-----------------")

x1=np.array(test_data['X'])
y1=np.array(test_data['Y'])

test_data_pred=m*test_data['X']+c
print(test_data_pred)

yp1=[]
for i in range(len(x1)):
  p1=(m*x1[i])+c
  yp1.append(p1)
print("Test data predicted values : ",yp1)

sum=0
for i in range(len(x1)):
  sum+=(y1[i]-yp1[i])**2
  mse1=sum/len(x1)
print("Mean Square Error (MSE) : ",mse1)

plt.scatter(test_data['X'],test_data['Y'],color='red')
plt.plot(test_data['X'],test_data_pred,'green')
plt.grid()

x_min=data['X'].min()
x_max=data['X'].max()
y_min=data['Y'].min()
y_max=data['Y'].max()

x2=float(input("Enter pH value of well water :"))
xi=(x2-x_min)/(x_max-x_min)
yi=m*xi+c
yi=yi*(y_max-y_min)+y_min
print("Bicarbonates of well water based on its pH {} is : {}".format(x2,yi))
