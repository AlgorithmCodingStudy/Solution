#-*- coding:utf-8 -*-

"""
n개의 컴퓨터와 m개의 신뢰관계가 있다
A가 B를 신뢰하면 B가 A를 해킹 가능하다.
가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터를 오름차순으로 출력

알고리즘: dfs

1. 무식하게 풀어보기
    1. 모든 컴퓨터에 대해 DFS 돌려보기
    2. sorting과 max로 같은 컴퓨터를 오름차순으로 출력
"""
import sys
read = sys.stdin.readline
from collections import deque
n, m = map(int, read().strip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, read().strip().split())
    graph[b].append(a)


def dfs(start):
    stack = deque()
    stack.append(start)
    visit = [False] * (n+1)
    visit[start] = True
    n_com = 1

    while stack:
        node = stack.popleft()
        for nxt in graph[node]:
            if not visit[nxt]:
                stack.append(nxt)
                visit[nxt] = True
                n_com += 1

    return n_com


max_value = 0
max_idx = []
for i in range(1, n+1):
    tmp = dfs(i)
    if max_value < tmp:
        max_value = tmp
        max_idx = [i]
    elif max_value == tmp:
        max_idx.append(i)


print(" ".join(map(str, max_idx)))
