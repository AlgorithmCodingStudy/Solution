"""
4014 활주로 건설

땅에 길이 X 높이 1인 경사로를 설치할 수 있다.
경사로를 설치해서 활주로의 높이가 1차이 난다면 활주로 건설이 가능하다.
가로세로 N+N개의 경우를 검사해서 건설가능한 활주로의 개수를 출력하라.

알고리즘: 시뮬레이션

1. N+N개의 줄을 하나씩 가져와서
    1. before을 초기화
    2. i+1부터 before과 같은지 보고
        1. 다르면
            1. 차이가 1 초과면 다음 줄
            2. 차이가 1 이하면
                1. 한칸 낮거나 높은 상태로 x개를 검사
                    1. 되면 설치하고 before을 한칸 낮거나 높게 업데이트
                    2. 안되면 다음 줄
        2. 된 줄에 대해서는 cnt+=1
"""

import sys
sys.stdin = open("input2.txt", "r")


def check_line():
    # 같은 숫자끼리 묶기
    divide_line = [[line[0]]]
    before = line[0]
    for v in line[1:]:
        if before == v:
            divide_line[-1].append(v)
        else:
            divide_line.append([v])
        before = v
    # [[3, 3, 3], [2], [1, 1]]
    # [[3, 3], [2], [3, 3, 3]]

    before = divide_line[0]
    for i, divide in enumerate(divide_line[1:]):
        if 0 < divide[0] - before[-1] <= 1.5:  # 상승 [2, 2, 2] [3, 3]와 같은 상황
            if len(before) < x:  # 이전 블럭의 길이가 경사로 길이보다 작으면 설치 불가
                return
            for j in range(x):  # 이전 블럭을 뒤에서 앞으로 검토
                if divide_line[i][len(before)-x+j] % 1 != 0:  # 1로 나누어서 나머지가 있다는건 이미 경사로가 설치된 것이므로 설치 불가
                    return
                divide_line[i][len(before)-x+j] += 0.5  # 설치 가능하면 0.5씩 더해서 경사로를 설치했다고 표시
            before = divide  # 이전 블럭을 현재 블럭으로 업데이트
        elif -1.5 <= divide[0] - before[-1] < 0:  # 하강 [3, 3], [2, 2, 2]와 같은 상황
            if len(divide) < x:  # 현재 블럭의 길이가 경사로 길이보다 작으면 설치 불가
                return
            for j in range(x):  # 현재 블럭을 앞에서 부터 경사로 길이 만큼
                divide_line[i+1][j] += 0.5  # 경사로 설치
            before = divide  # 이전 블럭을 현재 블럭으로 업데이트
        else:  # 차이가 2이상 나면 설치 불가
            return

    global cnt
    cnt += 1  # 모든 검토가 끝났으면 활주로 건설이 가능하므로 +1
    return


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, x = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0

    for line in ground:  # 가로 모두 검토
        check_line()

    ground = [list(line) for line in zip(*ground)]  # transpose를 통해 세로를 가로로

    for line in ground:  # 세로 모두 검토
        check_line()

    print("#{} {}".format(test_case, cnt))
    # ///////////////////////////////////////////////////////////////////////////////////

