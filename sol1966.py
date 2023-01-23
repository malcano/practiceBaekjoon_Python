# sol 1966
from collections import deque
def solution():
    for _ in range(int(input())):
        N, M = map(int, input().split()) #N: 문서의 개수 , M: 궁금한 문서 몇 번쨰?
        printQ = deque(list(map(int, input().split())))
        indexQ = deque(list(range(N)))
        count = 0
        targetIndex = M

        while printQ:
            imp = max(printQ)
            if printQ[0] == imp:
                printQ.popleft()
                index = indexQ.popleft()
                count+=1
                if index == targetIndex:
                    break
            else :
                printQ.append(printQ.popleft())
                indexQ.append(indexQ.popleft())

        print(count)


