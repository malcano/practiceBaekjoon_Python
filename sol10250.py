# sol10250
import sys
from collections import deque

def solution():
    index = sys.stdin.readline

    T = int(index())

    for _ in range(T):
        H, W, N = map(int, input().split())
        floor = [deque() for _ in range(H)]
        roomnum = 0

        for human in range(0, N):
            floor[human%H].append('0')
            roomnum = (human%H+1)*100+len(floor[human%H])
        print(roomnum)