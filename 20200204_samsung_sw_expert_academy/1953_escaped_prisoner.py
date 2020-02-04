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

    block_type = [[],  # 검토해야하는 방향들
                  [(0, (-1, 0)), (1, (1, 0)), (2, (0, -1)), (3, (0, 1))],  # 1번 상하좌우
                  [(0, (-1, 0)), (1, (1, 0))],  # 2번 상하
                  [(2, (0, -1)), (3, (0, 1))],  # 3번 좌우
                  [(0, (-1, 0)), (3, (0, 1))],  # 4번 상우
                  [(1, (1, 0)), (3, (0, 1))],  # 5번 하우
                  [(1, (1, 0)), (2, (0, -1))],  # 6번 하좌
                  [(0, (-1, 0)), (2, (0, -1))]]  # 7번 상좌
    # 다음에 올 수 있는 블럭들
    nxt_block_type = [[1, 2, 5, 6],  # 아래부분이 뚫려있는
                      [1, 2, 4, 7],  # 윗부분이 뚫려있는
                      [1, 3, 4, 5],  # 오른쪽이 뚫려있는
                      [1, 3, 6, 7]]  # 왼쪽이 뚫려있는

    stack = [(r, c, [(r, c)])]  # 현위치와 path
    visit[(r, c)] = True

    while stack:
        x, y, path = stack.pop()
        if len(path) == l:  # path의 길이가 l이면 시간초과
            continue

        for direction, (dx, dy) in block_type[underground[x][y]]:  # 현재 블럭타입으로부터 검토해야할
            nx, ny = x+dx, y+dy
            if not check_range(nx, ny):
                continue
            if underground[nx][ny] in nxt_block_type[direction] and (nx, ny) not in path:  # 다음 블럭이 다음에 올 수 있는 블럭들에 있고 현재 path에 방문하지 않았다면
                stack.append((nx, ny, path+[(nx, ny)]))
                visit[(nx, ny)] = True


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, r, c, l = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(n)]

    visit = {}  # 방문한 곳에서는 모두 존재할 수 있는 위치
    dfs()
    print("#{} {}".format(test_case, len(visit)))
    # ///////////////////////////////////////////////////////////////////////////////////
