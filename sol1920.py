# sol 1920
def solution(): #python 내장 함수를 활용한 풀이
    N = int(input())
    A = set(map(int,input().split()))
    M = int(input())
    isAmember = list(map(int,input().split()))

    for _ in isAmember:
        if _ in A:
            print(1)
        else: print(0)

def solution(): # 문제의 의도한 바
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    M = int(input())
    isAmember = list(map(int,input().split()))

    for member in isAmember:
        left = 0
        right = len(A)-1
        exist = False

        while left <= right:
            mid = (left+right)//2
            if member == A[mid]:
                exist = True
                print(1)
                break;
            if member > A[mid]:
                left = mid+1
            else:
                right = mid-1

        if not exist: print(0)


