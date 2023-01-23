#sol 1436

def solution():
    N = int(input())
    count = 0
    answer= 665

    while  count != N:
        answer+=1;
        num = answer
        while num != 0:
            if num % 1000 == 666:
                count+=1
                break
            num = num//10

    print(answer)


