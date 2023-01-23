# sol 1654
import sys
def solution():
    K, N = map(int, input().split()) # K : 가지고 있는 랜선 개수 N: 필요한 랜선 개수
    lines = [int(sys.stdin.readline()) for _ in range(K)]
    start = 1
    end = max(lines)

    while start <= end:
        mid = (start + end)//2
        num = 0
        for line in lines:
            num += line//mid
        if num >= N:
            start = mid+1
        else:
            end = mid-1

    print(end)


