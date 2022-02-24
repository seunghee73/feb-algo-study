def palindrome(N):
    if N <= 1: # 1일때 1 넘기기
        return 1

    if tmp[N] > -1: #w재귀 돌때 바로바로 뭔가를 연산을 줄여주는듯? 코드 없애거나 부등호 바꾸거나 해봤는데 이것만 시간초과 안남
        return tmp[N]

    tmp[N] = 1 # 최소 1 이상이니 1로 초기화
    for i in range(N): #0 ~ N
        if (N - i) % 2 == 1: #  N-i가 홀수이면 넘어간당
            continue 
        tmp[N] += palindrome((N - i) // 2) # p(7) 경우 1+p(3)+p(2)+p(1)

    return tmp[N]
    
tmp = [-1 for i in range(1001)] # 안겹치게 -1로 tmp 초기화 (1~1000)

T = int(input()) # 인풋값

for _ in range(T):
    N = int(input())
    print(palindrome(N))