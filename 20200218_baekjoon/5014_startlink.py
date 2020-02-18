"""
5014 스타트링크

F층인 건물에서 S층에서 G층으로 가기 위한 최소 횟수를 출력
U만큼 위로 D만큼 아래로 갈 수 있다.
1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000

알고리즘: BFS

1. U나 D가 0인데 갈수 없는 방향이면 false
2. bfs
    1. 위랑 아래로 계속 퍼지기
    2. 1000000이 넘으면 못가는 곳이므로 return
    3. 목적지 도착하면 true
    4. 전부 다 돌았으면 false
"""
from collections import deque
import sys
read = sys.stdin.readline

f, s, g, u, d = map(int, read().strip().split())

if (u == 0 and g > s) or (d == 0 and g < s):
    print("use the stairs")
    sys.exit(0)


def bfs():
    q = deque([s])
    visit = {}
    cnt = 0
    while q:
        qsize = len(q)

        for _ in range(qsize):
            now = q.popleft()
            if now == g:
                return cnt

            now_u = now + u
            now_d = now - d
            if now_u <= f and now_u not in visit:
                visit[now_u] = True
                q.append(now_u)
            if now_d >= 1 and now_d not in visit:
                visit[now_d] = True
                q.append(now_d)

        cnt += 1

    return "use the stairs"


print(bfs())
