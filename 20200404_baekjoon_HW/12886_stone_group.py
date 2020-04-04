"""
12886 돌 그룹

ABC 돌 그룹을 모두 같게 하고 싶다.
두 그룹을 선택한 후 작은 그룹이 X 큰 그룹을 Y로 지정
X = X*2, Y = Y-X
계속 반복해서 같은 개수가 될 수 있을까?

알고리즘: 탐색

기록을 하자.
visit = 3차원 1000 * 1000 * 1000
"""
from copy import deepcopy
from itertools import permutations
import sys
read = sys.stdin.readline

abc = list(map(int, read().split()))
idxs = [(0, 1), (1, 2), (0, 2)]


def dfs():
    global abc
    visit = {(na, nb, nc):True for na, nb, nc in permutations(abc, 3)}
    stack = [tuple(abc)]
    while stack:
        abc = stack.pop()
        if len(set(abc)) == 1:
            return 1
        for i, j in idxs:
            if abc[i] == abc[j]: continue
            small, big = (abc[i], abc[j]) if abc[i] < abc[j] else (abc[j], abc[i])
            nabc = list(deepcopy(abc))
            nabc[i], nabc[j] = small*2, big-small
            if tuple(nabc) not in visit:
                for nnabc in permutations(nabc, 3):
                    visit[nnabc] = True
                stack.append(tuple(nabc))

    return 0

print(dfs())
