"""
14899 스타트와 링크

같은 팀이 됐을때 더해지는 능력치가 NxN으로 주어진다.
팀을 나누었을때 팀의 능력치가 최소가 되는 경우를 출력

알고리즘: 브루트포스, 조합

1. N에서 N/2를 뽑는 조합을 구해서 팀을 나누는 경우를 모두 구한다.
2. 경우를 모두 탐색하며 최소를 구한다.
"""
from itertools import combinations
import sys
read = sys.stdin.readline

n = int(read().strip())
weight = [list(map(int, read().strip().split())) for _ in range(n)]

cases = combinations(range(n), n//2)


def calculate_weight(player):
    now_weight = 0
    for c1 in player:
        for c2 in player:
            now_weight += weight[c1][c2]
    return now_weight


min_weight = sys.maxsize
for case in cases:
    w1 = calculate_weight(case)
    w2 = calculate_weight(set(range(n)) - set(case))
    if abs(w1-w2) < min_weight:
        min_weight = abs(w1-w2)
print(min_weight)