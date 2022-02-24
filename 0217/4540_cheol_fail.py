# insert 쓰면서 하다보니 문제의 본질을 왜곡하여 코드를 짜버림 포기
from collections import deque
T = int(input())

for tc in range(T):
    N,M = map(int,input().split()) # N q길이 M연산횟수
    lst1 = list(input().split())
    dq = deque()

    for i in range(N):
        dq.append(lst1[i])

    for _ in range(M):
        a, b = map(int, input().split())  # dq = deque(['alpha', 'beta', 'gamma', 'delta', 'epsilon'])
        if a > b:
            tmp = dq[a-1]
            dq[a-1] = '-1'
            dq.insert(b-1, tmp)
            dq.remove(dq[a])
        else:
            tmp = dq[a-1]
            dq[a-1] = '-1'
            dq.insert(b, tmp)
            dq.remove(dq[a-1])

    print(' '.join(dq))
