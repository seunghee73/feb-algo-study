from collections import deque
import sys
N = int(sys.stdin.readline())
lst = deque([])
for _ in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        lst.append(a[1])
    elif a[0] == 'pop':
        if len(lst) == 0 : print(-1)
        else : print(lst.popleft())
    elif a[0] == 'size':
        print(len(lst))
    elif a[0] == 'empty':
        if len(lst) == 0 : print(1)
        else: print(0)
    elif a[0] == 'front':
        if len(lst) == 0 : print(-1)
        else : print(lst[0])
    elif a[0] == 'back':
        if len(lst) == 0 : print(-1)
        else : print(lst[-1])
