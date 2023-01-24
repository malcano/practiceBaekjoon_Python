import importlib # dynamic import

def load_module(module_number):
    mod = importlib.import_module("sol"+str(module_number))
    return mod

# 모듈을 동적으로 호출
# solution number만 변경하면 main을 실행할 수 있음

#Do not Edit this code!
if __name__ == '__main__':

    #######################
    solution_number = 4153 # input solution number
    #######################
    print(f"console activate, solution num: {solution_number}") #몇 번 문제 푸는지 알려주는 콘솔 프린트 추가

    getattr(load_module(solution_number), f'solution')()






