"""
15686 치킨 배달

도시에 M개의 치킨집만 남기고 나머지는 모두 폐업할 계획이다.
치킨거리는 M개의 치킨집중 가장 가까운 맨해튼거리고
도시의 치킨거리는 치킨거리들의 합이다.
도시의 치킨거리의 최솟값을 구하라.

알고리즘: 브루트 포스, 구현

1. 모든 치킨집중 M개 고르는 combinations을 구한다.
2. 경우를 하나씩 가져오며
    1. 각 집의 치킨거리를 모두 구한다.
    2. 도시의 치킨거리를 구한다.
    3. 최솟값 비교를 한다.
3. 출력한다.
"""
from itertools import combinations
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
city, houses, chickens = [], [], []
for i in range(n):
    city.append(list(map(int, read().split())))
    for j, v in enumerate(city[i]):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))

def get_city_chicken_distance():
    def get_distance(x1, y1, x2, y2):
        return abs(x2-x1) + abs(y2-y1)

    ccd = 0
    for x_house, y_house in houses:
        chicken_distance = sys.maxsize
        for x_chicken, y_chicken in remain_chickens:
            chicken_distance = min(chicken_distance, get_distance(x_house, y_house, x_chicken, y_chicken))
        ccd += chicken_distance
    return ccd

min_ccd = sys.maxsize
for remain_chickens in combinations(chickens, m):
    min_ccd = min(min_ccd, get_city_chicken_distance())
print(min_ccd)
