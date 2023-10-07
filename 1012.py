pi = 3.14159
A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)
    
areaTriangulo = float(A*C/2)
areaCirculo = float(pi*(C**2))
areaTrapezio = float((A + B)*C/2)
areaQuadrado = float(B**2)
areaRetangulo = float(A * B)

print(f'TRIANGULO: {areaTriangulo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')