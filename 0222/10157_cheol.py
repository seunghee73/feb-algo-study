C, R = map(int, input().split())
K = int(input())
a = [[0 for i in range(C+1)] for j in range(R+1)]

if K > C*R:
    print(0)
else:
    for i in range(R+1):
        a[i][C] = -1
    for j in range(C+1):
        a[R][j] = -1
    cnt = 0
    n = 1
    i, j = 0, 0
    a[0][0] = 1

    while True:
        if n == K:
            break
        else:
            if cnt == 0:
                if a[i+1][j] == 0:
                    i += 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 1
            elif cnt == 1:
                if a[i][j+1] == 0:
                    j += 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 2
            elif cnt == 2:
                if a[i-1][j] == 0:
                    i -= 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 3
            elif cnt == 3:
                if a[i][j-1] == 0:
                    j -= 1
                    n += 1
                    a[i][j] = n
                else:
                    cnt = 0
    print(j+1, i+1)