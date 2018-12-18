import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from matplotlib import pyplot as plt
from numpy import *
from time import sleep

def f(x):
    return sinh(sqrt(x))

a = 0
b = 10

funa = f(a)
funb = f(b)

if (funa * funb > 0.0):
    print("Dotaja intervaala [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()
else:
    print("Dotaja intervala sakne(s) ir!")

deltax = 0.000001

k = 0
while ((b-a)>deltax):
    k = k+1
    x = (a+b)/2
    funx = f(x)
    
    if (funa*funx==0):
        b = x
    else:
        a = x
        

print("Sakne ir: ", x)
y = sinh(sqrt(x))
print("Funkcijas vērtība: ", y)
print("Iterāciju skaits: ", k)

x1 = linspace(0, 10, 80)      
y1 = sinh(sqrt(x1))    
plt.grid()
plt.plot(x1, y1)
plt.show()
