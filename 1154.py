soma_idade = 0
cont = 0

while True:
    num = int(input())
    if num < 0:
        break

    soma_idade += num
    cont += 1

print(f"{soma_idade/cont:.2f}")