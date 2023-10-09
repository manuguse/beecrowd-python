aumentos = {
    400: 1.15,
    800: 1.12,
    1200: 1.10,
    2000: 1.07,
    100000000000000: 1.04
}

salario = float(input())

for aumento in aumentos:
    if salario <= aumento:
        novo_salario = salario * aumentos[aumento]
        reajuste = novo_salario - salario
        percentual = (aumentos[aumento] - 1) * 100
        break

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual:.0f} %')