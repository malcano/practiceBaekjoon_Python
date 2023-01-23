import sys

def solution():

    while True:
        n = input()
        is_pel = True
        if n == '0':
            return

        for index in range(int(len(n)/2)):
            if n[index] == n[len(n)-1-index]:
                continue
            else: is_pel=False

        if is_pel == True:
            print("yes")
        else: print("no")
