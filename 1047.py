hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

inicio = hora_inicial * 60 + minuto_inicial
fim = hora_final * 60 + minuto_final

if inicio == fim:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

elif inicio < fim:
    duracao = fim - inicio
    horas = int(duracao / 60)
    minutos = duracao % 60
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

elif inicio > fim:
    duracao = (24 * 60 - inicio) + fim
    horas = int(duracao / 60)
    minutos = duracao % 60
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')