for i in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())

    # if x1 > x2 or x2 > p1 or q2 < y1 or q1 < y2:
    #     print('d')
    #     break

    x = max(x1,x2)
    y = max(y1,y2)
    p = min(p1,p2)
    q = min(q1,q2)

    dx = p - x
    dy = q - y

    if dx > 0 and dy > 0:
        print('a')
    elif dx < 0 or dy < 0:
        print('d')
    elif dx == 0 and dy == 0:
        print('c')
    else:
        print('b')