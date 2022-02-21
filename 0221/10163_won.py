import sys

N = int(sys.stdin.readline())
temp = [[0] * 1001 for _ in range(1001)]

for i in range(1, N + 1):
    sx, sy, w, h = map(int, sys.stdin.readline().split())
    for r in range(sy, sy + h):
        temp[r][sx:sx + w] = [i] * w

for i in range(1, N + 1):
    cnt = 0
    for r in range(1001):
        cnt += temp[r].count(i)
    print(cnt)