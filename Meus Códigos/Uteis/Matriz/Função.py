def Soma_matriz(A,B):


    resultado = []

    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            num = A[i][j] + B[i][j]
            linha.append(num)
        resultado.append(linha)

    print ('A soma das matrizes é:')

    for i in resultado:
        print (i)

def Mutiplicacao(A, B): 
    
    resultado = []
    for i in range(len(A)):
        linhas = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            linhas.append(total)
        resultado.append(linhas)


    #Print
                
    print ('A Mutiplicacao das matrizes:')
    print('Matriz A: ')
    for i in A:
        print (i)
    print('Matriz B: ')
    for i in B:
        print (i)
    print('Resulta em:')
    for i in resultado:
        print (i)
            











