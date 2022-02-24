N = int(input())
lst = []
for _ in range(6):
    _, B = map(int,input().split())
    lst.append(B)
idx = lst.index(max(lst))

if idx == 5: # 리스트의 끝인 경우 (idx + 1에서 index error 방지)
    max_val = max(lst[idx-1], lst[0])
    min_val = min(lst[idx-1], lst[0])
    min_idx = lst.index(min_val)
    next_min = min(lst[min_idx+1], lst[min_idx-1])
else :
    max_val = max(lst[idx-1], lst[idx+1])
    min_val = min(lst[idx-1], lst[idx+1])
    min_idx = lst.index(min_val)
    if min_idx == 5: # 리스트의 끝인 경우
        next_min = min(lst[0], lst[min_idx-1])
    else :
        next_min = min(lst[min_idx+1], lst[min_idx-1])

S = lst[idx] * max_val - next_min * (max_val - min_val)
print(S*N)
