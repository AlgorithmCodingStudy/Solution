"""
4013 특이한 자석

자석이 4개 있는데 돌릴때 좌우에 있는 자석과 극이 다르면 반대방향으로 회전한다.

알고리즘: 시뮬레이션

1. left 함수
    1. idx가 0이면 끝
    2. 아니면
        1. 왼쪽꺼 극이 반대면
            left
2. right 함수
    1. idx가 3이면 끝
    2. 아니면
        1. 오른쪽꺼 극이 반대면
            right
"""
from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def rotate():
    def left(idx, d):
        if idx == 0:
            return
        else:
            if magnetics[idx][6] ^ magnetics[idx-1][2]:
                rotate_target.append((idx-1, -d))
                left(idx-1, -d)

    def right(idx, d):
        if idx == 3:
            return
        else:
            if magnetics[idx][2] ^ magnetics[idx+1][6]:
                rotate_target.append((idx+1, -d))
                right(idx+1, -d)

    global number
    number -= 1
    rotate_target = [(number, direction)]
    left(number, direction)
    right(number, direction)
    for n, dr in rotate_target:
        magnetics[n].rotate(dr)


def get_score():
    return magnetics[0][0] + (magnetics[1][0] << 1) + (magnetics[2][0] << 2) + (magnetics[3][0] << 3)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    magnetics = [deque(list(map(int, input().split()))) for _ in range(4)]
    for _ in range(k):
        number, direction = map(int, input().split())

        rotate()

    score = get_score()

    print("#{} {}".format(test_case, score))
