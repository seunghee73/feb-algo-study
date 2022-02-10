from itertools import combinations

def comb (n, r):
    if n == r or r == 0:
        return lst[1]
    else :
        return lst[comb(n-1,r-1) + comb(n-1,r)]
# combination 개수 세는 재귀 함수

while True:
    lst = list(map(int,input().split()))
    if lst == [0]:
        break
    a = list(combinations(lst[1:], 6))
    new_lst = []
    for i in a:
        temp_list = list(i)
        new_lst.append([str(j) for j in temp_list])
    for i in new_lst :
        print(' '.join(i))
    print()