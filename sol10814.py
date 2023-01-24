# sol 10814
import sys
def solution():
    input = sys.stdin.readline
    N = int(input())
    name_list = []

    for _ in range(N):
        age, name = map(str, input().split())
        name_list.append([int(age), name])

    name_list = list(sorted(name_list, key=lambda x : x[0]))

    for _ in name_list:
        print(f"{_[0]} {_[1]}")