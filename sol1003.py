#solution 1003
def solution():
    """
    이 문제는 얼핏 보면 재귀를 돌려 푸는 문제인 것 같지만, 재귀로 일일이 풀면 시간제한에 걸리는 문제이다.
    DP로 풀어야 하는 문제이며, 함정에 속지 말자.
    """
    zero_save =[1, 0] # 값이 0, 1일 때 0이 호출되는 경우를 미리 리스트에 저장한다.
    one_save = [0, 1] # 값이 0,1일 때 1이 호출되는 경우를 미리 리스트에 저장한다.
    var_count = int(input()) # 받을 케이스 수를 저장
    target = [] # 케이스를 저장할 리스트

    for arg in range(var_count):
        target.append(int(input())) # 케이스 값을 리스트에 저장

    for arg in target:# 케이스를 하나씩 꺼내온다
        if arg > len(zero_save):# 해당 케이스에 대한 값이 리스트에 저장되어 있지 않다면
            for index in range(len(zero_save), arg + 1):#없는 케이스를 만들어주자
                # 0, 1의 호출 횟수는 피보나치 수열과 같은 패턴을 지닌다.
                # zero save와 one save에 케이스를 미리 저장해주자
                zero_save.append(zero_save[index - 1] + zero_save[index - 2])
                one_save.append(one_save[index-1]+one_save[index-2])
        print(f"{zero_save[arg]} {one_save[arg]}")#저장되어 있는 케이스를 꺼내온다.

