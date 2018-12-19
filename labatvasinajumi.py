import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import *
from matplotlib import pyplot as plt


def f(x):
    return sinh(sqrt(x))


x = linspace (0, 10, 20)

y = f(x)


#legend = []
#print(legend)


plt.axis([0, 10, 0, 10])
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Funkcija $sinh(sqrt(x))$ un tās atvasinajumi")
plt.plot(x, y, "k")


#legend.append("$sinh(sqrt(x))$ - default - viss ir savienots ar taisnam linijam")
#print(legend)


plt.plot(x, y, "ro")


#legend.append("$sinh(sqrt(x))$ - tikai dazi punkti")
#print(legend)


N = len(x)
deltax = x[1] - x[0]
atvasinajums = []

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i]))/deltax
    atvasinajums.append(temp)

plt.plot(x, atvasinajums, "y")
#legend.append("$sinh(sqrt(x))$ atvasinajums - viss ir savienots ar taisnam linijam")

plt.plot(x, atvasinajums, "go")
#legend.append("$sinh(sqrt(x))$ atvasinajums - dazi punkti")

N = len(atvasinajums)
deltax = atvasinajums[1] - atvasinajums[0]
atvasinajums2 = []

for i in range(N):
    temp = (f(atvasinajums[i] + deltax) - f(atvasinajums[i]))/deltax
    atvasinajums2.append(temp)

plt.plot(x, atvasinajums2, "m")
plt.plot(x, atvasinajums2, "bo")


#atvasinajumscaurmassivu = []
#for i in range(N-1):
    #temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    #atvasinajumscaurmassivu.append(temp)


#plt.plot(x[0:N-1], atvasinajumscaurmassivu, "m")
#legend. append("$sinh(sqrt(x))$ atvasinajums, izmantojot massiva vertibas - viss ir savienots ar taisnam linijam")
#plt.plot(x[0:N-1], atvasinajumscaurmassivu, "bo")
#legend. append("$sinh(sqrt(x))$ atvasinajums, izmantojot massiva vertibas - dazi punkti")


#plt.plot(0.680, 0.620, "ch", markersize = 10)


#print(plt.legend.__doc__)
#plt.legend(legend, loc = "lower left")
#plt.legend(legend, loc = 3, fancybox = True, framealpha = 0.5, facecolor = "orange")

plt.show()
