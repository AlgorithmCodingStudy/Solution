"""
5014 스타트링크

F층인 건물에서 S층에서 G층으로 가기 위한 최소 횟수를 출력
U만큼 위로 D만큼 아래로 갈 수 있다.
1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000

알고리즘: dp

1. frog 함수를 만들어보자.

"""
from collections import deque
import sys
read = sys.stdin.readline

f, s, g, u, d = map(int, read().strip().split())

if (u == 0 and g > s) or (d == 0 and g < s):
    print("use the stairs")
    sys.exit(0)

visit = {s: 0}


def frog(goal):
    if goal in visit:
        return visit[goal]
    if goal + d <= 1000000:
        if goal - u >= 1:
            m = min(frog(goal + d), frog(goal - u))
        else:
            m = frog(goal + d)
    else:
        if goal - u >= 1:
            m = frog(goal - u)
    visit[goal] = m
    return m


print(frog(g))
