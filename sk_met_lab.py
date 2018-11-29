# -*- coding: utf-8 -*-
from math import *

def sinnh(x):
    k = 0
    a = sqrt(x)*(pow(x, 0))/(2*0+1)
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 500:
        k = k + 1
        R = x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        if k == 499:
            print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        elif k == 500:
            print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

    return S        

x = float(input("Ievadi argumentu X: "))
y = sinh(sqrt(x))
print("Sinh(sqrt(%.2f)) = %6.2f"%(x,y))

yy = sinnh(x)
print("                                                               ")
print("X pieder visiem skaitliem, kas lielaki par 0 lidz pat bezgalibai!")
print("                                                               ")
print("                           500                                       ")
print("                          _____                                      ")
print("                          \          k                              ")
print("                           \        x                               ")
print("        Sinh(sqrt(%.2f))"%(x) + " = >  ___________ * sqrt(x)            ")
print("                           /                                         ")
print("                          /____  (2*k+1)!                          ")
print("                           k=0                                       ")
print("                                                               ")
print("                                                               ")
print("                                 x                             ")
print("Rekurences reizinatajs:   ________________                     ")
print("                                                               ")
print("                           (2*k)*(2*k+1)                       ")


