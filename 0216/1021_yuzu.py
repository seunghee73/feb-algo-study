n, m = map(int, input().split())
a = list(map(int, input().split()))
q = [i+1 for i in range(n)]
cnt = 0
for aa in a:
    cnt_l = 0
    cnt_r = 1
    for i in range(len(q)):
        if q[i] == aa:
            break
        cnt_l += 1
    for j in range(len(q)-1, -1, -1):
        if q[j] == aa:
            break
        cnt_r += 1

    if cnt_l >= cnt_r:
        while q[-1] != aa:
            q.insert(0, q.pop())
        q.insert(0, q.pop())
        cnt += cnt_r
    else:
        while q[0] != aa:
            q.append(q.pop(0))
        cnt += cnt_l
    q.pop(0)
print(cnt)