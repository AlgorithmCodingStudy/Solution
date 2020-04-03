"""
1707 이분그래프

정점의 집합을 둘로 나누었을때 정점끼리 인접하지 않는다면 그걸 이분그래프라고 한다.

알고리즘: DFS

"""

import sys
read = sys.stdin.readline


def bfs():
    q = [1]
    g = [[1], []]
    visit = {}
    group = True
    while q:
        new_q = []
        for now in q:
            for nxt in graph[now]:
                if (now, nxt) not in visit:
                    visit[(now, nxt)] = True
                    visit[(nxt, now)] = True
                    new_q.append(nxt)
                    if nxt in g[group]:
                        return 'NO'
                    g[not group].append(nxt)
        group = not group
        q = new_q
    return 'YES'


for _ in range(int(read())):
    v, e = map(int, read().split())
    edges = [list(map(int, read().split())) for _ in range(e)]

    graph = {i+1:[] for i in range(v)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    print(bfs())
