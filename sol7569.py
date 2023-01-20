#sol 7569

import sys
from collections import deque
def solution():
    input = sys.stdin.readline

    M, N, H = map(int, input().split())
    tomato_box_block = []

    for _ in range(H):
        tomato_box = [list(map(int, input().split())) for _ in range(N)]
        tomato_box_block.append(tomato_box)
    count = 0
    queue = deque([])

    dx, dy, dz = [-1, 1, 0 ,0, 0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_box_block[i][j][k] == 1:
                    queue.append([i,j,k])

    while queue:
        qx, qy, qz = map(int, queue.popleft())
        for find in range(6): #여섯 방향을 탐색
            nearX = qx+dx[find]
            nearY = qy+dy[find]
            nearZ = qz+dz[find]
            if 0<= nearX < H and 0<= nearY < N and 0<= nearZ < M and tomato_box_block[nearX][nearY][nearZ]==0:
                queue.append([nearX, nearY,nearZ])
                tomato_box_block[nearX][nearY][nearZ] = tomato_box_block[qx][qy][qz]+1

    for i in tomato_box_block: #토마토 박스에 익지 않은 토마토가 있는지를 확인한다.
        for j in i:
            for k in j:
                if k==0:
                    print(-1)
                    return
            count = max(count, max(j)) #가장 큰 값을 출력한다

    print(count-1)