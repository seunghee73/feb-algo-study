import sys

read = sys.stdin.readline

N, M = map(int, read().split())
answer = 'Yes'

for _ in range(M):

    book_num = int(read())
    books = list(map(int, read().split()))

    for i in range(0, book_num - 1):
        if books[i] < books[i + 1]:
            answer = 'No'
            break
print(answer)