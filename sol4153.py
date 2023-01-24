#sol 4153

import sys

def solution():
    input = sys.stdin.readline

    while True:
        number = tuple(map(int, sorted(input().split(), key = lambda x: int(x))))
        if number[0] == 0 and number[1] == 0 and number[2] == 0:
            return
        print("right") if number[0]*number[0] + number[1]*number[1] == number[2]*number[2] else print("wrong")
