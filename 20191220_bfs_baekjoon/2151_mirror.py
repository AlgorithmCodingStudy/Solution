#-*- coding:utf-8 -*-

"""
2151 거울 설치

거울을 설치할 건데 한 쪽 문에서 다른 쪽 문을 볼 수 있도록
5
***#*
*.!.*
*!.!*
*.!.*
*#***

#는 문이고 항상 두개
.은 아무것도 없는 곳으로 빛이 통과
!는 거울을 설치할 수 있는 지점
*는 벽

설치해야 할 거울의 최소 개수 출력

알고리즘: BFS

1. 문 두 개 위치 구하기
2. BFS
    1. 문 하나는 start, 하나는 end
    2. 다음에 올수 있는 노드를 추가
        1. 상하좌우
        2. .
        3. !
        4. 현재 노드가 !라면 90도에 있는 노드만 가능
    3. 현재 노드가 end면 mirror를 리턴하며 종료
"""

import sys
read = sys.stdin.readline
from queue import Queue

n = int(read().strip())
map = [list(read().strip()) for _ in range(n)]

# 1. 문 두 개 위치 구하기
door = []
for i, row in enumerate(map):
    for j, v in enumerate(row):
        if v == '#':
            door.append((i, j))


def bfs(start, end):
    def next_direction(x, y, direction):
        if map[x][y] == '!':
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n \
                        and map[nx][ny] not in path\
                        and map[nx][ny] != '*':

                    direct_xy = (direction[0] + dx, direction[1] + dy)

                    if direct_xy == (0, 2) or direct_xy == (2, 0):
                        q.put((nx, ny, path + [(nx, ny)], mirror, (dx, dy)))
                    else:
                        q.put((nx, ny, path + [(nx, ny)], mirror + 1, (dx, dy)))

        elif map[x][y] == '.':
            nx, ny = x + direction[0], y + direction[1]
            if 0 <= nx < n and 0 <= ny < n \
                    and map[nx][ny] not in path\
                    and map[nx][ny] != '*':
                q.put((nx, ny, path + [(nx, ny)], mirror, (direction[0], direction[1])))

        elif map[x][y] == '#':
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n \
                        and map[nx][ny] not in path\
                        and map[nx][ny] != '*':
                    q.put((nx, ny, path + [(nx, ny)], mirror, (dx, dy)))

    q = Queue()
    q.put((*start, [], 0, (0, 0)))

    while q.qsize() > 0:
        a, b, path, mirror, direct = q.get()
        if (a, b) == end:
            return mirror

        next_direction(a, b, direct)


print(bfs(door[0], door[1]))
pass