# 이 미로문제는 일반적으로 BFS 로 푸는게 맞습니다.
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(x, y, cnt):
    global min_cnt

    if x == N-1 and y == M-1:
        min_cnt = min(min_cnt, cnt)
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

        if visited[nx][ny]: continue

        if not road[nx][ny]: continue

        # DFS 이니까
        # nx, ny를 방문했다 치고 DFS 로 보낸다.
        visited[nx][ny] = True
        dfs(nx, ny, cnt+1)
        visited[nx][ny] = False



# 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

min_cnt = N*M
# min_cnt = float('inf')
visited[0][0] = True

"""
DFs 파라미터 어떻게 정하죠 ?
1. 종료 조건이 될 수 있는 변수, 재귀함수를 종료시키는 변수 => (좌표)
2. 결국 내가 얻으려는 누적값 ( 이동 거리 )
"""
dfs(0, 0, 0)
