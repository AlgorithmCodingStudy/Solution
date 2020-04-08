"""
1916 최소비용 구하기

n개의 도시와 m개의 버스가 있다.
a번째 도시에서 b번째 도시로 가는 버스 최소 비용을 구하라.

알고리즘: 다익스트라

1. 그래프를 그린다.
2. 출발지점은 d가 0 나머지는 inf로 초기화
3. heapq에 담는다.
4. 하나씩 꺼내면서 도착지의 현재 d와 출발지의 현재 d + weight를 비교
"""
import heapq
import sys
read = sys.stdin.readline

n = int(read())
m = int(read())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

start, end = map(int, read().split())
ds = [sys.maxsize]*(n+1)
ds[start] = 0
hq = []
heapq.heappush(hq, (0, start))

while hq:
    d, u = heapq.heappop(hq)
    if ds[u] < d:
        continue

    for v, w in graph[u]:
        c = ds[u]+w
        if c < ds[v]:
            ds[v] = c
            heapq.heappush(hq, (c, v))

print(ds[end])
