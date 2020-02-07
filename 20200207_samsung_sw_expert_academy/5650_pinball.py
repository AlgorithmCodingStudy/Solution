"""
5650 핀볼게임

-1 블랙홀
0 빈공간
1-5 블럭
6-10 웜홀

블랙홀 빠지거나 시작 지점으로 돌아오면 끝
부딪히는 블럭이랑 벽만큼 점수
출발지점과 방향을 임의로 정할 때 최고 점수는?

알고리즘: 시뮬레이션, 브루트 포스

1. 가로 세로 모두 검토하면서
    1. 빈공간이면
        1. 네 방향으로 핀볼시작
            1. 다음지점이 0이면 계속 전진
            2. 1-5면 방향전환
            3. 6-10면 대칭 웜홀로 위치 이동
            4. -1이나 시작지점이면
                score 비교 및 업데이트
2. 출력
"""

import sys
sys.stdin = open("input2.txt", "r")


def game_start(sx, sy, sd):
    def forward():
        return x+dx, y+dy

    def backward():
        d_ = d + 2 if d < 2 else d - 2
        return x-dx, y-dy, d_, score+1

    def turn_left():
        d_ = d + 1 if d < 3 else 0
        x_, y_ = x+dxy[d_][0], y+dxy[d_][1]
        return x_, y_, d_, score+1

    def turn_right():
        d_ = d - 1 if d > 0 else 3
        x_, y_ = x+dxy[d_][0], y+dxy[d_][1]
        return x_, y_, d_, score+1

    def block0():
        return forward()

    def block1():
        if d == 0:
            return backward()
        elif d == 1:
            return backward()
        elif d == 2:
            return turn_right()
        else:
            return turn_left()

    def block2():
        if d == 0:
            return backward()
        elif d == 1:
            return turn_right()
        elif d == 2:
            return turn_left()
        else:
            return backward()

    def block3():
        if d == 0:
            return turn_right()
        elif d == 1:
            return turn_left()
        elif d == 2:
            return backward()
        else:
            return backward()

    def block4():
        if d == 0:
            return turn_left()
        elif d == 1:
            return backward()
        elif d == 2:
            return backward()
        else:
            return turn_right()

    def block5():
        return backward()

    def block678910(hole):
        for hx, hy in holes[hole]:
            if (x, y) != (hx, hy):
                return hx+dx, hy+dy

    dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    score = 0
    x, y = sx, sy
    d = sd
    while True:
        dx, dy = dxy[d][0], dxy[d][1]
        block = game_map[x][y]
        if block == 0:
            x, y = block0()

        elif block == 1:
            x, y, d, score = block1()

        elif block == 2:
            x, y, d, score = block2()

        elif block == 3:
            x, y, d, score = block3()

        elif block == 4:
            x, y, d, score = block4()

        elif block == 5:
            x, y, d, score = block5()

        elif 6 <= block:  # 웜홀이면
            x, y = block678910(block - 6)  # 다른 웜홀로 이동

        dx, dy = dxy[d][0], dxy[d][1]
        if not(0 <= x < n and 0 <= y < n):  # 범위 밖이면
            x, y, d, score = backward()  # 뒤로 오기

        block = game_map[x][y]
        if (x, y) == (sx, sy) or block == -1:  # 처음으로 돌아오거나 블랙홀이면
            global max_score
            max_score = max(score, max_score)  # 비교 및 업데이트
            return  # 종료


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    game_map = [list(map(int, input().split())) for _ in range(n)]
    holes = [list() for _ in range(5) ]
    for i in range(n):
        for j in range(n):
            if game_map[i][j] > 5:
                holes[game_map[i][j] - 6].append((i, j))

    max_score = 0

    for i in range(n):
        for j in range(n):
            if game_map[i][j] == 0:
                for d_ in range(4):
                    game_start(i, j, d_)

    print("#{} {}".format(test_case, max_score))
