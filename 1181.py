matriz = []
for i in range(12):
    matriz.append([0]*12)

linha = int(input())
operacao = input()

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

resultado = 0

for coluna in range(12):
    resultado += matriz[linha][coluna]

if operacao == "M":
    resultado /= 12

print(f"{resultado:.1f}")