import sys


def solution():
    N, M = map(int, input().split())
    board = []
    for _ in range(M):
        board.append(input())

    #chessboard = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
    print([_ for _ in board])
    # for _ in chessboard:
