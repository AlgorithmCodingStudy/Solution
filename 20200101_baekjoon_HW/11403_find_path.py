#-*- coding:utf-8 -*-

"""
11403 경로 찾기

인접행렬이 주어지면 i에서 j로 가는 경로가 있으면 1로 없으면 0으로 출력하라.

알고리즘: DFS/BFS

1. 1인곳을 찾아 BFS 돌리며 방문하는 곳을 전부 1로 칠하자.
"""
from collections import deque
import sys
read = sys.stdin.readline

n = int(read().strip())
adjmat = [list(map(int, read().strip().split())) for _ in range(n)]


def bfs(start, target):
    q = deque()
    q.append(start)
    visit = {}

    while q:
        qsize = len(q)
        for _ in range(qsize):
            i = q.popleft()

            for j, v in enumerate(adjmat[i]):
                if v == 1 and (i, j) not in visit:
                    adjmat[i][j] = 1
                    visit[(i, j)] = True
                    q.append(j)
                    if j == target:
                        adjmat[start][target] = 1
                        return


for x in range(n):
    for y in range(n):
        if adjmat[x][y] == 0:
            bfs(x, y)

for line in adjmat:
    print(" ".join(map(str, line)))
