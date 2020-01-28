"""
12100 2048 (easy)

상하좌우 움직여서 블럭을 합치는 2048 게임이다.
5번 움직여서 가장 큰 블럭을 출력

알고리즘: DFS or BFS

1. 재귀로 풀어보자.
    1. 상
        1. 중력작용
        2. 합치기
    2. 하
        1. 중력작용
        2. 합치기
    3. 좌
        1. 중력작용
        2. 합치기
    4. 우
        1. 중력작용
        2. 합치기
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
blocks = [list(map(int, read().strip().split())) for _ in range(n)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def step(direction):
    def gravity():
        if direction == 0:
            for i in range(n):
                before = blocks[i][n-1]
                for j in range(n-1, -1, -1):
                    if

    for nxt in range(4):
