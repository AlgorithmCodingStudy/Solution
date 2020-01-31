import sys
from itertools import combinations
sys.stdin = open("input2.txt", "r")


def get_taste(g):
    taste = 0
    for i in g:
        for j in g:
            taste += adj[i][j]
    return taste


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    adj = [list(map(int, input().split())) for _ in range(n)]

    min_diff = 100000
    cases = combinations(range(n), n//2)
    for case in cases:
        g1 = list(case)
        g2 = list(set(range(n)) - set(case))
        diff = abs(get_taste(g1) - get_taste(g2))
        min_diff = min(diff, min_diff)

    print("#{} {}".format(test_case, min_diff))