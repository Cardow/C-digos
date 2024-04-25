import math

def Problema1():

    pass

def Problema2():
    #nao sei oq eu fiz aqui ta
    def mdc(x,y):
        while y!= 0:
            t = y
            y = x%y
            x = t
        return x


    limite = 10**7
    for i in (2, limite+1):
        for j in (2, limite +1):
            for h in range(2, int(j**0.5 +1)):
                if j%h and i%h:
                    coprimo = True
                if coprimo:
                    print('%i,%i' %(i,j))

def Problema3():
    def primo(x):
        for i in range(2, int(x**0.5 +1)):
            if x % i == 0:
                return False
        return True
    
    limite = 10*7
    primo1 = 2
    primo2 = 0

    for i in range(3, limite + 1):
        if primo(i):
            primo2 = i
            An = math.sqrt(primo2) - math.sqrt(primo1)>= 1
            if An >= 1:
                print('%i,%i' %(primo1, primo2)) 
            primo1 = i


def Problema4():
    #Exemplo Suponha que A = {46, 69, 32, 60, 52, 41}
    #Suponha que P = {48, 70, 34, 62, 54, 42}
    A = [46, 69, 32, 60, 52, 41]
    x = P = [48, 70, 34, 62, 54, 42]
    n = len(P)
    m = len(A)

#Media de P
    SiP1 = 0
    SomaP1 = 0
    for i in range(n):
        SiP1 = x[i]/n
        SomaP1 += SiP1
    print('Media da populacao:', SomaP1)
#Variancia de P
    SiP2 = 0
    SomaP2 = 0
    for i in range(n):
        SiP2 = ((x[i]-SomaP1)**2)/n
        SomaP2 += SiP2
    print('Variancia da populacao:', SomaP2)
#Desvio padrao de P
    SomaP3 = math.sqrt(SomaP2)
    print('Desvio padrao da populacao:', SomaP3)
#Coeficiente de variacao de P
    SomaP4 = (SomaP3/SomaP1)*100
    print('Coeficiente de variacao da populacao: ', SomaP4)

#Media de A
    SiA1 = 0
    SomaA1 = 0
    for i in range(n):
        SiA1 = x[i]/n
        SomaA1 += SiA1
    print('Media da Amostra:', SomaA1)
#Variancia de A
    SiA2 = 0
    SomaA2 = 0
    for i in range(n):
        SiA2 = ((x[i]-SomaA1)**2)/n
        SomaA2 += SiA2
    print('Variancia da Amostra:', SomaA2)
#Desvio padrao de A
    SomaA3 = math.sqrt(SomaA2)
    print('Desvio padrao da Amostra:', SomaA3)
#Coeficiente de variacao de A
    SomaA4 = (SomaA3/SomaA1)*100
    print('Coeficiente de variacao da Amostra: ', SomaA4)



    
def main():
    #Problema1()
    #Problema2()
    #Problema3()
    Problema4()
    
if __name__ == '__main__':
    main()

'''
 A = [46, 69, 32, 60, 52, 41] #conjunto usado no Exemplo da Apostila
    P = [28, 41, 50, 60, 64, 52, 11, 32, 55, 46, 74, 69] #P contém A
'''
