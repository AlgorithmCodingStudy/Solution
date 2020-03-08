"""
17825 주사위 윷놀이

윷놀이처럼 파란색 지점에 도착하면 파란색 방향으로 가야한다.

알고리즘: 시뮬레이션, DFS

1.
"""
from copy import deepcopy
import sys
read = sys.stdin.readline

dices = list(map(int, read().strip().split()))
road = [list(range(0, 41, 2)),
       list(range(0, 10, 2)) + [10, 13, 16, 19, 25, 30, 35, 40],
       list(range(0, 20, 2)) + [20, 22, 24, 25, 30, 35, 40],
       list(range(0, 30, 2)) + [30, 28, 27, 26, 25, 30, 35, 40]]


def trial(time, markers, score):
    if time == 10:
        global max_score
        max_score = max(max_score, score)
    now = dices[time]
    for i, (line, marker) in enumerate(markers):
        nxt = marker + now
        if line == 0:
            if road[0][nxt] == 10:
                line = 1
            elif road[0][nxt] == 20:
                line = 2
            elif road[0][nxt] == 30:
                line = 3
        if (line, nxt) in markers or nxt > len(road[line]):
            continue
        nxt_markers = deepcopy(markers)
        nxt_markers[i] = (line, nxt)
        score += road[line][nxt]
        trial(time+1, nxt_markers, score)


max_score = 0
trial(0, [(0, 0), (0, 0), (0, 0), (0, 0)], 0)
print(max_score)