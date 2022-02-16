n, m = map(int, input().split())
temp = [i for i in range(1, n + 1)]  # n
arr = list(map(int, input().split()))  # m
result = 0

def rotation(temp, num, result):
    idx = 0
    for i in range(len(temp)):
        if temp[i] == num:
            idx = i
            break

    if len(temp) // 2 >= idx:
        for _ in range(idx):
            temp += [temp.pop(0)]
    else:
        idx = len(temp) - idx
        for _ in range(idx):
            temp = [temp.pop()] + temp
    temp.pop(0)
    result += idx
    return temp, result

for i in range(m):
    temp, result = rotation(temp, arr[i], result)

print(result)