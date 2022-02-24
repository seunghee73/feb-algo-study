n = 9

arr = [int(input()) for _ in range(n)]

sumV = sum(arr)
for i in range(9):
    for j in range(i + 1, 9):
        if sumV - (arr[i] + arr[j]) == 100:
            tmp1, tmp2 = arr[i], arr[j]

arr.remove(tmp1)
arr.remove(tmp2)


print('\n'.join(map(str, sorted(arr))))
