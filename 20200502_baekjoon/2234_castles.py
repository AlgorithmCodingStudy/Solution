"""
2234 성곽

미로처럼 맵이 주어진다.
주어진 맵에서 구해야하는 것이 3가지이다.
1. 방의 개수
2. 가장 넓은 방의 넓이
3. 벽을 하나 부술때 가장 큰 방의 넓이

알고리즘: DFS, 브루트포스

1. DFS로 각방의 개수와 넓이를 다 구한다.
2. DFS를 다시 돌며 인접한 방이 어딘지 그래프를 만든다.
3. 인접한 방끼리 모두 더해보며 가장 큰 방을 구한다.
"""
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
area = [list(map(lambda x: bin(int(x))[2:], read().split())) for _ in range(m)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(sx, sy):
    stack = [(sx, sy)]
    visit = {(sx, sy): True}

    while stack:
        x, y = stack.pop()
        now = '0'*(4-len(area[x][y])) + area[x][y]
        for idx, (dx, dy) in enumerate(dxy):
            nx, ny = x+dx, y+dy
            if not(0 <= nx < m and 0 <= ny < n):
                continue
            if (nx, ny) not in visit and now[idx] == '0':
                stack.append((nx, ny))
                visit[(nx, ny)] = True

    return visit


global_visit = {}
castles = []
max_room = 0
for i in range(m):
    for j in range(n):
        if (i, j) not in global_visit:
            castles.append(dfs(i, j))
            global_visit.update(castles[-1])
            max_room = max(max_room, len(castles[-1]))

max_2_room = 0
castles.sort(key=len, reverse=True)
for i, castle1 in enumerate(castles):
    for j, castle2 in enumerate(castles):
        if i >= j: continue
        for a, b in castle1.keys():
            for dx, dy in dxy:
                na, nb = a+dx, b+dy
                if (na, nb) in castle2:
                    room_2 = len(castle1) + len(castle2)
                    max_2_room = max(room_2, max_2_room)
print(len(castles))
print(max_room)
print(max_2_room)
