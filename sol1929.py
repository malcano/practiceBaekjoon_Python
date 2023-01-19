# sol 1929
def solution():
    """
    소수구하기
    '에라토스테네스의 체'라는 방식을 사용한다
    """
    N, M = map(int, input().split())
    isPrime = [False, False] + [True]*(M-1)# M이하 수가 소수인지 여부를 검사하기 위해 True로 초기화된 숫자 리스트를 만든다

    for _ in range(2,M+1):
        if isPrime[_]: # 만일 소수라면
            for notPrime in range(_*2,M+1,_): #해당 소수의 배수를 접근하여 False로 변경
                isPrime[notPrime] = False

    [print(_) for _ in range(N, len(isPrime)) if isPrime[_] is True] #prime이 true일 때만 값을 print한다