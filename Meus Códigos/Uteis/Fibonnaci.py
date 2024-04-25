

#Fibonnaci

def Fibonnaci(termos):
    x = 0
    y = 1
    print(x)
    print(y)
    for i in range(0, termos):
        z = x+y
        print(z)
        x = y
        y = z


#Teste
numero = int(input())
Fibonnaci(numero)








