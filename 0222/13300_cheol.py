N, K = map(int,input().split())
stu = [[0]*6 for _ in range(2)]

for i in range(N):
    S, Y = map(int, input().split())
    stu[S][Y-1] += 1 # 성별에 따른 학년 저장

bang = 0
for i in stu:
    for j in range(len(i)):
        if i[j] == 0:
            continue
        elif i[j] % K == 0:
            bang += i[j] // K
        else:
            bang += i[j] // K + 1
print(bang)
