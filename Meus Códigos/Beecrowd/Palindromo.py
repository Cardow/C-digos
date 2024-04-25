
#Função para ver se é um palíndromo

def Palindromo (numero):
    numero = str(numero)
    if len(numero) == 6:
        if numero[0] == numero[5] and numero[1] == numero[4] and numero[2] == numero[3]:
            return True

#Maior palíndromo 3 digitos
        
todos = []
    
for i in range(999, 99, -1):
      for h in range(999,99, -1):
            valor = i*h
            if Palindromo(valor):
                  todos.append(valor)

Maior_palindromo = max(todos)
print(Maior_palindromo)