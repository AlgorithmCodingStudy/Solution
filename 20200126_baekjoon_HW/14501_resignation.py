"""
14501 퇴사

각 날짜마다 상담스케줄이 있고
걸리는 날짜와 돈이 있다.
적절히 상담했을때 가장 많은 돈을 받는 경우의 수익을 구하라.

알고리즘: DFS

1. DFS를 하자.
    1. 1-N까지
    2. 상담 마친날부터 N까지
    3. 끝나면 수익 비교
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
t, p = [], []
for _ in range(n):
    a, b = map(int, read().strip().split())
    t.append(a)
    p.append(b)

max_benefit = 0


def dfs(day, benefit):
    global max_benefit
    for i in range(day, n):
        next_day = day+t[i] + (i-day)
        next_benefit = benefit + p[i]
        if next_day > n:
            if benefit > max_benefit:
                max_benefit = benefit
        elif next_day == n:
            if next_benefit > max_benefit:
                max_benefit = next_benefit
        else:
            dfs(next_day, next_benefit)


dfs(0, 0)
print(max_benefit)
