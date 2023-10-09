matriz = []
for i in range(12):
    matriz.append([0]*12)

operacao = input()
resultado = 0

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for linha in range(1, 12):
    for coluna in range(linha):
        resultado += matriz[linha][coluna]

if operacao == "M":
    resultado /= 66

print(f"{resultado:.1f}")