#sol 11497 그리디

def solution():
    number_of_testcase = int(input())
    woodList = []

    for case in range(number_of_testcase):
        number_of_wood = int(input())
        woodList = list(map(int, input().split()))
        result = 0
        woodList.sort(reverse=True)
        for index in range(number_of_wood-2):
            result = max(result, abs(woodList[index]-woodList[index+2]))
        print(result)