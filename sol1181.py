#sol 1181

def solution():
    """
    알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

    1) 길이가 짧은 것부터
    2) 길이가 같으면 사전 순으로
    """
    N = int(input()) # 단어의 개수를 N에 저장
    get_word = {} # 같은 단어가 여러 번 입력되는 경우에는 한 번만 출력하기 위해서 dictionary 사용

    for _ in range(N):
        keyword = input()
        get_word.update({keyword: len(keyword)}) # 키워드를 key, 키워드의 길이를 value로 저장, 딕셔너리이기 때문에 중복되어 저장되지 않는다

    get_word = dict(sorted(get_word.items(), key= lambda x: x[0])) # 우선 키워드를 사전 순으로 정렬, 길이가 같은 애들을 미리 사전 순으로 만들어 놓아야 한다
    get_word = dict(sorted(get_word.items(), key= lambda x: x[1])) # 길이가 짧은 순서로 정렬

    for _ in get_word:
        print(_)