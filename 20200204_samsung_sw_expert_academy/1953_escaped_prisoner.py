"""
1953 탈주범 검거

L시간동안 탈주범이 위치할 수 있는 곳의 개수를 출력

알고리즘: DFS

1. 입력받고
2. 지하터널을 배치
3. DFS의 length를 L만큼 제한해서 시작
4. DFS가 방문할 수 있는 모든 곳을 체크하고 카운트한다.
"""

import sys
sys.stdin = open("input.txt", "r")


def dfs():
    def check_range(_x, _y):
        return 0 <= _x < n and 0 <= _y < m

    block_type = [[],
                  [(0, (-1, 0)), (1, (1, 0)), (2, (0, -1)), (3, (0, 1))],
                  [(0, (-1, 0)), (1, (1, 0))],
                  [(2, (0, -1)), (3, (0, 1))],
                  [(0, (-1, 0)), (3, (0, 1))],
                  [(1, (1, 0)), (3, (0, 1))],
                  [(1, (1, 0)), (2, (0, -1))],
                  [(0, (-1, 0)), (2, (0, -1))]]
    nxt_block_type = [[1, 2, 5, 6],
                      [1, 2, 4, 7],
                      [1, 3, 4, 5],
                      [1, 3, 6, 7]]

    stack = [(r, c, [(r, c)])]
    visit[(r, c)] = True

    while stack:
        x, y, path = stack.pop()
        if len(path) == l:
            continue

        for direction, (dx, dy) in block_type[underground[x][y]]:
            nx, ny = x+dx, y+dy
            if not check_range(nx, ny):
                continue
            if underground[nx][ny] in nxt_block_type[direction] and (nx, ny) not in path:
                stack.append((nx, ny, path+[(nx, ny)]))
                visit[(nx, ny)] = True


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, r, c, l = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(n)]

    visit = {}
    dfs()
    print("#{} {}".format(test_case, len(visit)))
    # ///////////////////////////////////////////////////////////////////////////////////

