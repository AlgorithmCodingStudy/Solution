"""
17779 게리맨더링2

구역을 다섯 구역으로 나눈다.
나눈 후 인구가 가장 큰 곳과 작은 곳의 차이의 최솟값을 구하라.

알고리즘: 시뮬레이션, 브루트 포스

1 <= x < n-2
    1 <= y < n-1

"""

import sys
read = sys.stdin.readline

n = int(read().strip())
area = [list(map(int, read().strip().split())) for _ in range(n)]


def set_area():
    def get_population():
        for i in range(x+d1-1):
            if i < x:
                length = y+1
            else:
                length = y-(i)
            for j in range(length):
        return region
    global min_population
    for d1 in range(1, y):
        for d2 in range(1, n-y):
            regions = get_population()
            diff = max(regions) - min(regions)
            min_population = min(min_population, diff)


min_population = sys.maxsize
for x in range(0, n-2):
    for y in range(1, n-1):
