TC = int(input())

for _ in range(TC):
    m, n = map(int, input().split())
    arr = input().split()
    op = [list(map(int, input().split())) for _ in range(n)]
    new = [0] * m
    for i in range(n):
        target = arr[int(op[i][0]) - 1]
        pos = int(op[i][1]) - 1
        new[pos] = target

    for i in range(n):
        arr[int(op[i][0]) - 1] = 0

    remains = []
    for i in range(m):
        if arr[i] != 0:
            remains += [arr[i]]

    for i in range(m):
        if new[i] == 0:
            new[i] = remains.pop(0)
    print(*new)
