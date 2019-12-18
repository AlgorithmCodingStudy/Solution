#-*- coding:utf-8 -*-

"""
1697 숨바꼭질

수빈이는 N(0 <= N <= 100000)
동생은 K(0 <= K <= 100000)
1초후 N+1 or N-1 or 2*N
몇 초안에 찾을 수 있을까

알고리즘: BFS 최단경로

1. 3가지 경우를 기반으로 BFS를 작동한다.
2. 현재 노드가 K면 멈추고 length를 출력한다.
"""
from queue import Queue
import sys
r = sys.stdin.readline

n, k = map(int, r().strip().split())


def bfs():
    q = Queue()
    # start와 length를 n과 0으로 초기화
    q.put((n, 0))
    visit = {}
    while q.qsize() > 0:
        node, length = q.get()
        if node == k:  # k에 도착하면 length를 리턴
            return length
        visit[node] = True  # 방문한 곳은 True
        for nxt in [node+1, node-1, 2*node]:  # 가능한 경우 3가지를 검사
            if 0 <= nxt <= 100000 and nxt not in visit:  # 다음 node가 0에서 100000사이에 들어가고 방문하지 않았으면
                q.put((nxt, length+1))  # length에 1을 더해 queue에 put


print(bfs())
