soma_pos:int = 0
pos:int = 0

for i in range(6):
    num:float = float(input())
    if num > 0:
        pos += 1
        soma_pos += num

print(f'{pos} valores positivos')
print(f'{soma_pos/pos:.1f}')