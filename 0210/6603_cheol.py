lotto = [0] * 6

def go(idx, start, n, m):
    if idx == 6:
        print(' '.join(map(str, lotto)))
        return

    for i in range(start, len(n)):
        lotto[idx] = n[i]
        go(idx + 1, i + 1, n, m)


while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break
    go(0, 0, num[1:], 6)
    print()