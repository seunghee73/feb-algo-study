w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

p = p + T
q = q + T

p = p % (2 * w)
q = q % (2 * h)

if p > w:
    p = 2 * w - p
if q > h:
    q = 2 * h - q
print(p, q)
# w, h = map(int,input().split())
# p, q = map(int,input().split())
# T = int(input())
# dx = [1,-1,-1,1]
# dy = [1,1,-1,-1]

# cnt = 0
# dir = 0
#
# while 1:
#     if T == cnt:
#         break
#     cnt += 1
#     mov_p, mov_q = p + dx[dir], q + dy[dir]
#     if mov_p <= 0:
#         if dir == 0:
#             dir = 1
#         elif dir == 1:
#             dir = 0
#         elif dir == 2:
#             dir = 3
#         elif dir == 3:
#             dir = 2
#     if mov_p >= w:
#         if dir == 0:
#             dir = 1
#         elif dir == 1:
#             dir = 0
#         elif dir == 2:
#             dir = 3
#         elif dir == 3:
#             dir = 2
#     if mov_q <= 0:
#         if dir == 0:
#             dir = 3
#         elif dir == 1:
#             dir = 2
#         elif dir == 2:
#             dir = 1
#         elif dir == 3:
#             dir = 0
#     if mov_q >= h:
#         if dir == 0:
#             dir = 3
#         elif dir == 1:
#             dir = 2
#         elif dir == 2:
#             dir = 1
#         elif dir == 3:
#             dir = 0
#     p, q = mov_p, mov_q
# print(p,q)
