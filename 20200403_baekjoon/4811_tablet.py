"""
4811 알약

N개의 약을 먹는데 반씩 먹는다.
꺼낸 알이 새거면 W
반개짜리면 H
2N 동안

재귀로 풀어보자.

"""
import sys
read = sys.stdin.readline

memo = [[0]*(30+1) for _ in range(30+1)]

def dfs(w, h):
    if w == 0: return 1
    if not memo[w][h]:
        memo[w][h] = dfs(w-1, h+1)
        if h: memo[w][h] += dfs(w, h-1)
    return memo[w][h]

n = int(read())
while n:
    print(dfs(n, 0))
    n = int(read())
