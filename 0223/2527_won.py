# def search():
#     isPoint = False
#     isLine = False
#     isArea = False
#     for r in range(y2 - y, q2 - y + 1):
#         for c in range(x2 - x, p2 - x + 1):
#             arr[r][c] += 1
#             if arr[r][c] == 2:
#                 isPoint = True
#                 if r - 1 >= 0 and c - 1 >= 0 and arr[r - 1][c] == 2 and arr[r][c - 1] == 2:
#                     isArea = True
#                     break
#                 elif (r - 1 >= 0 and arr[r - 1][c] == 2) or (c - 1 >= 0 and arr[r][c - 1] == 2):
#                     isLine = True
#     if isArea:
#         return 'a'
#     else:
#         if isLine:
#             return 'b'
#         else:
#             if isPoint:
#                 return 'c'
#             else:
#                 return 'd'
#
# for _ in range(4):
#     x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
#     x = x2 if x1 > x2 else x1
#     y = y2 if y1 > y2 else y1
#     p = p1 if p1 > p2 else p2
#     q = q1 if q1 > q2 else q2
#
#     arr = [[0] * (p - x + 1) for _ in range(q - y + 1)]
#     for r in range(y1 - y, q1 - y + 1):
#         arr[r][x1 - x:p1 - x + 1] = [1] * (p1 - x1 + 1)
#     sol = search()
#     print(sol)




for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    x = x1 if x1 > x2 else x2
    y = y1 if y1 > y2 else y2
    p = p1 if p1 < p2 else p2
    q = q1 if q1 < q2 else q2

    xdiff = p - x
    ydiff = q - y
    if xdiff > 0 and ydiff > 0:
        print('a')
    elif xdiff < 0 or ydiff < 0:
        print('d')
    elif xdiff == 0 and ydiff == 0:
        print('c')
    else:
        print('b')