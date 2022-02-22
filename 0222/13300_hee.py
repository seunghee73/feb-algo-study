import math
N, K = map(int, input().split())
W = [0] * 7
M = [0] * 7
for i in range(N):
    S = list(map(int, input().split()))
    if S[0] == 0 :
        W[S[1]] += 1
    else :
        M[S[1]] += 1
cnt = 0
for i in range(1, 7):
    cnt += math.ceil(W[i]/K)
    cnt += math.ceil(M[i]/K)
print(cnt)