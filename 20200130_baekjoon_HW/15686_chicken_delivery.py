"""
15686 치킨 배달

최대 M개의 치킨집을 골라서 도시치킨거리를 모두 구하고 최소비교하자.

알고리즘: 조합

1. 전체 치킨집과 집 파악
2. for 1-M
    1. 치킨집 고르기
    2. 모든 집 치킨거리
        1. 집에 대해 고른 치킨집과의 거리 계산 (치킨거리)
        2. 도시치킨거리에 더하기
    3. 최소비교
3. 최소 도시 치킨거리 출력
"""
from itertools import combinations
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
city, chicken, house = [], [], []
for a in range(n):
    city.append(list(map(int, read().strip().split())))
    for b in range(n):
        if city[a][b] == 1:
            house.append((a, b))
        elif city[a][b] == 2:
            chicken.append((a, b))


def get_chicken_distance():
    def get_distance(x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    city_chicken_distance = 0
    for hx, hy in house:
        chicken_distance = 100000
        for cx, cy in case:
            chicken_distance = min(get_distance(hx, hy, cx, cy), chicken_distance)
        city_chicken_distance += chicken_distance

    return city_chicken_distance


min_city_chicken_distance = 100000
for r in range(1, m+1):
    cases = combinations(chicken, r)
    for case in cases:
        min_city_chicken_distance = min(min_city_chicken_distance, get_chicken_distance())

print(min_city_chicken_distance)
