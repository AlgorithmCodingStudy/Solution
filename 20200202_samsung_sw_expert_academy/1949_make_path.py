"""
1949 등산로 조성

등산로를 낮은 지역부터 정상까지 만들것이다.
등산로는 무조건 오름차순이며 같은 고도가 존재하지 않는다.
공사를 통해 K보다 작은 수 만큼 한번 고도를 깎을 수 있다.
가장 긴 등산로의 길이를 출력하라.

알고리즘: DFS, 완전 탐색

1. 산의 max 값과 그 위치를 찾는다. (봉우리)
2. NxNxk 만큼 다 깎으면서 찾아본다.
3. 봉우리에서 DFS를 시작한다.
    1. 상하좌우를 탐색해서 낮은 지역으로만 간다.
    2. 더이상 갈곳이 없다면 path 길이 비교
4. max 출력
"""

import sys
sys.stdin = open("input2.txt", "r")
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(sx, sy):
    stack = [(sx, sy, 1)]

    while stack:
        x, y, length = stack.pop()

        for dx, dy in dxy:
            nxt = []
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] < area[x][y]:
                    nxt.append((nx, ny, length+1))
            if nxt:
                stack.extend(nxt)
            else:
                global max_length
                max_length = max(length, max_length)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    top_height = 0
    for line in area:
        top_height = max(top_height, *line)
    top_pos = []
    for i in range(n):
        for j in range(n):
            if area[i][j] == top_height:
                top_pos.append((i, j))

    max_length = 0
    for i in range(n):
        for j in range(n):
            for deep in range(1, k+1):
                area[i][j] -= 1
                if area[i][j] < 0:
                    continue
                for ni, nj in top_pos:
                    if (i, j) != (ni, nj):
                        dfs(ni, nj)
            area[i][j] += k

    print("#{} {}".format(test_case, max_length))

