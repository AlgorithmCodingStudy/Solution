"""
1753 최단경로

가중치가 있는 그래프가 주어질 모든 정점으로의 최단 경로를 구해라

알고리즘: 다익스트라 알고리즘

1. 그래프 만들기
2. heapq 선언
3. 출발점을 0 다른 정점들은 inf로 초기화
4. 거리가 제일 가까운 것 부터 빼면서
    1. 목표 정점의 현재 거리 vs 간선 가중치 + 출발 정점의 현재 거리
"""
import heapq
import sys
read = sys.stdin.readline

V, e = map(int, read().split())
k = int(read())
graph = {i: [] for i in range(1, V+1)}
for _ in range(e):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

hq = []
heapq.heappush(hq, (0, k))
for i in range(V):
    if i+1 == k: continue
    heapq.heappush(hq, (sys.maxsize, i+1))

d = [sys.maxsize]*(V+1)
d[k] = 0
while hq:
    now_d, i = heapq.heappop(hq)
    if d[i] < now_d: continue

    for v, w in graph[i]:
        if now_d + w < d[v]:
            d[v] = now_d + w
            heapq.heappush(hq, (d[v], v))

for distance in d[1:]:
    if distance == sys.maxsize: distance = 'INF'
    print(distance)
