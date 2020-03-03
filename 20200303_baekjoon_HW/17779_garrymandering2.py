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
        r = [0]*5
        for i in range(n):
            for j in range(n):
                if i < x:
                    bound1, bound2 = y, y
                    if j <= bound1:
                        r[0] += area[i][j]
                    else:
                        r[1] += area[i][j]

                elif x <= i < x+d1:
                    if
                    bound1, bound2 = bound1-1, bound2+1
                    if j <= bound1:
                        r[0] += area[i][j]
                    elif bound1 < j < bound2:
                        r[4] += area[i][j]
                    else:
                        r[1] += area[i][j]

                elif x+d1 <= i <= x+d1+d2:
                    bound1, bound2 =
                else:
                    pass
        r1 = 0
        for i in range(x+d1):
            if i < x:
                length = y+1
            else:
                length = y-(i-x)
            for j in range(length):
                r1 += area[i][j]

        r2 = 0
        for i in range(x+d2+1):
            if i <= x:
                length = n-y-1
                for j in range(length):
                    r2 += area[i][y+1+j]
            else:
                length = y-(i-x)+1
                for j in range(length):
                    r2 += area[i][y+1+(i-x)+j]

        return r1

    global min_population
    d1, d2 = 1, 1
    regions = get_population()
    for d1 in range(1, y+1):
        for d2 in range(1, n-y):
            regions = get_population()
            # diff = max(regions) - min(regions)
            # min_population = min(min_population, diff)


min_population = sys.maxsize
x, y = 2, 2
set_area()
for x in range(0, n-2):
    for y in range(1, n-1):
        set_area()
