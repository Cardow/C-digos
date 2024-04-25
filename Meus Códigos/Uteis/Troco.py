while True:
    try:
        dinheiro = float(input())
        if dinheiro <= 0 or dinheiro >=100000000:
            print('Numero precisa ser maior que 0 e menor que 100000000')
            continue
        break
    except: print('Precisa ser um número')
   
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]
dinheiro*=100

numnotas=[]
nummoeda=[]

for x in notas:
    i = (dinheiro/x)
    numnotas.append(i)
    dinheiro = dinheiro%x
   


for y in moedas:
    h = (dinheiro/y)
    nummoeda.append(h)
    dinheiro = dinheiro%y
   


print('NOTAS:')

for x, y in zip(numnotas, notas):
   
    print('%i nota(s) de R$ %.2f' %(x,y/100))
   
print('MOEDAS:')
   
for h, j in zip(nummoeda, moedas):
   
    print('%i moeda(s) de R$ %.2f' %(h,j/100))