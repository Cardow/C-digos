
A , B ,  C = input().split()

A = float(A)
B = float(B)
C = float(C)

Numeros = [A, B, C]
Numeros.sort(reverse=True)

a = Numeros[0]
b = Numeros [1]
c = Numeros [2]

print (a)

if A>= B + C:
    print('NAO FORMA TRIANGULO')
elif A**2 == B**2 + C**2:
    print('TRIANGULO RETANGULO')
elif A**2 > B**2 + C**2:
    print('TRIANGULO OBTUSANGULO')
elif A**2 < B**2 + C**2:
    print('TRIANGULO ACUTANGULO')
elif A == B == C:
    print('TRIANGULO EQUILATERO') 
elif A == B and C!= A and C!= B or B == C and A!= C and A!= B or A == C and B!= A and B!= C:
    print('TRIANGULO ISOCELES')
