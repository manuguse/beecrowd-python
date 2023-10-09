x = int(input())
while True:
    z = int(input())
    if z > x:
        break

soma = 0
cont = 0

while soma <= z:
    soma += x
    x += 1
    cont += 1

print(cont)