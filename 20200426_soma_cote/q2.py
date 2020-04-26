"""
최고의 팀

각각 관계가 주어지면 같은 그래프는 같은 팀이다.
그 팀을 감싸는 가장 작은 직사각형의 둘레중 최댓값을 구하자.

알고리즘: DFS

1. DFS를 통해 같은 팀끼리 묶는다.
2. 팀을 하나씩 가져오며
    1. x의 최댓값 - x의 최솟값
    2. y의 최댓값 - y의 최솟값
    3. 둘레를 구한다.
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
pos = [list(map(int, read().split())) for _ in range(n)]
graph = {i: set() for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].add(b)
    graph[b].add(a)


def dfs(sx):
    stack = [sx]
    visit = {sx: True}
    global_visit[sx] = True

    while stack:
        node = stack.pop()

        for nxt in graph[node]:
            if nxt not in visit:
                stack.append(nxt)
                visit[nxt] = True
                global_visit[nxt] = True

    return list(visit.keys())


teams = []
global_visit = {}
for i in range(1, n+1):
    if i not in global_visit:
        teams.append(dfs(i))

max_result = 0
for team in teams:
    max_x, min_x, max_y, min_y = 0, 100000001, 0, 100000001
    for i in team:
        x, y = pos[i-1]
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    result = ((max_x-min_x)+(max_y-min_y))*2
    max_result = max(max_result, result)
print(max_result)