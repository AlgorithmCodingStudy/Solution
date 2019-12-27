#-*- coding:utf-8 -*-

"""
Sorting Game

ex)
3412 -> 4312 -> 4321 -> 1234 // 3번
3412 -> 3214 -> 1234 // 2번

최소 연산 횟수를 출력

알고리즘: BFS

1. 입력 길이가 4일때 정렬할 수 있는 경우의 수는 4 33 222로 6개 이경우에 대해 계속 BFS 진행
2. 단 이전에 했던 정렬을 다시할 이유가 없음
3. 이전에 했던 정렬을 방문처리해 반복 방지
"""
from collections import deque
import sys
read = sys.stdin.readline

t = int(read().strip())
case = []
for _ in range(t):
    n = int(read().strip())
    nums = list(map(int, read().strip().split()))
    case.append((n, nums))

q = deque()


def bfs():
    global n, nums
    q = deque()


for n, nums in case:
    bfs()