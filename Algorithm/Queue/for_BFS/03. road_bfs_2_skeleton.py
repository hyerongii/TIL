import sys
from collections import deque
sys.stdin = open('practice_input.txt')


def get_road_move_time(road, n, m):
    dxy = [[1,0], [0,1], [-1,0], [0, -1]]

    visited = [[False] * m for _ in range(n)]

    # 큐 안에는 [x 좌표, y좌표, 이동 시간 ]
    queue = deque([0, 0, 0])
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in dxy:
            # 갈 수 있느 곳이라면 (nx, ny, n_dist) 를 저장한다.
            nx, ny = x + dx, y + dy
            n_dist = dist + 1

            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue

            # 방문한 적이 있는 경우
            if visited[nx][ny]:
                continue

            # 도로가 아닌 경우
            if road[nx][ny] == 0:
                continue

            queue.append((nx, ny, n_dist))
            visited[nx][ny] = True

            if nx == n-1 and ny == m-1:
                return n_dist
    return -1








n, m = map(int, input().split())  # 도로의 크기 n * m 입력 받기
road = [list(map(int, input())) for _ in range(n)]  # 도로 정보 입력

# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)
