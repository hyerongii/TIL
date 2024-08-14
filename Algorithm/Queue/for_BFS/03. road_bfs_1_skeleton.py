import sys
from collections import deque
sys.stdin = open('practice_input.txt')


def get_road_move_time(road, n, m):
    # 델타탐색
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # 이해하기 쉽게 0,0을 시작점으로 잡을거다
    # 도착지점을 n-1, m-1
    queue = deque([0, 0])

    # visited 겸 복사하기로 했죠. 각 좌표마다 걸리는 최소 이동 시간을 저장하는 2차원 리스트를 복사
    # 꼭 -1이 아니여도 됩니다.
    distance = [[-99] * m for _ in range(n)]
    distance[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 범위 검사하고
            if 0 > nx or nx >= n or 0 > ny or ny >= m: continue
            # 갈 수 있는 길인지 확인하고
            if road[nx][ny] == 0: continue
            # 방문했던 적이 있는 지 확인하고
            if distance[nx][ny] != -99: continue
            # 위에 다 통과했으면, 큐에 집어넣고,
            queue.append((nx, ny))
            # distance 변수에 현재 위치까지 오는데 걸리는 시간 + 1을 저장
            distance[nx][ny] = distance[x][y] + 1

            if nx == n-1 and ny == m-1:
                return distance[nx][ny]

    # 이거 -1도 외우면 안된다.
    # 도착하지 못한 경우에는 -1을 출력하세요~
    # -9999
    return -9999









n, m = map(int, input().split())  # 도로의 크기 n * m 입력 받기
road = [list(map(int, input())) for _ in range(n)]  # 도로 정보 입력

print(road)
# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)
