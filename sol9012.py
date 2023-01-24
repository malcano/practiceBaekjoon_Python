#sol 9012

import sys
from collections import deque
def solution():
    input = sys.stdin.readline
    N = int(input())

    for _ in range(N):
        stringQ = deque(input())
        stackPS = []
        isVPC = True

        while len(stringQ) != 1:
            target = stringQ.popleft()
            if target == '(':
                stackPS.append(target)
                continue
            if len(stackPS) == 0:
                isVPC = False
                break
            stackPS.pop(len(stackPS)-1)

        print("YES") if isVPC==True and len(stackPS)==0 else print("NO")
