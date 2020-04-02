"""
4386 별자리 만들기

별들을 이어서 별자리를 만들 예정이다.
선을 이을 때 거리만큼 비용이 든다 할때
별자리를 만드는 최소 비용을 구하라

알고리즘: mst

1. 별들을 입력 받는다.
2. 입력 받은 별들로 부터 edge들을 모두 구한다.
3. 오름차순으로 정렬
4. 하나씩 가져온다.
    1. find-union
        1. from의 root와 to의 root를 찾는다. find
        2. 같지 않다면 union
        3. 같으면 continue
    2. 스패닝트리에 추가되었다면 거리 더하기
5. 출력
"""
from itertools import combinations
import sys
read = sys.stdin.readline

n = int(read())
stars = [list(map(float, read().split())) for _ in range(n)]

edges = []
for s1, s2 in combinations(list(range(n)), 2):
    x1, y1 = stars[s1]
    x2, y2 = stars[s2]
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    edges.append([s1, s2, distance])
edges = sorted(edges, key=lambda f: f[-1])

p = [-1]*n


def find(v):
    if p[v] < 0:
        return v
    p[v] = find(p[v])
    return p[v]


def union(v1, v2):
    p[v2] = v1

result = 0
for from_, to_, weight in edges:
    from_p, to_p = find(from_), find(to_)
    if from_p == to_p:
        continue
    union(from_p, to_p)
    result += weight
print(result)
