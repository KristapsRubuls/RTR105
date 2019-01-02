import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import*
from matplotlib import pyplot as plt


def f(x):
    return sinh(sqrt(x))

x = linspace(0, 10, 1000)
y = f(x)

N = 1000
a = 0
b = 10
c = 12

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcija un taas integraalis (laukums starp funkciju un x ass)')

plt.plot(x,y)

x1 = random.uniform(a,b,N)
y1 = random.uniform(a,c,N)

N1 = 0
for i in range(N):
    if y1[i] < f(x1[i]):
        plt.plot(x1[i],y1[i],'go')
        N1 = N1 + 1
    else:
        plt.plot(x1[i],y1[i],'ro')


S_zinaamais = (b-a) * (b-a)
S_nezinaamais = 1. * S_zinaamais * N1 / N
print(S_nezinaamais)


plt.show()
