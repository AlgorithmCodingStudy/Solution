"""
5373 큐빙

큐브를 주어진 방법대로 돌리고 나서 결과를 출력하면 된다.

알고리즘: 시뮬레이션

1. 입력받기
2. 돌리기 돌리기 돌리기

[위, 아래, 앞, 뒤, 왼, 오]
"""

import sys
input = sys.stdin.readline


def cubing(s, d):
    def turn(direct, t):
        cube[t][0][0], cube[t][0][2], cube[t][2][2], cube[t][2][0] \
            = swap(not direct, cube[t][0][0], cube[t][0][2], cube[t][2][2], cube[t][2][0])
        cube[t][0][1], cube[t][1][2], cube[t][2][1], cube[t][1][0] \
            = swap(not direct, cube[t][0][1], cube[t][1][2], cube[t][2][1], cube[t][1][0])

    def swap(direct, s1, s2, s3, s4):
        if direct:
            s1, s2, s3, s4 = s2, s3, s4, s1
        else:
            s1, s2, s3, s4 = s4, s1, s2, s3
        return s1, s2, s3, s4

    def up():
        turn(d, 0)
        for i in range(3):
            cube[3][0][i], cube[4][0][i], cube[2][0][i], cube[5][0][i] \
                = swap(d, cube[3][0][i], cube[4][0][i], cube[2][0][i], cube[5][0][i])

    def down():
        turn(d, 1)
        for i in range(3):
            cube[2][2][i], cube[4][2][i], cube[3][2][i], cube[5][2][i] \
                = swap(d, cube[2][2][i], cube[4][2][i], cube[3][2][i], cube[5][2][i])

    def front():
        turn(d, 2)
        for i in range(3):
            cube[0][2][i], cube[4][-(i+1)][2], cube[1][0][-(i+1)], cube[5][i][0] \
                = swap(d, cube[0][2][i], cube[4][-(i+1)][2], cube[1][0][-(i+1)], cube[5][i][0])

    def back():
        turn(d, 3)
        for i in range(3):
            cube[0][0][i], cube[5][i][2], cube[1][2][-(i+1)], cube[4][-(i+1)][0] \
                = swap(d, cube[0][0][i], cube[5][i][2], cube[1][2][-(i+1)], cube[4][-(i+1)][0])

    def left():
        turn(d, 4)
        for i in range(3):
            cube[0][i][0], cube[3][-(i+1)][2], cube[1][i][0], cube[2][i][0] \
                = swap(d, cube[0][i][0], cube[3][-(i+1)][2], cube[1][i][0], cube[2][i][0])

    def right():
        turn(d, 5)
        for i in range(3):
            cube[0][i][2], cube[2][i][2], cube[1][i][2], cube[3][-(i+1)][0] \
                 = swap(d, cube[0][i][2], cube[2][i][2], cube[1][i][2], cube[3][-(i+1)][0])

    if s == 'U':
        up()
    elif s == 'D':
        down()
    elif s == 'F':
        front()
    elif s == 'B':
        back()
    elif s == 'L':
        left()
    else:
        right()


T = int(input())
for _ in range(T):
    n = int(input())
    operations = list(map(list, input().strip().split()))
    cube = [[list('www'), list('www'), list('www')],
            [list('yyy'), list('yyy'), list('yyy')],
            [list('rrr'), list('rrr'), list('rrr')],
            [list('ooo'), list('ooo'), list('ooo')],
            [list('ggg'), list('ggg'), list('ggg')],
            [list('bbb'), list('bbb'), list('bbb')]]

    for side, direction in operations:
        direction = True if direction == '+' else False
        cubing(side, direction)
    print("{}\n{}\n{}".format("".join(cube[0][0]), "".join(cube[0][1]), "".join(cube[0][2])))
