base = [300, 1500, 600, 1000, 150]
ans = 225
for i in range(5):
    ans += base[i]*int(input())
print(ans)