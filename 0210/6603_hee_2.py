while True:
    data = list(map(int, input().split()))
    if data == [0]:
        break

    def nCr(n, ans, r):
        if n == data[0]:
            if len(ans) == r:
                temp = [i for i in ans]
                new_temp = [str(i) for i in temp]
                print(' '.join(new_temp))
            return

        ans.append(data[n+1])
        nCr(n + 1, ans, r)
        ans.pop()
        nCr(n + 1, ans, r)

    nCr(0, [], 6)
    print()