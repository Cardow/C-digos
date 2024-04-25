#Numero de Euler

import math as mp

k = 1
S = 0

limite = 10**3

for i in range (limite):
    Si = 1/mp.factorial(k -1)
    S += Si
    k += 1

print(S)




