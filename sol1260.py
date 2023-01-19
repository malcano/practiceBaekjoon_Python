# solution for 1260
def solution():
    N, M, V = map(int, input().split()) #정점, 간선의 개수, 시작정점 초기화
    graph = [[] for _ in range(N + 1)] # 노드의 간선을 저장할 리스트 (접근 편의성 때문에 0번을 비움)
    visitedDFS = [False for _ in range(N + 1)] # DFS 노드 방문여부를 확인하는 리스트
    visitedBFS = [False for _ in range(N + 1)] # BFS 노드 방문여부를 확인하는 리스트

    for _ in range(M):# 간선의 개수 M만큼 저장
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for _ in graph: #간선 정보를 가진 리스트를 정렬(작은 노드부터 방문해야 하기 떄문에)
        _.sort()

    DFS(graph, V, visitedDFS)
    print()
    BFS(graph, V, visitedBFS)


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

def BFS(graph:list, v:int, visited:list):
    """
    BFS는 queue 자료구조를 활용한다.
    :param graph: 노드가 연결하는 다른 노드 리스트
    :param v: 노드 번호
    :param visited: 방문 여부를 저장하는 boolean 리스트
    :return: void
    """
    queue = []
    queue.append(v) #첫번째 요소를 큐에 push 하고
    visited[v] = True #방문 큐 처리한다

    while len(queue) !=0: #큐가 빌 때까지 반복한다
        v = queue.pop(0) #큐에서 노드를 꺼내온다
        print(v, end=" ") #노드를 출력한다
        for _ in graph[v]: #해당 노드와 연결된 노드를 확인 (작은 노드부터 방문해야 하기 때문에 graph의 요소는 정렬되어 있어야 한다.)
            if not visited[_]: #방문한 노드가 아니면 일단 큐에 넣는다.
                queue.append(_)
                visited[_] = True # 큐에 넣은 노드는 방문한 노드이니 방문처리 해준다.
        #이 과정을 반복





