import sys

def solution():
    input = sys.stdin.readline
    number = int(input())
    count = 1
    index = 1

    while index < number:
        index = index + count*6
        count +=1

    print(count)