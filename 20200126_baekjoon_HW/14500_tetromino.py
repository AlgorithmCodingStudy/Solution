"""
14500 테트로미노

테트로미노 5가지를 NxM에 배치하여 합이 가장 큰 경우를 구하자.
회전이나 대칭 가능

알고리즘: 시뮬레이션

1. (0, 0)부터 (i, j)까지 서치
    1. 테트로미 5가지
        1. 4x1, 1x4
        2. 2x2
        3. ㄱ, ㄱ회전, ㄱ대칭, ㄴ, ㄴ회전
        4. 꾸불, 꾸불회전, 꾸불대칭, 꾸불대칭회전
        5. ㅗ, ㅗ회전, ㅜ, ㅜ회전

"""

import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
area = [list(map(int, read().strip().split())) for _ in range(n)]


def check_tetromino(x, y):
    def check_range(nx, ny):
        return 0 <= nx < n and 0 <= ny < m

    def block1():
        # 4x1
        # @@@@
        if check_range(x, y+3):
            sum_block = sum(area[x][y:y+4])
            blocks.append(sum_block)
        # 1x4
        # @
        # @
        # @
        # @
        if check_range(x+3, y):
            sum_block = area[x][y] + area[x+1][y] + area[x+2][y] + area[x+3][y]
            blocks.append(sum_block)

    def block2():
        # 2x2
        # @@
        # @@
        if check_range(x+1, y+1):
            sum_block = area[x][y] + area[x][y+1] + area[x+1][y] + area[x+1][y+1]
            blocks.append(sum_block)

    def block3():
        # ㄱ
        # %@@
        #   @
        if check_range(x+1, y+2):
            sum_block = sum(area[x][y:y+3], area[x+1][y+2])
            blocks.append(sum_block)
        # ㄱ 270
        #  %
        #  @
        # @@
        if check_range(x+2, y-1):
            sum_block = area[x][y] + area[x+1][y] + area[x+2][y] + area[x+2][y-1]
            blocks.append(sum_block)
        # ㄱ 90
        # @@
        # @
        # %
        if check_range(x-2, y+1):
            sum_block = area[x][y] + area[x-1][y] + area[x-2][y] + area[x-2][y+1]
            blocks.append(sum_block)
        # ㄱ 180
        # @
        # @@%
        if check_range(x-1, y-2):
            sum_block = sum(area[x][y-2:y+1], area[x-1][y-2])
            blocks.append(sum_block)

        # %@@
        # @
        if check_range(x+1, y) and check_range(x, y+2):
            sum_block = sum(area[x][y:y+3], area[x+1][y])
            blocks.append(sum_block)
        # @
        # @
        # %@
        if check_range(x-2, y) and check_range(x, y+1):
            sum_block = area[x][y] + area[x-1][y] + area[x-2][y] + area[x][y+1]
            blocks.append(sum_block)
        #   @
        # @@%
        if check_range(x, y-2) and check_range(x-1, y):
            sum_block = sum(area[x][y-2:y+1], area[x-1][y])
            blocks.append(sum_block)
        # @%
        #  @
        #  @
        if check_range(x, y-1) and check_range(x+2, y):
            sum_block = area[x][y] + area[x][y-1] + area[x+1][y] + area[x+2][y]
            blocks.append(sum_block)

    def block4():
        # original
        # %
        # @@
        #  @
        if check_range(x+2, y+1):
            sum_block = area[x][y] + area[x+1][y] + area[x+1][y+1] + area[x+2][y+1]
            blocks.append(sum_block)
        # original 270
        #  @@
        # %@
        if check_range(x-1, y+2):
            sum_block = area[x][y] + area[x][y+1] + area[x-1][y+1] + area[x-1][y+2]
            blocks.append(sum_block)
        # 대칭
        #  %
        # @@
        # @
        if check_range(x+2, y-1):
            sum_block = area[x][y] + area[x+1][y] + area[x+1][y-1] + area[x+2][y-1]
            blocks.append(sum_block)
        # 대칭 90
        # %@
        #  @@
        if check_range(x+1, y+2):
            sum_block = area[x][y] + area[x][y+1] + area[x+1][y+1] + area[x+1][y+2]
            blocks.append(sum_block)

    def block5():
        # ㅗ
        if check_range(x-1, y+1) and check_range(x, y+2):
            sum_block = area[x][y] + area[x][y+1] + area[x-1][y+1] + area[x][y+2]
            blocks.append(sum_block)
        # ㅏ
        if check_range(x+2, y) and check_range(x+1, y+1):
            sum_block = area[x][y] + area[x+1][y] + area[x+1][y+1] + area[x+2][y]
            blocks.append(sum_block)
        # ㅜ
        if check_range(x, y+2) and check_range(x+1, y+1):
            sum_block = area[x][y] + area[x][y+1] + area[x+1][y+1] + area[x][y+2]
            blocks.append(sum_block)
        # ㅓ
        if check_range(x+1, y-1) and check_range(x+2, y):
            sum_block = area[x][y] + area[x+1][y] + area[x+1][y-1] + area[x+2][y]
            blocks.append(sum_block)

    blocks = []
    block1()
    block2()
    block3()
    block4()
    block5()
    if blocks:
        return max(blocks)
    else:
        return 0


max_result = 0
for i in range(n):
    for j in range(m):
        result = check_tetromino(i, j)
        if result > max_result:
            max_result = result
print(max_result)
