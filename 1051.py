salario = float(input())

if salario <= 2000:
    print("Isento")
elif 2000 < salario <= 3000:
    print(f"R$ {(salario - 2000) * 0.08:.2f}")
elif 3000 < salario <= 4500:
    print(f"R$ {(salario - 3000) * 0.18 + 1000 * 0.08:.2f}")
else:
    print(f"R$ {(salario - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08:.2f}")