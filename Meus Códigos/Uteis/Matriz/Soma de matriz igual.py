#Comprimento das matrizes


m = int(input('Insira o numero de Linhas: ')) #ou len(A)
n = int(input('Insira o numero de Colunas: ')) # ou len(A[0])


A = []
B = []
C = []

#Matriz A
for i in range(1, m+1):
    linhaA = []
    for j in range(1, n+1):
        num = int(input("Insira o numero A%ix%i: " %(i,j)))
        linhaA.append(num)
    A.append(linhaA)
    

#Matriz B
for i in range(1, m+1):
    linhaB = []
    for j in range(1, n+1):
        num = int(input("Insira o numero B%ix%i: " %(i,j)))
        linhaB.append(num)
    B.append(linhaB)

#Soma das matrizes A+B = C
    
for i in range(0, m):
    linhaC = []
    for j in range(0, n):
        num = A[i][j] + B[i][j]
        linhaC.append(num)
    C.append(linhaC)

#Print

print ('A soma das matrizes é:')
for i in C:
    print (i)
        










