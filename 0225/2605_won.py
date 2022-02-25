n = int(input())
arr = list(map(int, input().split()))
sol = []
for i in range(len(arr)):
    sol.insert(i - arr[i], i + 1)
print(*sol)