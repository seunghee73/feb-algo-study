import sys
from collections import deque

N = int(sys.stdin.readline())
sol = deque([])
for _ in range(N):
    arr = list(sys.stdin.readline().split())
    n = len(sol)
    if arr[0] == 'push':
        sol += [arr[1]]
    elif arr[0] == 'pop':
        if not sol:
            print(-1)
        else:
            print(sol.popleft())
    elif arr[0] == 'size':
        print(n)
    elif arr[0] == 'empty':
        if not sol:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if not sol:
            print(-1)
        else:
            print(sol[0])
    elif arr[0] == 'back':
        if not sol:
            print(-1)
        else:
            print(sol[n - 1])
