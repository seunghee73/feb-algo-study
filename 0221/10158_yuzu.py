import sys
input = sys.stdin.readline

w, h = map(int, input().split())
x, y = map(int, input().split())
n = int(input())
x_lst = [i for i in range(w+1)]
xx_lst = x_lst[1:-1]
x_lst += xx_lst[::-1]
y_lst = [i for i in range(h+1)]
yy_lst = y_lst[1:-1]
y_lst += yy_lst[::-1]
print(x_lst[(x+n)%(2*w)], y_lst[(y+n)%(2*h)])