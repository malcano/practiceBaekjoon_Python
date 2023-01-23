# sol 2108
import sys
def solution():
    input = sys.stdin.readline
    get = int(input())
    num_list = []
    dic = {}


    for _ in range(get):
        temp = int(input())
        num_list.append(temp)
        if temp in dic.keys():
            dic.update({temp: dic.get(temp)+1 })
        else:
            dic.update({temp: 1 })
    dic = dict(sorted(dic.items(), key = lambda x : x[0]))
    dic = dict(sorted(dic.items(), key = lambda x : x[1], reverse=True))
    keyList = list(dic.keys())
    valList =list(dic.values())

    num_list.sort()
    print(round(sum(num_list)/len(num_list)))
    print(num_list[len(num_list)//2])

    if len(keyList) >1:
        if valList[0] == valList[1]:
            print(keyList[1])
        else:
            print(keyList[0])
    else: print(keyList[0])

    print(max(num_list)-min(num_list))