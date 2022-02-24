k = int(input())
lst = []
for _ in range(6):
    a, b = map(int, input().split())
    lst.append(b)

max = 0
min = 0
idx = 0
for i in range(6):
    if i == 5:
        s = lst[5]*lst[0]
    else:
        s = lst[i]*lst[i+1]
    if s > max:
        max = s
        idx = i
min = lst[(idx+3)%6]*lst[(idx+4)%6]
print((max-min)*k)