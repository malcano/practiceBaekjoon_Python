# sol 2798

import sys
from collections import deque
def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    card = []
    most_close = 0

    card = list(map(int,input().split()))

    card.sort()
    card = deque(card)

    while len(card) >= 3:
        firstCard = card.popleft()
        secondindex = 0
        thirdindex = 1
        for sec in range(secondindex,len(card)-1):
            for trd in range(thirdindex, len(card)):
                sum = firstCard + card[sec] + card[trd]
                if sum > M:
                    continue
                most_close = sum if most_close < sum else most_close

    print(most_close)