import sys

arr = [[-1 for i in range(1001)] for i in range(1001)]
N = int(input())
for n in range(N):
    x, y , dx, dy = map(int, sys.stdin.readline().split())
    for i in range(dx):
        for j in range(dy):
            arr[y+j][x+i] = n

cnt = [0] * N
for i in range(1001):
    for j in range(1001):
        if arr[j][i] > -1 : cnt[arr[j][i]] += 1
for i in cnt : print(i)
