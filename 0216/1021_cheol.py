from collections import deque

N, M = map(int, input().split())
lst = list(map(int, input().split()))
q = deque([i for i in range(1, N+1)])
cnt = 0
while len(lst) > 0:
    if q[0] == lst[0]:
        q.popleft()
        del lst[0]
    else:
        if q.index(lst[0]) > len(q) / 2:
            while q[0] != lst[0]:
                q.appendleft(q.pop())
                cnt += 1
        else:
            while q[0] != lst[0]:
                q.append(q.popleft())
                cnt += 1
print(cnt)