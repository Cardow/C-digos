import math

x = int (input())
y = int(input())
e = math.e

S= 0
k = 1
limite = 10*3

for i in range(limite): 
    sin = math.sin(k*y)
    Si = ((e**k*x)*(sin))/k
    S += Si
    k += 2

print(S)





