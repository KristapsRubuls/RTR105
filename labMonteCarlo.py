import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from math import*
from numpy import sinh, linspace, sqrt, random
from matplotlib import pyplot as plt

N = 1000
a = 0
b = 5

#pseido-gadiijuma skaitlju generatora grauds
#random.seed(1)

x = linspace(0, 5, 1000)
y = sinh(sqrt(x))

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcija un taas integraalis (laukums starp funkciju un x ass)')
#nav jeegas ziimeet shaadi plt.plot(x,y)
plt.plot(x,y)


x1 = random.uniform(a,b,N)

y1 = random.uniform(a,b,N)


N1 = 0
for i in range(N):
    if y1[i] < y[i]:
        plt.plot(x1[i],y1[i],'go')
        N1 = N1 + 1
    else:
        plt.plot(x1[i],y1[i],'ro')

#S_zinaamais = (b-a) * (b-a)
#S_nezinaamais = 1. * S_zinaamais * N1 / N
#print(S_nezinaamais)

plt.show()
