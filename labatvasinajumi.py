import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import *
from matplotlib import pyplot as plt


def f(x):
    return sinh(sqrt(x))


x = linspace (0, 10, 100)

y = f(x)



legend = []
#plt.axis([0, 10, 0, 10])
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Funkcija $sinh(sqrt(x))$ un tās atvasinājumi")
plt.plot(x, y, "k")

legend.append("$sinh(sqrt(x))$ - default - viss ir savienots ar taisnām linijam")

plt.plot(x, y, "ro")

legend.append("$sinh(sqrt(x))$ - tikai daži punkti")

N = len(x)

atvasinajumscaurmassivu = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    atvasinajumscaurmassivu.append(temp)

plt.plot(x[0:N-1], atvasinajumscaurmassivu, "m")
legend. append("$sinh(sqrt(x))$ atvasinājums, izmantojot massīva vertības - viss ir savienots ar taisnām līnijām")
plt.plot(x[0:N-1], atvasinajumscaurmassivu, "bo")
legend. append("$sinh(sqrt(x))$ atvasinājums, izmantojot massīva vertības - daži punkti")


atvasinajumscaurmassivu2 = []
for i in range(N-2):
    temp = (atvasinajumscaurmassivu[i+1] - atvasinajumscaurmassivu[i]) / (x[i+1] - x[i])
    atvasinajumscaurmassivu2.append(temp)

plt.plot(x[0:N-2], atvasinajumscaurmassivu2, "y")
legend. append("$sinh(sqrt(x))$ otrās kārtas atvasinājums, izmantojot massīva vertības - viss ir savienots ar taisnām līnijām")
plt.plot(x[0:N-2], atvasinajumscaurmassivu2, "go")
legend. append("$sinh(sqrt(x))$ otrās kārtas atvasinājums, izmantojot massīva vertības - daži punkti")



plt.legend(legend, loc = 3, fancybox = True, framealpha = 0.5, facecolor = "orange")
plt.show()
