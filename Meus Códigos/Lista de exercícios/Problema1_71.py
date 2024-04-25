
import math as mp

x = int(input())
n = 0
S = 0
limite = 10**3

for i in range(limite):
    cima = (mp.factorial(3*n))*(-1**n)*(x**(2*n))
    baixo = ((mp.factorial(n))*(mp.factorial(3*n)))**3
    Si = cima/baixo
    n+= 1

print(S)




