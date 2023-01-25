#sol 10828
import sys
import time
def solution():
    input = sys.stdin.readline
    stack_list = []

    N = int(input())
    for _ in range(N):
        start = time.time()
        command_buf = list(map(str, input().split()))
        command = command_buf[0]
        if command == 'push':
            stack_list.append(int(command_buf[1]))
        elif command == 'pop':
            print(stack_list.pop()) if len(stack_list) != 0 else print(-1)
        elif command == 'size':
            print(len(stack_list))
        elif command == 'empty':
            print(1) if len(stack_list) == 0 else print(0)
        elif command == 'top':
            print(stack_list[- 1]) if len(stack_list) != 0 else print(-1)
        print(time.time() - start)
