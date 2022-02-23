for _ in range(4):
    a1, a2, b1, b2, x1, x2, y1, y2 = map(int, input().split())
    p = max(a1, x1)
    q = min(b1, y1)
    r = max(a2, x2)
    s = min(b2, y2)

    i = q-p
    j = s-r

    if i > 0 and j > 0:
        print('a')
    elif i < 0 or j < 0:
        print('d')
    elif i == 0 and j == 0:
        print('c')
    else:
        print('b')