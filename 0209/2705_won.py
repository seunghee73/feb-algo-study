TC = int(input())

for tc in range(TC):
    num = int(input())

    def pal(n):
        if n == 1 or n == 2:
            return n
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 4
        if n % 2:
            return pal((n - 1) // 2) + pal(n - 2)
        else:
            return pal(n + 1)

    print(pal(num))
