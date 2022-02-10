from itertools import combinations

while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break
    l = list[0]
    arr = num[1:len(num)]
    arr = list(combinations(arr, 6))
    for i in range(len(arr)):
        result = []
        for n in arr[i]:
            result += [str(n)]
        print(' '.join(result))
    print()
