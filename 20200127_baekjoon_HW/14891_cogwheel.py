"""
14891 톱니바퀴

톱니바퀴를 회전하는데 양옆에 톱니바퀴의 극이 반대면 반대로 움직이고 같으면 안움직인다.

알고리즘: 시뮬레이션

1. 주어지는 톱니바퀴를 회전하는데 왼쪽 2와 오른쪽 6을 체크한다.
    1. 같으면 그냥 두기
    2. 다르면 회전한 방향의 반대로 움직이기
        1. 다시 그 양옆 확인하기
"""
from collections import deque
import sys
read = sys.stdin.readline

wheels = []
wheels = [deque(map(int, list(read().strip()))) for _ in range(4)]
k = int(read().strip())


def check_left(pos, direct, first):
    if pos == 0:
        wheels[pos].rotate(direct)
        return
    else:
        if wheels[pos][6] != wheels[pos-1][2]:
            check_left(pos-1, -direct, False)
        if not first:
            wheels[pos].rotate(direct)


def check_right(pos, direct, first):
    if pos == 3:
        wheels[pos].rotate(direct)
        return
    else:
        if wheels[pos][2] != wheels[pos+1][6]:
            check_right(pos+1, -direct, False)
        if not first:
            wheels[pos].rotate(direct)


def get_score():
    score = 0
    if wheels[0][0]:
        score += 1
    if wheels[1][0]:
        score += 2
    if wheels[2][0]:
        score += 4
    if wheels[3][0]:
        score += 8
    return score


for _ in range(k):
    num, direction = map(int, read().strip().split())
    num -= 1
    if num > 0:
        check_left(num, direction, True)
    if num < 3:
        check_right(num, direction, True)
    wheels[num].rotate(direction)

print(get_score())
