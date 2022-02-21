W, H = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

t_W = t % (2*W)
t_H = t % (2*H)
dx = [1, -1]
dy = [1, -1]

while t_W > 0 :
    for i in range(2) :
        while -1 < x + dx[i] < W+1 and t_W > 0:
            x = x + dx[i]
            t_W -= 1

while t_H > 0 :
    for i in range(2) :
        while -1 < y + dy[i] < H+1 and t_H > 0:
            y = y + dy[i]
            t_H -= 1
print(x,y)
