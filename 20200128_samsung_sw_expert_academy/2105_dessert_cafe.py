"""
2105 디저트카페

디저트카페 투어를 할건데 길이 대각선이다.
갔던 길을 되돌아가면 안되고
같은 디저트를 먹으면 안된다.
출발한 지점으로 다시 돌아와야한다.
디저트 투어가 가능한 경우 가장 많은 디저트를 먹는 경우 디저트 수를 출력하라.

알고리즘: DFS or BFS

1. 모든 지점을 출발지점으로 탐색한다.
    1. start 지점의 길이 1개 밖에 없으면 리턴
    2. 아니면
        1. 현 위치가 출발지점이면 디저트 개수 계산 및 최대 비교
        2. 다음에 갈 곳을 정하자. 4가지 길중에
            1. 안가본 곳
            2. 먹지 않은 디저트


"""
import sys
sys.stdin = open("input.txt", "r")
dxy = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def dfs(sx, sy):
    def check_range(_x, _y):
        return 0 <= _x < n and 0 <= _y < n

    stack = [(sx, sy, [], 0)]
    while stack:
        x, y, desserts, direction = stack.pop()
        if (x, y) == (sx, sy) and len(desserts) > 2:
            length = len(desserts)
            global max_length
            if length > max_length:
                max_length = length

        if direction == 4:
            continue

        dx, dy = dxy[direction]
        direction += 1
        nxt_desserts = []
        while check_range(x+dx, y+dy) and area[x+dx][y+dy] not in desserts+nxt_desserts:
            x, y = x+dx, y+dy
            nxt_desserts.append(area[x][y])
            stack.append((x, y, desserts+nxt_desserts, direction))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    max_length = -1

    for i in range(n):
        for j in range(n):
            if (i, j) in [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]:
                continue
            dfs(i, j)

    print("#{} {}".format(test_case, max_length))
    # ///////////////////////////////////////////////////////////////////////////////////

