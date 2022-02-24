from itertools import product

n = int(input())
if n == 1:
    print(1)

# 같은것을 포함한 순열을 이용해 -1(pop)과 1(push)로 구성된 순열 리스트 구성
else:
    l = []
    dataset = [-1, 1]
    for p in product(dataset, repeat=2*(n-1)):
        if sum(p) == 0:
            l.append(p)
# 순열리스트를 순회하면서 -1일땐 pop 1일땐 push 한 결과를 출력
    seq = []
    for ll in l:
        lst = [i + 1 for i in range(n)]
        stack = []
        stack.append(lst.pop(0))
        s = []
        p = 1
        for i in ll:
            if p>0:
                if i == -1:
                    s.append(stack.pop())
                    p -= 1
                else:
                    stack.append(lst.pop(0))
                    p += 1
            else:
                if i == -1:
                    s = []
                    break
                else:
                    stack.append(lst.pop(0))
                    p += 1
        if len(s) != 0:
            s.append(stack.pop())
            seq.append(s)
    for se in seq:
        for see in se:
            print(see, end=' ')
        print()