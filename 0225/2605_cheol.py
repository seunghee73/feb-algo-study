N = int(input())
num = list(map(int,input().split()))

answer = []

for i in range(N):
    answer.insert(i - num[i],str(i+1))
print(*answer)