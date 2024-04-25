import nunpy

def multiplicacao(A,B):
    multiplicacao = nunpy.dot(A,B)
    print('Resultado Multiplicacao:')
    print(multiplicacao)

def soma(A,B):
    soma = nunpy.add(A,B)
    print('Resultado Soma: ')
    print(soma)

#Exemplo

A = nunpy.array([[1, 2, 3],[4, 5, 6]])
B = nunpy.array([[7, 8],[9, 10],[11, 12]])




