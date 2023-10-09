opcoes = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}
codigo, quantidade = map(int, input().split())

valor = opcoes[codigo] * quantidade
print(f"Total: R$ {valor:.2f}")