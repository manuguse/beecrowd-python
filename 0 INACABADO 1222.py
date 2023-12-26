while True:
    try:
        numPalavras, numMaxLinhas, numMaxCaracter = map(int, input().split())
        conto = input()
        palavras = len(conto.split())
        paginas = 0
        caracteresPag = 0
        for palavra in conto:
            caracteresPag += len(palavra)
    except EOFError:
        break
