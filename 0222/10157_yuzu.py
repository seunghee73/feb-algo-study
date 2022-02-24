d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
c, r = map(int, input().split())
k = int(input())
if c*r < k:
    print(0)
else:
    check = [[False]*c for _ in range(r)]
    x, y = 0, 0
    check[x][y] = True
    k -= 1
    while k >0:
        if 0<=x+d[0][0]<r and 0<=y+d[0][1]<c and check[x+d[0][0]][y+d[0][1]] == False:
            x += d[0][0]
            y += d[0][1]
            check[x][y] = True
        else:
            d.append(d.pop(0))
            x += d[0][0]
            y += d[0][1]
            check[x][y] = True
        k -= 1
    print(y+1, x+1)