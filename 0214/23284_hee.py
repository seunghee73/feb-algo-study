#from itertools import permutations
#from itertools import combinations
#from collections import deque

# nums = [0 for i in range(N)] + [1 for i in range(N)]
# stack_list = [i for i in range(1,N+1)]
# L = list(set(permutations(nums)))
# lst = []
#
# def stack_func(stack_list, arr):
#     a = list(stack_list); arr = list(arr)
#     temp = []; idx = 0; result = []
#     for i in arr:
#         if i == 1:
#             temp.append(a[idx])
#             idx += 1
#         elif i == 0:
#             result.append(temp.pop())
#     return result
#
# for i in L :
#     if L[0] == 0 : continue
#     cnt = [0, 0]
#     for j in i :
#         cnt[j] += 1
#         if cnt[0] > cnt[1]:
#             break
#     else:
#         lst.append(i)
# R = []
# for i in lst:
#     R.append(stack_func(stack_list, i))
# R.sort()
# for i in R:
#     new_lst = [str(a) for a in i]
#     print(' '.join(new_lst))
# 시간 초과 엔딩 ^^ 2^20? 어림없지...

# nums = [i for i in range(1, N+1)]
# com = list(permutations(nums))
# print(com)
# lst = []
#
# for i in com:
#     stack = []
#     here = 0
#     for j in i:
#         while here < j:
#             here += 1
#             stack.append(here)
#         if stack[-1] == j:
#             stack.pop()
#         else:
#             break
#     else: lst.append(i)
# print(lst)
# 더 나아졌지만 여전히 너무 오래 걸림ㅠ

N = int(input())

ans =[]
chk = [False] * (N+1)
result = []
lst = []
def recur(num):
    if num == N:
        result.append(list(ans))
        return
    for i in range(1, N+1):
        if chk[i]==False:
            chk[i] = True
            ans.append(i)
            recur(num+1)
            chk[i] = False
            ans.pop()
recur(0)
for i in result:
    stack = []
    here = 0
    for j in i:
        while here < j:
            here += 1
            stack.append(here)
        if stack[-1] == j:
            stack.pop()
        else:
            break
    else: print(' '.join(map(str,i)))
# 두 과정을 하나로 합쳐야 할듯