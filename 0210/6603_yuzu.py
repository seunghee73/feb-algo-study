import itertools
import sys

input = sys.stdin.readline

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    k = s[0]
    s = s[1:]

    com = list(itertools.combinations(s, 6))
    for c in com:
        for cc in c:
            print(cc, end = ' ')
        print()
    print()