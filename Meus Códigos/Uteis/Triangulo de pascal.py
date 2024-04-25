def num_Pascal(n, p): #C(n/p) = n!/p!(n-p)!

    #Linha 0 = 1 o ultimo de cada linha =1
    if p == 0  or p == n:
        return 1
    
    #Propriedade aditiva dos coeficientes binomiais
    else:
        valor = num_Pascal(n - 1, p - 1) + num_Pascal(n - 1, p)
        return valor

linhas = 10

for n in range(0,linhas + 1):
    for p in range (0, n + 1):
        resultado = num_Pascal(n, p)
        print(resultado)
    
        