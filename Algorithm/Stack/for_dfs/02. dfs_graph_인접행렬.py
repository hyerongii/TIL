# 점과 점이 연결되어 있는지? 여부 불러올때 씀
# current:탐색 정점
# adjMatrix: 인접 행렬
# visited: 방문 체크 리스트
def dfs(current, adj_matrix, visited):
    visited[current] = True  # 현재 정점을 방문했다고 표시

    for i in range(len(adj_matrix)):  # 모든 정점에 대해
        # 현재 정점과 연결되어 있고, 아직 방문하지 않은 정점이라면
        if adj_matrix[current][i] and not visited[i]:  
            dfs(i, adj_matrix, visited)  # 그 정점을 방문

# 정점 수: N
N = 5
# 인접 행렬asdasdasdasd
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

# 방문 체크 배열 초기화
visited = [False] * N  # 모든 정점을 아직 방문하지 않았다고 표시

# 시작 정점: 0
dfs(0, adj_matrix, visited)  # 깊이 우선 탐색 시작


# 인접 행렬 만드는법
V, E = map(int, input().split())
adjL = [[] for _ in range(V+1)]
arr = list(map(int, input().split()))
for i in range(E):
    v, w = arr[i*2], arr[i*2+1]
    adjL[v].append(w)
    adjL[w].append(v)