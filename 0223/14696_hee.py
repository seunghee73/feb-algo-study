N = int(input())

for _ in range(N):
    a = list(map(int, input().split()))
    a_cnt = [0] * 5
    for i in range(1, a[0]+1):
        a_cnt[a[i]] += 1
    b = list(map(int, input().split()))
    b_cnt = [0] * 5
    for i in range(1, b[0]+1):
        b_cnt[b[i]] += 1
    for i in range(4, 0, -1):
        if a_cnt[i] > b_cnt[i]:
            print('A')
            break
        elif a_cnt[i] < b_cnt[i]:
            print('B')
            break
    else : print('D')
