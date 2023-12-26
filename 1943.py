categorias = [1, 3, 5, 10, 25, 50, 100]
colocacao = int(input())
for categoria in categorias:
    if colocacao <= categoria:
        print(f'Top {categoria}')
        break