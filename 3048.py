N = int(input())
nums:list = []
ans = 1
nums.append(int(input()))
for i in range(1, N):
    nums.append(int(input()))
    if nums[i] != nums[i-1]:
        ans += 1
print(ans)