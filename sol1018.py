import sys
# solution #1018
def solution():
    N, M = map(int, input().split())
    board = []
    color = ''
    resultList = []
    whiteFirst = 'WBWBWBWB'
    blackFirst = 'BWBWBWBW'

    for _ in range(N):
        board.append(input())
    nLimit = N-8+1
    mLimit = M-8+1

    result1 = 0
    result2 = 0
    firstblock = 'B'

    # chessboard = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
    for n in range(nLimit):
        for m in range(mLimit):
            result1 = 0
            result2 = 0

            for i in range(8):
                for j in range(8):
                    if i%2 == 0:
                        if board[n+i][m+j] != whiteFirst[j]:
                            result1 += 1
                        if board[n+i][m+j] != blackFirst[j]:
                            result2 +=1
                    else:
                        if board[n+i][m+j] != blackFirst[j]:
                            result1 += 1
                        if board[n+i][m+j] != whiteFirst[j]:
                            result2 +=1
            resultList.append(result1)
            resultList.append(result2)

    print(min(resultList))
