for line in iter(input, '0 0'):
    X, M = map(int, line.split())
    print(X * M)