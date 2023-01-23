#sol 1085
def solution():
    x,y,w,h = map(int, input().split())

    minX = min(x, abs(w-x))
    minY = min(y, abs(h-y))

    print(min(minX,minY))




