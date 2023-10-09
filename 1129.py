while True:
    num_questoes = int(input())
    if num_questoes == 0:
        break

    for i in range(num_questoes):
        resposta = input().split()
        resposta = list(map(int, resposta))

        cont_alternativas = 0
        resposta_correta = ''

        for questao in resposta:
            if questao <= 127:
                cont_alternativas += 1
                resposta_correta = chr(resposta.index(questao) + 65)

        if cont_alternativas == 1:
            print(resposta_correta)
        else:
            print('*')