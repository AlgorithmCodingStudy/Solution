"""
구슬 N번
맵 WxH

구슬로 맨위의 벽돌만 깰 수 있다. -> 0-9까지의 선택 DFS or BFS
벽돌은 숫자 1-9
상하좌우로 숫자만큼 벽돌을 부심
부술때 부숴지는 벽돌의 숫자 또한 적용돼서 연쇄작용
부수고 나서는 중력 작용

최대한 많은 벽돌을 부수고 남은 벽돌의 수를 출력

알고리즘: DFS or BFS

1. dfs
    1. 구슬 수를 세며 N번이면 끝
        1. 남은 벽돌수 체크
    2. 아직이면
        1. 현재 위치 벽돌 부수고 부수면서 다시 재귀?
        2. 다부수고 나면 중력 적용
"""
from copy import deepcopy
import sys
sys.stdin = open("input2.txt", "r")
sys.setrecursionlimit(100000)


def dfs(now_blocks, cnt):
    def break_block(breaking_blocks, idx):
        def range_check(x_, y_):
            return 0 <= x_ < w and 0 <= y_ < h
        if 0 not in breaking_blocks[idx]:
            start = h-1
        else:
            start = breaking_blocks[idx].index(0) - 1

        def break_(n_block, x, y):
            breaking_blocks[x][y] = 0
            for a in range(-(n_block-1), n_block):
                nx1, ny1, nx2, ny2 = x+a, y, x, y+a
                if range_check(nx1, ny1):
                    num = breaking_blocks[nx1][ny1]
                    if num > 1:
                        break_(num, nx1, ny1)
                    elif num == 1:
                        breaking_blocks[nx1][ny1] = 0
                if range_check(nx2, ny2):
                    num = breaking_blocks[nx2][ny2]
                    if num > 1:
                        break_(num, nx2, ny2)
                    elif num == 1:
                        breaking_blocks[nx2][ny2] = 0

        break_(breaking_blocks[idx][start], idx, start)

        return breaking_blocks

    def gravity(set_blocks):
        for line in set_blocks:
            n_iter = line.count(0)
            for _ in range(n_iter):
                line.remove(0)

        for line in set_blocks:
            line += [0]*(h - len(line))

    global min_remains
    if cnt == n:
        count_0 = 0
        for line in now_blocks:
            count_0 += line.count(0)
        count_1 = w*h - count_0
        if count_1 < min_remains:
            min_remains = count_1
    else:
        for i in range(w):
            new_blocks = break_block(deepcopy(now_blocks), i)
            gravity(new_blocks)
            dfs(new_blocks, cnt+1)
            pass


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    n, w, h = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(h)]
    blocks = [list(reversed(x)) for x in zip(*blocks)]
    min_remains = 10000000
    dfs(blocks, 0)
    print("#{} {}".format(test_case, min_remains))

    # ///////////////////////////////////////////////////////////////////////////////////

