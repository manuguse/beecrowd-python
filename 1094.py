especies = {
    'C': 0, 'R': 0, 'S': 0
}

num = int(input())
total:int = 0

for i in range(num):
    num_tipo, tipo = input().split(' ')
    num_tipo = int(num_tipo)

    total += num_tipo
    especies[tipo] += num_tipo

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {especies["C"]}')
print(f'Total de ratos: {especies["R"]}')
print(f'Total de sapos: {especies["S"]}')
print(f'Percentual de coelhos: {(especies["C"] / total) * 100:.2f} %')
print(f'Percentual de ratos: {(especies["R"] / total) * 100:.2f} %')
print(f'Percentual de sapos: {(especies["S"] / total) * 100:.2f} %')