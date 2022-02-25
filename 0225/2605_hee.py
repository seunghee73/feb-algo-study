N = int(input())
nums = list(map(int, input().split()))
result = []
for i in range(1, N+1):
    if nums[i-1] == 0 :
        result.append(i)
    else :
        result.insert(-nums[i-1],i)
print(*result)
