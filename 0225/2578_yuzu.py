bingo = [list(map(int, input().split())) for _ in range(5)]
lst = []
for _ in range(5):
    lst += list(map(int, input().split()))

def game(arr):
    cnt = 0
    sum = 0
    for i in range(5):
        sum += arr[i][i]
    if sum == 0:
        cnt += 1
    sum = 0
    for j in range(5):
        sum += arr[j][4-j]
    if sum == 0:
        cnt += 1
    for p in range(5):
        sum1 = 0
        sum2 = 0
        for q in range(5):
            sum1 += arr[p][q]
            sum2 += arr[q][p]
        if sum1 == 0:
            cnt += 1
        if sum2 == 0:
            cnt += 1
    if cnt >= 3:
        return 1

ans = 0
for l in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == lst[l]:
                bingo[i][j] = 0
                ans += 1
    if game(bingo) == 1:
        break
print(ans)