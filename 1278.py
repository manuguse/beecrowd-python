while True:
    cont = 0
    if cont != 0:
        print()
    N = int(input())
    if N == 0:
        break
    maxLen = 0
    frases = []
    for i in range(N):
        fraseSemEspaco = ''
        frase = input().split()
        for palavra in frase:
            fraseSemEspaco += (palavra + ' ')
        fraseSemEspaco = fraseSemEspaco.rstrip()
        if len(fraseSemEspaco) > maxLen:
            maxLen = len(fraseSemEspaco)
        frases.append(fraseSemEspaco)
    for frase in frases:
        print(frase.rjust(maxLen, ' '))
    cont += 1
