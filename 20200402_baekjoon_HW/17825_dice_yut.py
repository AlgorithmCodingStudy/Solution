"""
17825 주사위 윷놀이

주사위를 굴려서 진행을 하는데 윷놀이처럼 회전하는 지점이 존재한다.
말은 4개로 만약 진행할 지점에 말이 잇으면 진행하지 못한다.
앞으로 주어질 주사위 10개를 안다면 얻을 수 있는 최댓값을 출력하라.

알고리즘: 구현, 완전 탐색

1. 경로 4개에 대해 모두 초기화 해둔다.
2. 모든 경우의 수를 전부 검토해야한다.
    1. 말 4개중에 진행 말을 정할 수 있으므로 경우는 4개씩 추가된다.
    2. 만약 꺾이는 지점에 도착한다면 경로를 변경한다.
    3. 계속 점수를 더한다.
    4. 10개를 모두 사용했으면 최댓값과 비교
3. 최댓값 출력

재귀로 짜보자.
"""

import sys

movements = list(map(int, sys.stdin.readline().split()))
path_info = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
    [10, 13, 16, 19, 25],
    [20, 22, 24, 25],
    [30, 28, 27, 26, 25],
    [25, 30, 35, 40, 0]
]
piece_positions = [[0, 0], [0, 0], [0, 0], [0, 0]]
piece_scores = [0, 0, 0, 0]
answer = 0


def dfs(idx):
    if idx == 10:
        global answer
        answer = max(answer, sum(piece_scores))
        return answer

    move = movements[idx]

    for i in range(4):
        cur_path = piece_positions[i][0]
        cur_block = piece_positions[i][1]

        if cur_block == len(path_info[cur_path]) - 1:
            continue

        next_path = cur_path
        next_block = cur_block + move
        if cur_path == 0:
            if next_block == 5:
                next_path = 1
                next_block = 0
            elif next_block == 10:
                next_path = 2
                next_block = 0
            elif next_block == 15:
                next_path = 3
                next_block = 0
            elif next_block == 20:
                next_path = 4
                next_block = 3
        elif cur_path < 4:
            if next_block >= len(path_info[cur_path]) - 1:
                next_path = 4
                next_block -= len(path_info[cur_path]) - 1

        if next_block >= len(path_info[next_path]):
            next_block = len(path_info[next_path]) - 1

        if path_info[next_path][next_block] != 0:
            if [next_path, next_block] in piece_positions:
                continue

        piece_positions[i][0] = next_path
        piece_positions[i][1] = next_block
        piece_scores[i] += path_info[next_path][next_block]

        dfs(idx + 1)

        piece_positions[i][0] = cur_path
        piece_positions[i][1] = cur_block
        piece_scores[i] -= path_info[next_path][next_block]


dfs(0)
print(answer)
