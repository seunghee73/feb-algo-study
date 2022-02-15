import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for _ in range(m):
    a = int(input())
    b = list(map(int, input().split()))
    ans = 'Yes'
    for i in range(a-1):
        # 책 더미의 위쪽부터 오름차순 정렬이 아닐 경우 No
        if b[i] < b[i+1]:
            ans = 'No'
            break
    if ans == 'No':
        break
print(ans)