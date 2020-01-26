"""
14499 주사위 굴리기

주사위 굴린후
    바닥이 0이면 주사위의 아랫면이 바닥으로 복사
    0이 아니면 바닥을 주사위 아랫면으로 복사후 칸이 0이 된다.
    처음에는 모두 0이 쓰여있다.

n, m : h, w
x, y : 처음 시작점
k : 명령 개수
동서북남 : 1234

알고리즘: 시뮬레이션

1. 한칸이동
    1. 바닥이 0인지 아닌지 체크
        1. 0이면 주사위 아랫면 바닥으로 복사
        2. 0이 아니면 바닥을 주사위 아랫면으로 복사, 바닥 0으로 초기화

  2
4 1 3
  5
  6

"""

import sys
read = sys.stdin.readline

n, m, x, y, k = map(int, read().strip().split())
area = [list(map(int, read().strip().split())) for _ in range(n)]
command = list(map(int, read().strip().split()))

dice = [0 for _ in range(6)]


def move():
    def check_range(nx, ny):
        return 0 <= nx < n and 0 <= ny < m

    global x, y
    if c == 1:
        if not check_range(x, y+1):
            return dice, False
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        x, y = x, y+1
    elif c == 2:
        if not check_range(x, y-1):
            return dice, False
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        x, y = x, y-1
    elif c == 3:
        if not check_range(x-1, y):
            return dice, False
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        x, y = x-1, y
    else:
        if not check_range(x+1, y):
            return dice, False
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        x, y = x+1, y
    return new_dice, True


def update():
    if area[x][y] == 0:
        area[x][y] = dice[5]
    else:
        dice[5] = area[x][y]
        area[x][y] = 0


for c in command:
    dice, move_flag = move()
    if move_flag:
        update()
        print(dice[0])
