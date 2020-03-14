from collections import deque
from copy import deepcopy

n, k = map(int, input().split())
arr = list(map(int, input().split()))


def bfs():
    q = deque([[1]*n])
    depth = 1

    while q:
        qsize = len(q)
        for _ in range(qsize):
            now_arr = q.popleft()
            idx = arr.index(depth)
            start = idx-k if idx-k >= 0 else 0
            stop = idx if idx+k <= n else n-k+1
            for i in range(start, stop):

