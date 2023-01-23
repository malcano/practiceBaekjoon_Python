#sol 2164

import sys
from collections import deque

def solution():
    input = sys.stdin.readline

    N = int(input())

    card = [ number+1 for number in range(N)]
    card = deque(card)

    while len(card) !=1:
        card.popleft()
        card.append(card.popleft())

    print(card.popleft())