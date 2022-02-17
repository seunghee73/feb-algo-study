T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    items = list(input().split())
    items_copy = list(items)
    ans = ['ㄱ'] * m
    for _ in range(n):
        a, b = list(map(int, input().split()))
        ans[b-1] = items[a-1]
        items_copy.remove(items[a-1])
    for i in items_copy:
        for j in range(m):
            if ans[j] == 'ㄱ':
                ans[j] = i
                break
    print(' '.join(ans))