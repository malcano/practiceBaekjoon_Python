#sol 2231

import sys

def solution():
    input = sys.stdin.readline

    N = int(input())

    answer = 0
    indexNumber = 0

    while indexNumber<N:
        indexNumber +=1
        M = indexNumber
        temp=indexNumber
        while temp!=0:
            M += temp%10
            temp = temp//10
        if M==N:
            answer = indexNumber
            break
    print(answer)