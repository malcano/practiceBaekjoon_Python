import sys
def solution():
    input = sys.stdin.readline
    a,b = map(int, input().split())

    print(gcd(a,b))
    print(lcm(a,b))

def gcd(a: int , b: int):
    if max(a,b)%min(a,b)== 0:
        return min(a,b)
    else: return gcd(min(a,b), max(a,b)%min(a,b))

def lcm (a : int, b: int ):
    return int(a*b/gcd(a,b))