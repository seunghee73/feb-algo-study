import sys

total, m = map(int, sys.stdin.readline().split())  # total = 교과서 수, m = 더미 수
result = 'Yes'

for _ in range(m):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            result = 'No'
            break
print(result)
