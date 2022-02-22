girl = [0, 0, 0, 0, 0, 0]
boy = [0, 0, 0, 0, 0, 0]
n, k = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        girl[b-1] += 1
    else:
        boy[b-1] += 1
ans = 0
for g in girl:
    ans += (g+k-1)//k
for b in boy:
    ans += (b+k-1)//k
print(ans)