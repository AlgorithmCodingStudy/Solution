"""
17142 연구소 3

바이러스 몇 개가 있는데 그중 M개를 활성상태로 바꾸려한다.
활성상태가 되면 1초에 한 번 상하좌우로 퍼진다.
모든 빈칸에 바이러스가 퍼지는 시간을 재는데
최소를 구하라.

알고리즘 : BFS, 브루트 포스, 조합

1. 바이러스의 위치와 빈칸의 개수를 조사
2. 그중 M개를 뽑는 조합을 구한다.
3. 조합을 모두 검토
    1. M개에서 출발하는 BFS
    2. visit의 length가 빈칸의 개수와 같다면 끝, 최소 비교
4. 출력
"""
from collections import deque
from itertools import combinations
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
lab, virus, empty = [], [], 0
for a in range(n):
    lab.append(list(map(int, read().strip().split())))
    for b in range(n):
        if lab[a][b] == 2:
            virus.append((a, b))
        elif lab[a][b] == 0:
            empty += 1

if empty == 0:
    print(0)
    sys.exit(0)
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cases = combinations(virus, m)


def bfs(viruses):
    visit, virus_visit = {}, {}
    q = deque(viruses)

    time = 1
    while q:
        qsize = len(q)
        for _ in range(qsize):
            x, y = q.popleft()

            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not(0 <= nx < n and 0 <= ny < n):
                    continue
                if lab[nx][ny] == 0 and (nx, ny) not in visit:
                    visit[(nx, ny)] = True
                    if len(visit) == empty:
                        global min_time
                        min_time = min(min_time, time)
                    q.append((nx, ny))
                if (nx, ny) in non_activated and (nx, ny) not in virus_visit:
                    virus_visit[(nx, ny)] = True
                    q.append((nx, ny))

        time += 1


min_time = sys.maxsize
for case in cases:
    non_activated = set(virus) - set(case)
    bfs(case)
if min_time == sys.maxsize:
    min_time = -1
print(min_time)
