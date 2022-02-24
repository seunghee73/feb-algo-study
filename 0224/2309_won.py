arr = []
for _ in range(9):
    arr += [int(input())]
total = 0
for i in range(9):
    total += arr[i]
notI1 = 0
notI2 = 0
for i in range(8):
    for j in range(i + 1, 9):
        if total - arr[i] - arr[j] == 100:
            notI1 = i
            notI2 = j
            break
del arr[notI1]
del arr[notI2 - 1]
arr.sort()
for i in range(7):
    print(arr[i])