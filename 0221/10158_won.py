w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
a, b = divmod(x + t, w)
c, d = divmod(y + t, h)
if a % 2:
    x = w - b
else:
    x = b
if c % 2:
    y = h - d
else:
    y = d
print(x, y)