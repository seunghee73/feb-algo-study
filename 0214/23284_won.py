# 미
# 완
# 성
# 입
# 니
# 다
# 어
# 려
# 워
n = int(input())
cnt = 0
arr = []
for i in range(1, n + 1):
    stack = []
    for j in range(1, n + 1):
        if len(stack) < i:
            stack += [j]
            break
    a = stack.pop()
    arr += [a]
print(arr)