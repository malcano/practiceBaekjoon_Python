import sys

# solution for 1260
def solution():
    N, M, V = map(int, input().split()) #정점, 간선의 개수, 시작정점 초기화
    graph = [[] for _ in range(N+1)] # 노드의 간선을 저장할 리스트 (접근 편의성 때문에 0번을 비움)
    visited = [False for _ in range(N+1)] # 노드 방문여부를 확인하는 리스트

    for _ in range(M):# 간선의 개수 M만큼 저장
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for _ in graph: #간선 정보를 가진 리스트를 정렬(작은 노드부터 방문해야 하기 떄문에)
        _.sort()

    print(graph)
    print(visited)

    DFS(graph, V, visited)
    BFS()

def DFS(graph:list, v:int, visited:list):
    """
    DFS는 stack 자료구조를 활용하며, 재귀적으로 탐색한다
    :param graph: 노드가 연결하는 다른 노드 리스트
    :param v: 방문하는 노드 번호
    :param visited: 방문 여부를 저장하는 boolean 리스트
    :return: void
    """
    visited[v] = True # 이번에 방문한 node를 방문한 노드로 변경
    print(v, end=" ") # 방문한 node를 print
    for _ in graph[v]: #방문한 node가 연결하는 node를 탐색
        if not visited[_]:#해당 노드가 방문하지 않은 노드이면
            DFS(graph, _ , visited) #노드 방문

def DFS_Stack(graph, v, visited):
    print(v, end= " ")
    stack = []
    for _ in graph[v]:
        stack.append()




def BFS():

    return




