from collections import deque

N , M = map(int, input().split())
nums = list(map(int, input().split()))
N_list = deque([i for i in range(1, N+1)])
cnt = 0
for i in range(M):
    idx = N_list.index(nums[i])
    if idx > (len(N_list) - idx):
        while N_list[0] != nums[i]:
            N_list.insert(0,N_list.pop())
            cnt += 1
    else :
        while N_list[0] != nums[i]:
            N_list.append(N_list.popleft())
            cnt += 1
    if N_list[0] == nums[i]:
        N_list.popleft()
print(cnt)