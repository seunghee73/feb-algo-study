n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
h = []
w = []
for i in range(6):
    if arr[i][0] in [3, 4]:
        h += [arr[i][1]]
    else:
        w += [arr[i][1]]
h = max(h)
w = max(w)
idx = 0
jdx = 0
for i in range(6):
    if arr[i][1] == h:
        idx = i
    if arr[i][1] == w:
        jdx = i
sol = (h * w - arr[(idx + 3) % 6][1] * arr[(jdx + 3) % 6][1]) * n
print(sol)
