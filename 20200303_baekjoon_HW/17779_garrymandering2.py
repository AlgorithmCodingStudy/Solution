"""
17779 게리맨더링2

구역을 다섯 구역으로 나눈다.
나눈 후 인구가 가장 큰 곳과 작은 곳의 차이의 최솟값을 구하라.

알고리즘: 시뮬레이션, 브루트 포스

1 <= x < n-2
    1 <= y < n-1

"""
from itertools import chain
import sys
read = sys.stdin.readline

n = int(read().strip())
area = [list(map(int, read().strip().split())) for _ in range(n)]


def set_area():
    def get_population():
        r = [0]*5

        for i in range(0, x+d1):
            for j in range(0, y+1):
                r[0] += area[i][j]
        t = 0
        for i in range(x, x+d1):
            for j in range(y-t, y+1):
                r[0] -= area[i][j]
            t += 1

        for i in range(0, x+d2+1):
            for j in range(y+1, n):
                r[1] += area[i][j]
        t = 1
        for i in range(x+1, x+d2+1):
            for j in range(y+1, y+1+t):
                r[1] -= area[i][j]
            t += 1

        for i in range(x+d1, n):
            for j in range(0, y-d1+d2):
                r[2] += area[i][j]
        t = 0
        for i in range(x+d1, x+d1+d2+1):
            for j in range(y-d1+t, y-d1+d2):
                r[2] -= area[i][j]
            t += 1

        for i in range(x+d2+1, n):
            for j in range(y-d1+d2, n):
                r[3] += area[i][j]
        t = 0
        for i in range(x+d2+1, x+d1+d2+1):
            for j in range(y-d1+d2, y+d2-t):
                r[3] -= area[i][j]
            t += 1

        r[4] = sum(chain(*area)) - sum(r)

        return r

    global min_population
    for d1 in range(1, y+1):
        for d2 in range(1, n-y):
            try:
                regions = get_population()
                diff = max(regions) - min(regions)
                min_population = min(min_population, diff)
            except:
                continue


min_population = sys.maxsize
for x in range(0, n-2):
    for y in range(1, n-1):
        set_area()
print(min_population)
