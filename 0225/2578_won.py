def find(k):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == k:
                arr[i][j] = -1
                return

def getBingNum():
    bing = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[i][j] == -1:
                cnt += 1
        if cnt == 5:
            bing += 1

    for j in range(5):
        cnt = 0
        for i in range(5):
            if arr[i][j] == -1:
                cnt += 1
        if cnt == 5:
            bing += 1

    cnt = 0
    for i in range(5):
        if arr[i][i] == -1:
            cnt += 1
    if cnt == 5:
        bing += 1

    cnt = 0
    for i in range(5):
        if arr[i][4 - i] == -1:
            cnt += 1
    if cnt == 5:
        bing += 1

    return bing

def sol():
    cnt = 0
    for i in range(5):
        for j in range(5):
            cnt += 1
            find(host[i][j])
            if getBingNum() >= 3:
                return cnt
arr = [list(map(int, input().split())) for _ in range(5)]
host = [list(map(int, input().split())) for _ in range(5)]
print(sol())
