num = int(input())
for i in range(num):
    caracteres = input()

    if caracteres[0] == caracteres[2]:
        resultado = int(caracteres[0]) * int(caracteres[2])

    elif caracteres[1].isupper():
        resultado = int(caracteres[2]) - int(caracteres[0])
    
    else:
        resultado = int(caracteres[0]) + int(caracteres[2])

    print(resultado)