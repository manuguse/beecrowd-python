A, B, C, D = map(int, input().split())

flag = False

if B > C:
    if D > A:
        if C + D > A + B:
            if C > 0 and D > 0:
                if A % 2 == 0:
                    print('Valores aceitos')
                    flag = True
if not flag:
    print('Valores nao aceitos')