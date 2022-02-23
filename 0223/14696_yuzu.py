for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_card = {4:0, 3:0, 2:0, 1:0}
    b_card = {4:0, 3:0, 2:0, 1:0}
    del a[0]
    del b[0]
    for aa in a:
        a_card[aa] += 1
    for bb in b:
        b_card[bb] += 1
    ans = 'D'
    for i in range(4, 0, -1):
        if a_card[i] > b_card[i]:
            ans = 'A'
            break
        elif a_card[i] < b_card[i]:
            ans = 'B'
            break
    print(ans)