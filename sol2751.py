#sol 2751

import sys

def solution():
    input = sys.stdin.readline

    N = int(input())
    num_list = []
    for _ in range(N):
        num_list.append(int(input()))

    num_list.sort()

    for _ in num_list:
        print(_)