#-*- coding:utf-8 -*-

"""
2206 벽 부수고 이동하기

(1, 1)에서 (N, M)까지 이동한다.
만약 벽을 부수고 이동할 때 더 짧은 경로가 된다면 벽을 하나까지 부술 수 있다.

최단 거리를 출력하라

알고리즘: BFS

1. 일단 벽을 부수지 않고 최단경로를 구해보자.
"""
from collections import deque
import sys
read = sys.stdin.readline
n, m = map(int, read().strip().split())
matrix = [list(map(int, read().strip())) for _ in range(n)]


def bfs():
    q = deque()
    q.append((0, 0, True))
    check_visit = [[0 for _ in range(m)] for _ in range(n)]
    check_visit[0][0] = 1

    def next_node():
        arr = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if break_flag:
                if (check_visit[nx][ny] == 0 or check_visit[nx][ny] == check_visit[x][y] + 1) and matrix[nx][ny] == 0:
                    arr.insert(0, (nx, ny, True))
                    check_visit[nx][ny] = check_visit[x][y] + 1
            else:
                if (check_visit[nx][ny] == 0 or check_visit[nx][ny] == check_visit[x][y] + 1) and matrix[nx][ny] == 0:
                    arr.insert(0, (nx, ny, False))
                    check_visit[nx][ny] = check_visit[x][y] + 1
            if check_visit[nx][ny] == 0 and matrix[nx][ny] == 1:
                arr.append((nx, ny, False))
                check_visit[nx][ny] = check_visit[x][y] + 1
        return arr

    while q:
        x, y, break_flag = q.popleft()
        if x == n-1 and y == m-1:
            return check_visit[x][y]
        q.extend(next_node())
    return -1


print(bfs())
