
#Função para definir numeros primos

def main(valor):
    for i in range(2, int(valor**0.5 +1)):
        if valor % i == 0:
            return False
        else:
            return True
    
#Resto de divisão botando a função

for i in range(600851475143 - 1 , 0, -1):
    if 600851475143%i == 0:
        if main(i):
            print(i)
            break


#Outra resolução

# def largest_prime_factor(n):
#     factor = 2
#     while factor * factor <= n:
#         if n % factor == 0:
#             n //= factor
#         else:
#             factor += 1
#     return n
# number = 600851475143
# largest_prime = largest_prime_factor(number)
# print("The largest prime factor of", number, "is", largest_prime)
