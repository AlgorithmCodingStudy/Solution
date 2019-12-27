#-*- coding:utf-8 -*-

"""
1389 케빈 베이컨의 6단계 법칙

몇 사람을 거치면 아는 사람일까?
가장 작은 사람이 우승

n은 사람수
m은 관계수

"""
from collections import deque
import sys
read = sys.stdin.readline
n, m = map(int, read().strip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, read().strip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visit = {start: True}

    while q:
        node, length = q.popleft()
        if node == end:
            return length
        visit[node] = True
        for nxt in graph[node]:
            if nxt not in visit:
                q.append((nxt, length+1))


result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(0, n):
    for j in range(i, n):
        if i != j:
            tmp = bfs(i+1, j+1)
            result[i][j] = tmp
            result[j][i] = tmp

min_value = 10000000
min_idx = -1
for i, v in enumerate(result):
    sum_value = sum(v)
    if sum_value < min_value:
        min_value = sum_value
        min_idx = i+1

print(min_idx)
