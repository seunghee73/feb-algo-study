from itertools import combinations
lst = []

for _ in range(9):
    lst.append(int(input()))
lst.sort()
a = combinations(lst, 7)
for i in a:
    if sum(i)== 100:
        for j in i:
            print(j)
        break
