
n = 1
cima = 2**n
baixo = 20
print ('%i/%i' %(cima, baixo))

while baixo > 1 and n < 20:
    baixo = baixo -1
    n = n + 1
    cima = 2**n
    print ('%i/%i' %(cima, baixo))



