C, R = map(int, input().split())
K = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
if K > C * R :
    print(0)
else:
    C -= 1
    x, y = 1, 0

    while K > 0:
        for i in range(4):
            if K < abs(dx[i] * C + dy[i] * R) and K > 0:
                x += dx[i] * K
                y += dy[i] * K
                K = 0
                break
            elif K > 0:
                x += dx[i] * C
                y += dy[i] * R
                K -= abs(dx[i]*C) + abs(dy[i]*R)
                if (dx[i] * C) != 0:
                    C -= 1
                elif (dy[i] * R) != 0:
                    R-=1
    print(x,y)
