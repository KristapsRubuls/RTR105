# -*- coding: utf-8 -*-
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from matplotlib import pyplot as plt
from math import *
from numpy import *


def f(x):
    return sin(x)

a = 1.1
b = 3.2

funa = f(a)
funb = f(b)

if (funa * funb > 0.0):
    print("Dotajaa intervaalaa [%s,%s] saknju nav"%(a,b))
    sleep(1); exit()
else:
    print("Dotajaa intervaalaa sakne(s) ir!")

deltax = 0.01

k = 0
while ( fabs(b - a) > deltax ):
    k = k+1
    x = (a + b)/2; funx = f(x)
    if( funa*funx < 0.0):
        b = x
    else:
        a = x

print("Sakne ir: ", x)
y = sin(x)
print("Dotaas funkcijas veertiiba sajaa punktaa ir: ", y)
print("nepieciešamo iterāciju skaits intervālu dalīšanai uz pusēm: k = ", k)

x1 = linspace(0, 4, 80)
y1 = sin(x1)    
plt.grid()
plt.plot(x1, y1)
plt.show()
