#-*- coding:utf-8 -*-

"""
2667 단지번호붙이기

0은 집이 없는 곳, 1은 집이 있는 곳
1이 이어져있으면 같은 단지
단지 개수를 출력하고
각 단지의 아파트 수를 출력하라.

알고리즘: DFS로 보이나 저번에 풀어봤으므로 BFS로 도전

1. Queue에 넣는 방식을 (node, length)로 한다.
"""
import sys
r = sys.stdin.readline
from queue import Queue

n = int(input())
apt_map = [list(map(int, r().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = Queue()
    q.put((x, y))
    length = 0

    while q.qsize() > 0:
        a, b = q.get()
        if apt_map[a][b]:
            length += 1
            apt_map[a][b] = 0
            for nx, ny in zip(dx, dy):
                if 0 <= a+nx < n and 0 <= b+ny < n:
                    q.put((a+nx, b+ny))

    return length


result = []
for i, row in enumerate(apt_map):
    for j, v in enumerate(row):
        if v:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for v in result:
    print(v)
