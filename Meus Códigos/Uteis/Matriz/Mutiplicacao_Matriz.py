#Comprimento das matrizes

A = []
B = []
C = []

#Matriz A
m = int(input('Insira o numero de Linhas: ')) #ou len(A)
n = int(input('Insira o numero de Colunas: ')) # ou len(A[0])

for i in range(1, m+1):
    linhaA = []
    for j in range(1, n+1):
        num = int(input("Insira o numero A%ix%i: " %(i,j)))
        linhaA.append(num)
    A.append(linhaA)
    

#Matriz B
    
p = int(input('Insira o numero de Linhas: ')) #ou len(A)
q = int(input('Insira o numero de Colunas: ')) # ou len(A[0])

for i in range(1, p+1):
    linhaB = []
    for j in range(1, q+1):
        num = int(input("Insira o numero B%ix%i: " %(i,j)))
        linhaB.append(num)
    B.append(linhaB)

#Mutiplicacao A*B = C
    
for i in range(m):
        linhaC = []
        for j in range(q):
            linhaC.append(0)
        C.append(linhaC)

for i in range(m):
    for j in range(q):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

#Print
print ('A Mutiplicacao das matrizes:')

print('Matriz A: ')
for i in A:
    print (i)

print('Matriz B: ')
for i in B:
    print (i)

print('Resulta em:')
for i in C:
    print (i)
        