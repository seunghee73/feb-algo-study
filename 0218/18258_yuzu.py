import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# deque를 안쓰면 시간초과
queue = deque()
for _ in range(n):
    m = list(input().strip().split())
    if m[0] == 'push':
        queue.append(int(m[1]))
    elif m[0] == 'front':
        print(-1) if len(queue)==0 else print(queue[0])
    elif m[0] == 'back':
        print(-1) if len(queue)==0 else print(queue[-1])
    elif m[0] == 'size':
        print(len(queue))
    elif m[0] == 'empty':
        print(1) if len(queue)==0 else print(0)
    elif m[0] == 'pop':
        print(-1) if len(queue)==0 else print(queue.popleft())