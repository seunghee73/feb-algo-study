t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    s = list(input().split())
    arr = [[] for i in range(m)]
    for _ in range(n):
        a, b = map(int, input().split())
        arr[b-1] = s[a-1]
    for j in range(m):
        for ss in s:
            if len(arr[j]) == 0 and ss not in arr:
                arr[j] = ss
                break
    print(*arr)