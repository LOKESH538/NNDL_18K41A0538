from sympy import * 
import sympy as sym
x, y = symbols('x y')
diff_x=sym.diff(x**2+y**2+10,x)
y=sym.Symbol('y')
diff_y=sym.diff(x**2+y**2+10,y)

f = lambda x1,y1: x1**2+y1**2+10

print("The gradient/slope/first order derivative of given function for x is : ",diff_x)
print("The gradient/slope/first order derivative of given function for y is : ",diff_y)

x_is=-1
y_is=1
n=0.1
epoches=20
i=1
while(i<epoches):
    value_of_x=diff_x.subs(x,x_is)
    value_of_y=diff_y.subs(y,y_is)
    cx=-n*(value_of_x)
    cy=-n*(value_of_y)
    x_is=x_is+cx
    y_is=y_is+cy
    i=i+1
    if(i>epoches):
        break

print("The global minimum point of given function is at x =", round(x_is))
print("The global minimum point of given function is at y =", round(y_is))
print("The value of the function at minimum point is {}".format(round(f(x_is,y_is))))
