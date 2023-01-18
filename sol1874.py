import sys

def solution():
    stack = []
    getNum = [_ for _ in range(1,int(input())+1)]
    arr = [] # 만들어야 하는 수열
    result = []
    for _ in range(len(getNum)):
        arr.append(int(input()))

    while len(arr)!=0:
        if len(stack) == 0: #스택이 비어서 peek할 것이 없을 떄
            if len(getNum)==0:
                result=["NO"]
                break

            stack.append(getNum.pop(0))
            result.append('+')
        if arr[0] != stack[len(stack)-1]:# peek 했는데 아니면 stack에 push
            if len(getNum)==0:
                result=["NO"]
                break
            stack.append(getNum.pop(0))
            result.append('+')
        else: #
            stack.pop(len(stack)-1)
            arr.pop(0)
            result.append('-')

    for _ in result:
        print(_)

solution()