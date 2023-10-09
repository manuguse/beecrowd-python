def somaImpar(x,y):
    maior = max(x,y)
    menor = min(x,y)

    soma = 0

    for i in range(menor+1,maior):
        if i % 2 != 0:
            soma += i

    return soma

casos = int(input())
for i in range(casos):
    soma = 0
    x, y = map(int, input().split())
    print(somaImpar(x,y))