paper = [[0]*1001 for i in range(1001)]
T = int(input())

for i in range(T):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        for k in range(y, y+h):
            paper[j][k] = i+1
for i in range(T):
    cnt = 0
    for p in paper:
        cnt += p.count(i+1)
    print(cnt)