import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(N):
    s = list(map(str,sys.stdin.readline().split()))
    if s[0] == 'push':
        dq.append(s[1])
    elif s[0] == 'pop':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif s[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif s[0] == 'size':
        print(len(dq))
    elif s[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif s[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])