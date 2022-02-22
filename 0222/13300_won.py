N, K = map(int, input().split())
sol = 0
arr = [[0] * 2 for _ in range(6)]
for _ in range(N):
    gen, grade = map(int, input().split())
    arr[grade - 1][gen] += 1
for i in range(6):
    if arr[i][0]:
        sol += -(-arr[i][0] // K)
    if arr[i][1]:
        sol += -(-arr[i][1] // K)
print(sol)