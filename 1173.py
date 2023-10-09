vector = []

num = int(input())

for i in range(10):
    vector.append(num)
    num *= 2

for i in range(10):
    print(f"N[{i}] = {vector[i]}")