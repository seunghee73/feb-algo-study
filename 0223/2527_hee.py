for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    min_x = min(x1, x2)
    max_x = max(p1, p2)
    min_y = min(y1, y2)
    max_y = max(q1, q2)
    if ((max_x - min_x) > (p1-x1)+(p2-x2)) or ((max_y - min_y) > (q1-y1)+(q2-y2)): # 안 만나는 경우
        print('d')
    elif ((max_x - min_x) < (p1-x1)+(p2-x2)) and ((max_y - min_y) < (q1-y1)+(q2-y2)): # 직사각형 겹치는 경우
        print('a')
    elif ((max_x - min_x) == (p1-x1)+(p2-x2)) and ((max_y - min_y) == (q1-y1) + (q2-y2)): # 점이 만나는 경우
        print('c')
    else : # 선분이 만나는 경우
        print('b')
