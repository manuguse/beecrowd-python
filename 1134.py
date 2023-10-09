tipos = [0, 0, 0]

while True:

    while True:
        tipo = int(input())
        if 1 <= tipo <= 4:
            break
    if tipo == 4:
        break

    tipos[tipo - 1] += 1

print('MUITO OBRIGADO')
print(f'Alcool: {tipos[0]}')
print(f'Gasolina: {tipos[1]}')
print(f'Diesel: {tipos[2]}')