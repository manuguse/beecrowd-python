while True:
    try:
        rastro = input()
        processos = int(input())
        ciclos = 0
        count = processos
        for i in range(len(rastro)):
            if rastro[i] == 'W':
                ciclos += 1
                count = processos
            else:
                if count == processos:
                    ciclos += 1
                count -= 1
            if count == 0:
                count = processos
        print(ciclos)                
    except EOFError:
        break