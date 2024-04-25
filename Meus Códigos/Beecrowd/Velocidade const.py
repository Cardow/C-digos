while True:
    try:
        # Recebe entrada
        distancia, VA, VB = input().split()

        # Converte para inteiros
        distancia = int(distancia)
        VA = int(VA)
        VB = int(VB)

        # Verifica se VB > VA
        if VB > VA:
            print('impossivel')
        else:
            # Calcula o tempo necessário
            t = distancia / (VA - VB)
            print('%.2f' % t)
    except EOFError:
        break

