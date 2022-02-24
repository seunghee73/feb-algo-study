N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

w = 0
h = 0
widx = 0
hidx = 0
for i in range(len(arr)):
    if arr[i][0] == 1:
        if w < arr[i][1]:
            w = arr[i][1]
            widx = i
    elif arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            widx = i
    elif arr[i][0] == 3:
        if h < arr[i][1]:
            h = arr[i][1]
            hidx = i
    elif arr[i][0] == 4:
        if h < arr[i][1]:
            h = arr[i][1]
            hidx = i
shortW = abs(arr[(widx - 1) % 6][1] - arr[(widx + 1) % 6][1])
shortH = abs(arr[(hidx - 1) % 6][1] - arr[(hidx + 1) % 6][1])
answer = ((w*h)-(shortW*shortH)) * N
print(answer)
