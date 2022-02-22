C, R = map(int, input().split())
K = int(input())
if R * C < K:
    print(0)
else:
    arr = [[0] * C for _ in range(R)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    d = 0
    r = 0
    c = 0
    cnt = 1
    arr[0][0] = 1
    while cnt < K:
        newR = r + dr[d]
        newC = c + dc[d]
        if newR < 0 or newR >= R or newC < 0 or newC >= C or arr[newR][newC] != 0:
            d = (d + 1) % 4
        r += dr[d]
        c += dc[d]
        cnt += 1
        arr[r][c] = cnt
    print(c + 1, r + 1)
