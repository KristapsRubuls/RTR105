import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from math import *
from numpy import *
from matplotlib import pyplot as plt
x = linspace(0, 4, 70)
y1 = sin(x)
y2 = x
y3 = x - (x*x*x)/(1*2*3)
y4 = x - (x**3)/(1*2*3) + (x**5)/(1*2*3*4*5)
y5 = x - (x**3)/(1*2*3) + (x**5)/(1*2*3*4*5) - (x**7)/(1*2*3*4*5*6*7)
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Funkcija $sin(x)$ un tās izvirzījumi rindā")
plt.plot(x, y1)
plt.plot(x, y1, color = "#0FFFF0")
plt.plot(x, y2)
plt.plot(x, y2, color = "#00FF00")
plt.plot(x, y3)
plt.plot(x, y3, color = "#0000FF")
plt.plot(x, y4)
plt.plot(x, y4, color = "#FF0000")
plt.plot(x, y5)
plt.plot(x, y5, color = "#FFFF00")
plt.show()

