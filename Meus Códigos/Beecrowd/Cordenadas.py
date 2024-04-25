
X , Y = input().split()

X = float(X)
Y = float(Y)

altura = None
lado = None

if X > 0:
    lado = 'direito'
elif X < 0:
    lado = 'esquerdo'
if Y > 0:
    altura = 'cima'
elif Y < 0:
    altura = 'baixo'

if lado == 'direito' and altura == 'cima':
    print('Q1')
elif lado == 'esquerdo' and altura == 'cima':
    print('Q2')
elif lado == 'esquerdo' and altura == 'baixo':
    print('Q3')
elif lado == 'direito' and altura == 'baixo':
    print('Q4')
elif X == 0 and Y !=0:
    print('Eixo Y')
elif Y == 0 and X != 0:
    print('Eixo X')
elif X == 0 and Y == 0:
    print('Origem')


