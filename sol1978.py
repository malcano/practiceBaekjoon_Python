# sol 1978

def solution():
    case = int(input())
    num_list = list(map(int, input().split()))
    isPrime = [False, False] + [True]*(max(num_list)-1)
    count = 0

    for _ in range(2, max(num_list) + 1):
        if isPrime[_]:  # 만일 소수라면
            for notPrime in range(_ * 2, max(num_list)  + 1, _):  # 해당 소수의 배수를 접근하여 False로 변경
                isPrime[notPrime] = False
    for _ in num_list:
        if isPrime[_]:
            count+=1

