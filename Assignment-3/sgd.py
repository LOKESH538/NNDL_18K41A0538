from sympy import Symbol, Derivative, symbols
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

m= Symbol('m')
c= Symbol('c')
function = '0.5*(y-m*x-c)**2'
partialderivative= Derivative(function, m)
dfm = partialderivative.doit()
partialderivative= Derivative(function, c)
dfc = partialderivative.doit()
xa = [0.2,0.4,0.6,0.8,1.0,1.2]
ya = [2.4,3.8,4.2,4.6,5.0,5.4]
m1 = -1.0 
c1 = 1.0  
itr = 100  
learningrate = 0.1
for i in range(0,itr):
    for j in range(0,len(xa)):
        m = symbols('m')
        c = symbols('c')
        x = symbols('x')
        y = symbols('y')
        dfmv = dfm.subs(m, m1) 
        dfmv = dfmv.subs(c, c1) 
        dfmv = dfmv.subs(x, xa[j]) 
        dfmv = dfmv.subs(y, ya[j]) 
        dfmv = round(dfmv,2)
        dfcv = dfc.subs(c, c1) 
        dfcv = dfcv.subs(m, m1) 
        dfcv = dfcv.subs(x, xa[j]) 
        dfcv = dfcv.subs(y, ya[j]) 
        dfcv = round(dfcv,2)
        dm = (-1.0)*learningrate*dfmv
        dc = (-1.0)*learningrate*dfcv
        m1 = m1 + dm
        m1 = round(m1, 2) 
        c1 = c1 + dc
        c1 = round(c1, 2)
print(m1, c1)
print(f'minimum value obtained at m = {m1} ,c ={c1}')

x = np.linspace(-5,5,100)
y = m1*x+c1
plt.plot(x, y, '-r', label='y='+str(m1)+'x+'+str(c1))
plt.title('Graph of '+'y='+str(m1)+'x+'+str(c1))
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()

data_pred = []
for i in xa:
    data_pred.append(m1*i+c1)
mse = mean_squared_error(ya,data_pred)
print(f"mean square error : {mse}")
