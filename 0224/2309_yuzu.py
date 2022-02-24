arr = [int(input()) for _ in range(9)]
arr.sort()
sum = sum(arr)
x, y = 10, 10
for i in range(9):
    for j in range(i+1, 9):
        if i != j:
            if sum - arr[i] - arr[j] == 100:
                x, y = i, j
                break
    if x != 10:
        break
for a in arr:
    if a != arr[x] and a != arr[y]:
        print(a)