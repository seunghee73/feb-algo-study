import sys
N, M = map(int, input().split())

# books = []
# for _ in range(M):
#     k = int(sys.stdin.readline())
#     books.append(list(map(int, sys.stdin.readline().split())))
#
# temp = []
# for i in range(1, N+1):
#     for j in range(M):
#         if len(books[j]) == 0 : pass
#         elif books[j][-1] == i:
#             books[j].pop()

# if len(temp) == N : print('Yes')
# else: print('No')

ans = 'Yes'
for _ in range(M):
    k = int(sys.stdin.readline())
    book = list(map(int, sys.stdin.readline().split()))
    for i in range(k-1):
        if book[i] < book[i+1]:
            ans = 'No'
            break
print(ans)