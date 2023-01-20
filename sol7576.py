#sol7576
import sys
from collections import deque
def solution():
    """BFS 문제이다. BFS는 queue를 활용한다."""
    input = sys.stdin.readline # input을 내장 함수로 쓰면 시간초과난다고 한다  sys.stdin.readline을 input으로 써보도록 하자

    M, N = map(int, input().split()) # 두 값을 받는다.
    tomato_box = [] # 토마토 박스는 리스트에 저장
    queue = deque() #BFS를 위해 큐를 선언

    dx, dy = [-1,1,0,0], [0,0,-1,1] # 방향은 상, 하, 좌, 우 이렇게 네 가지 경우가 있다. 네 경우에 대해 검사할 수 있도록 다음과 같이 리스트를 선언
    tomato_box = [list(map(int, input().split())) for _ in range(N)] # 토마토를 박스에 담자
    count = 0

    for i in range(N):
        for j in range(M): # 토마토 박스를 검사한다
            if tomato_box[i][j] == 1:# 토마토 상태가 1인 좌표를 큐에 저장한다.
                queue.append([i, j])

    while len(queue) != 0:#큐가 빌 때까지 반복한다
        qx, qy = map(int, queue.popleft()) # 큐에서 값을 하나 꺼내온다
        for find in range(4): #네 방향을 탐색한다
            nearX = qx+dx[find]
            nearY = qy+dy[find]
            if 0 <= nearX < N and 0<= nearY<M and tomato_box[nearX][nearY] == 0:#인접한 토마토가 범위 안에 있고, 토마토가 익지 않은 토마토라면
                queue.append([nearX, nearY]) # 큐에 해당 토마토를 넣는다
                tomato_box[nearX][nearY] = tomato_box[qx][qy]+ 1 # 인접 토마토를 익힌다  +1을 함으로써 날짜를 알 수 있다

    for i in tomato_box: #토마토 박스에 익지 않은 토마토가 있는지를 확인한다.
        for j in i:
            if j==0:
                print(-1)
                return
        count = max(count, max(i)) #가장 큰 값을 출력한다
    print(count-1) #첫 시작이 1이므로