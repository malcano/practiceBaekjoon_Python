import sys


def solution():
    N, M = map(int, input().split())



    chessboard = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
    print([_ for _ in chessboard])
    # for _ in chessboard:
