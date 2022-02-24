def comparison(N):
    cntA = a.count(N) # 들어온 숫자의 갯수 측정
    cntB = b.count(N)

    if cntA > cntB: # 같으면 무승부
        return 'A'
    elif cntA < cntB:
        return 'B'
    else:
        if N == 0: #다 비교해서 0이 나오면 무승부
            return 'D'
        else:
            return comparison(N - 1) # 들어오는 숫자 -1 해서 재귀로 넣어주기
        #반복문 사용하면 너무 길엉


T = int(input())
for tc in range(T):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.remove(a[0]) #카드 숫자 제거
    b.remove(b[0])
    maxA = max(a) # 제일 큰 카드 저장
    maxB = max(b)

    if maxA != maxB: # 비교하여 a b 출력
        if maxA > maxB:
            print('A')
        else:
            print('B')
    else: # 같은 경우는 아랫놈들 비교 필요 comparison  함수 사용
        result = comparison(maxA)
        print(result)
