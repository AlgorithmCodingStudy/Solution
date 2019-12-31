#-*- coding:utf-8 -*-

"""
17471 게리맨더링

구역을 두개 설정했을때 인구수가 최소가 되는 경우

1. 123456을 두 구역으로 나눈 후 dfs로 같은 구역인지 테스트를 해볼까?
"""
from collections import deque
from itertools import combinations
from math import inf

import sys
read = sys.stdin.readline

n = int(read().strip())
district = list(range(1, n+1))
population = list(map(int, read().strip().split()))
graph = {}
for i in district:
    graph[i] = list(map(int, read().strip().split()))[1:]


def check_area(area):
    q = deque()
    q.append(list(area)[0])
    visit = {}

    while q:
        node = q.pop()
        if node not in visit:
            visit[node] = True
            if set(visit.keys()) == area:
                return True
            nxt = set(graph[node]) - (set(district) - area)
            q.extend(nxt)

    return False


def sum_population(area):
    result = 0
    for a in area:
        result += population[a-1]
    return result


min_area = inf
for i in range(1, n//2+1):
    for j in set(combinations(district, i)):
        area1 = set(j)
        area2 = set(district) - area1
        if check_area(area1) and check_area(area2):
            population1, population2 = sum_population(area1), sum_population(area2)
            diff = abs(population1 - population2)
            if diff < min_area:
                min_area = diff

if min_area == inf:
    print(-1)
else:
    print(min_area)
