from itertools import combinations
import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))
idxs = list(range(1, n))

cases = list(combinations(idxs, k-1))
min_cost = sys.maxsize
for case in cases:
    case = [0] + list(case) + [n]
    cost = 0
    for i in range(k):
        start, stop = case[i], case[i+1]
        cost += arr[stop-1] - arr[start]
    min_cost = min(cost, min_cost)

print(min_cost)

