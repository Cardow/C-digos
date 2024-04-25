import math

def Problema1(limite):
    def primo(x):
        for i in range(2, int(x**0.5 +1)):
            if x % i == 0:
                return False
        return True

    def C(x):
        y = 0
        for i in range(2, x+1):
            if primo(i):
                y += 1
        return y

    #Comecando pelo 3 pois 2<= n <= 100 e p2 = 3
    primo1 = 3
    print('Problema 1:')
    for i in range(4, limite + 1):
        if primo(i):
            primo2 = i
            Cprimo1 = C(primo1**2)
            Cprimo2 = C(primo2**2)
            if Cprimo2 - Cprimo1 < 4:
                print ('Problema 1: (%i,%i)' %(primo2, primo1))
            primo1 = i


def Problema2(linhas):
    def num_Pascal(n, p): #C(n/p) = n!/p!(n-p)!

        #Linha 0 = 1 o ultimo de cada linha =1
        if p == 0  or p == n:
            return 1
        else:
            valor = math.factorial(n) // (math.factorial(p) * math.factorial(n - p))
            return valor

    soma = 0
    for n in range(0,linhas):
        for p in range (0, n + 1):
            resultado = num_Pascal(n, p)
            if resultado % 2 != 0:
                
                soma += 1

    print('Problema 2:', soma)


def Problema3(termos):
    def primo(x):
        for i in range(2, int(x**0.5 +1)):
            if x % i == 0:
                return False
        return True

    Numero_termos = 0
    soma = 0
    n = 2 #n1 nao e primo ja pula pro n2
    potencia = 2

    while Numero_termos<= termos:
            potencia = potencia*2
            Mersenne = potencia - 1
            if primo(Mersenne) and primo(n):
                soma += n
                Numero_termos += 1
            n += 1
        
    print('Problema 3:', soma)


def main():
    Problema1(100)
    Problema2(1000)
    Problema3(30)

if __name__=='__main__':
    main()





