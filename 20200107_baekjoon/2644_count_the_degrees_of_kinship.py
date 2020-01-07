"""
2644 촌수계산

촌수를 계산하는 프로그램을 만들면 된다.
촌수는 관계당 1씩 증가한다.

알고리즘: BFS
가장 짧은 길로 가야한다.

1. 촌수 관계로 인접리스트를 만든다.
2. 인접리스트를 기반으로 BFS를 돌린다.
"""

from collections import deque
import sys
read = sys.stdin.readline

n = int(read().strip())
t1, t2 = map(int, read().strip().split())
m = int(read().strip())
adj_list = {t: set() for t in range(n+1)}
for _ in range(m):
    a, b = map(int, read().strip().split())
    adj_list[a].add(b)
    adj_list[b].add(a)


def bfs():
    visit = {}
    q = deque()
    q.append(t1)
    visit[t1] = True

    length = 0
    while q:
        qsize = len(q)

        for _ in range(qsize):
            node = q.popleft()
            if node == t2:
                return length
            visit[node] = True

            for nxt in adj_list[node]:
                if nxt not in visit:
                    q.append(nxt)

        length += 1

    return -1


print(bfs())
