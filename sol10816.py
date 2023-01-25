#sol 10816
import sys
from collections import deque
def solution():
    input = sys.stdin.readline
    N = int(input())
    cardDic = {}
    for number in list(map(int, input().split())):
        if number in cardDic.keys():
            cardDic.update({int(number):int(cardDic.get(number)+1)})
        else: cardDic.update({int(number): 1})

    M = int(input())

    for card_type in list(map(int, input().split())):
        if card_type not in cardDic.keys():
            print(0, end = " ")
        else: print(cardDic.get(card_type), end=" ")