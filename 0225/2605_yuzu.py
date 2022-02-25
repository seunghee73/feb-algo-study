n = int(input())
ans = []
m = list(map(int, input().split()))
for i in range(n):
    if m[i] == 0:
        ans.append(i+1)
    else:
        ans.insert(-m[i], i+1)
print(*ans)