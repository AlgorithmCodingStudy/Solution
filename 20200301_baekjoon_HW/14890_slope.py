"""
14890 경사로

높이가 1차이 나고 경사로 x의 길이만큼 공간이 있으면 경사로를 세울 수 있다.
가로세로 2n개에서 경사로를 설치하여 지나갈 수 있는 길의 수를 구하라.

알고리즘: 시뮬레이션

1. 가로 6개에 대해
    1. 같은 숫자끼리 divide한다.
    2. 이전꺼 기준으로 다음꺼가 높으면 before < after
        1. 이전꺼에 경사로가 설치되어 있지 않고 before % 1 == 0
        2. 길이가 경사로보다 길면 len(before) > l
        3. 설치가능
    3. 이전꺼 기준으로 다음꺼가 낮으면
        1. 다음꺼 길이가 경사로보다 길면
        2. 설치가능

2. 세로 6개에 대해
    1. 반복
"""

import sys
read = sys.stdin.readline

n, l = map(int, read().strip().split())
area = [list(map(int, read().strip().split())) for _ in range(n)]


def check_line(line):
    divide_line = [[line[0]]]
    for i in range(1, len(line)):
        if divide_line[-1][0] == line[i]:
            divide_line[-1].append(line[i])
        else:
            divide_line.append([line[i]])

    for i in range(1, len(divide_line)):
        if 0 < divide_line[i][0] - divide_line[i-1][-1] <= 1:
            if len(divide_line[i-1]) < l:
                return 0
            for j in range(l):
                if divide_line[i-1][-1-j] % 1 != 0:
                    return 0

        elif 0 < divide_line[i-1][0] - divide_line[i][0] <= 1.5:
            if len(divide_line[i]) < l:
                return 0
            else:
                for j in range(l):
                    divide_line[i][j] += 0.5
        else:
            return 0
    return 1


area_t = list(map(list, zip(*area)))
area = area + area_t

cnt = 0
for row in area:
    cnt += check_line(row)
print(cnt)
