
#1 caçador
#2 Flor

R1,X1,Y1,R2,X2,Y2 = input().split()


def trans_int(nu):
    nu = int(nu)
    return nu

R1,X1,Y1,R2,X2,Y2 = map(trans_int,(R1,X1,Y1,R2,X2,Y2))


if X1 + R1 <= X2 + R2 or X1 - R1<= X2 - R2 :
    if Y1 + R1 <= Y2 + R2 or Y1 - R1 <= Y2 - R2:
        print('RICO')
else:
    print('MORTO')




