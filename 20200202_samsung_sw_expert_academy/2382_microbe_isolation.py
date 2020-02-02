"""
2382 미생물 격리

1. 미생물을 약품이 처리된 곳 이외에 곳에 존재
2. 1시간에 한번 이동
3. 약품으로 이동하면 절반 죽고, 이동방향 반대로
4. 이동후 미생물들이 만나면 합쳐진다. 값은 더하고 방향은 더 큰놈 쪽으로
M시간 격리 후 남아있는 미생물의 합을 출력

알고리즘: 시뮬레이션

1. 입력 받
2. M번 반복
    1. 전부 이동
    2. 현위치가 약품인지 전부 확인
        1. 약품이면 n//2, 방향 반대
    3. 현위치가 겹치는 미생물들이 있는지 확인
        1. 겹친 생물들을 모아 대소비교
        2. 전부 더하고 방향은 가장 큰 놈의 방향으로
3. 합을 출력
"""


import sys
sys.stdin = open("input.txt", "r")

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move():
    for i, (x, y, n_microbe, direction) in enumerate(microbes):
        microbes[i][0], microbes[i][1] = x+dxy[direction-1][0], y+dxy[direction-1][1]


def check_range():
    for i, (x, y, n_microbe, direction) in enumerate(microbes):
        if 0 < x < n-1 and 0 < y < n-1:
            continue
        microbes[i][2] //= 2
        if direction % 2 == 1:
            microbes[i][3] += 1
        else:
            microbes[i][3] -= 1


def merge():
    nxt_microbes = []
    area = [[[] for _ in range(n)] for _ in range(n)]
    for x, y, n_microbe, direction in microbes:
        area[x][y].append([n_microbe, direction])
    for i in range(n):
        for j in range(n):
            if len(area[i][j]) > 1:
                max_microbe, idx = 0, -1
                sum_microbe = 0
                for q, (n_micro, _) in enumerate(area[i][j]):
                    sum_microbe += n_micro
                    if n_micro > max_microbe:
                        max_microbe = n_micro
                        idx = q

                nxt_microbes.append([i, j, sum_microbe, area[i][j][idx][1]])

            elif len(area[i][j]) == 1:
                nxt_microbes.append([i, j, area[i][j][0][0], area[i][j][0][1]])

    return nxt_microbes


T = int(input())
for test_case in range(1, T + 1):
    # 1. 입력받기
    n, m, k = map(int, input().split())

    microbes = []
    for _ in range(k):
        microbes.append(list(map(int, input().split())))

    # 2. M번 반복
    for _ in range(m):
        # 1. 전부 이동
        move()
        # 2. 약품 체크
        check_range()
        # 3. 겹치는 미생물
        microbes = merge()

    sum_microbes = 0
    for _, _, n_mic, _ in microbes:
        sum_microbes += n_mic
    print("#{} {}".format(test_case, sum_microbes))