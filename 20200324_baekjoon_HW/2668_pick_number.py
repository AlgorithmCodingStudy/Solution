"""
2668 숫자고르기

1234567
3115546

위 예제에서 135를 뽑으면 315로 위아래 집합이 일치한다.
이중 가장 큰 것을 출력하라.

알고리즘: DFS

1. 1-7반복
    1. 1 아래 숫자를 골라서 그 수를 stack에 넣기
    2. 넣을 수는 방문하지 않았어야 한다.
1. 방문한 곳을 출력
"""

import sys
read = sys.stdin.readline

n = int(read())
graph = {idx+1: int(read()) for idx in range(n)}


def dfs_all():
    def dfs(start):
        visit = {}
        stack = [start]
        first = True
        while stack:
            now = stack.pop()
            if now == start and not first:
                return list(visit.keys())
            if now not in visit:
                stack.append(graph[now])
                visit[now] = True
            first = False

        return []

    v = set()
    for i in range(n):
        for get in dfs(i+1):
            v.add(get)

    return list(sorted(v))


result = dfs_all()
print(len(result))
for s in result:
    print(s)

