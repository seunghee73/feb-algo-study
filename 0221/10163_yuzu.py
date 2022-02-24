import sys
input = sys.stdin.readline

arr = [[0]*1001 for _ in range(1001)]
n = int(input())
for i in range(1, n+1):
    x, y, a, b = map(int, input().split())
    for nx in range(x, x+a):
        arr[nx][y:y+b] = [i]*b
ans = [0]*(n+1)
for ar in arr:
    for arar in ar:
        if arar != 0:
            ans[arar] += 1
for an in ans[1:]:
    print(an)

'''
숫자마다 카운트하면 리스트에 한번에 카운팅 하는 것보다 시간이 2배 더 걸림
for j in range(1, n+1):
    count = 0
    for ar in arr:
        count += ar.count(j)
    print(count)
'''