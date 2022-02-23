def check(a, b):
    if a[3] > b[3]:
        return 'A'
    elif b[3] > a[3]:
        return 'B'
    else:
        if a[2] > b[2]:
            return 'A'
        elif b[2] > a[2]:
            return 'B'
        else:
            if a[1] > b[1]:
                return 'A'
            elif b[1] > a[1]:
                return 'B'
            else:
                if a[0] > b[0]:
                    return 'A'
                elif b[0] > a[0]:
                    return 'B'
                else:
                    return 'D'
N = int(input())
for _ in range(N):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    nA = arr1[0]
    nB = arr2[0]
    arr1 = arr1[1:]
    arr2 = arr2[1:]
    A = [0] * 4
    B = [0] * 4
    for i in range(nA):
        A[arr1[i] - 1] += 1
    for i in range(nB):
        B[arr2[i] - 1] += 1

    print(check(A, B))

