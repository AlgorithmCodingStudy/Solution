#-*- coding:utf-8 -*-

"""
2583 영역 구하기

MxN 크기의 영역에
K개의 직사각형을 그리고 남은
영역들의 넓이를 출력

알고리즘 : DFS

1. MxN 배열 1으로 초기화
2. K개의 직사각형 부분을 모두 0으로 대입
3. DFS 시작
4. DFS로 지나가는 path의 길이를 저장
"""


def dfs(start, matrix):
    # 영역의 넓이
    count = 0
    # start로 시작하는 stack
    stack = [start]

    # stack에 아무 것도 없을 때까지
    while stack:
        node = stack.pop()

        # 방문하지 않은 곳은 1
        if matrix[node[0]][node[1]] == 1:
            # 방문하면 0을 대입
            matrix[node[0]][node[1]] = 0
            # check_next로 상하좌우가 matrix의 out of range 확인
            stack.extend(check_next(node[0], node[1], len(matrix), len(matrix[0])))
            # 다음 노드를 방문할 때마다 +1
            count += 1

    return count


def check_next(x, y, width, height):
    next_list = []
    if x-1 >= 0:  # 좌
        next_list.append((x-1, y))
    if y-1 >= 0:  # 하
        next_list.append((x, y-1))
    if x+1 <= width-1:  # 우
        next_list.append((x+1, y))
    if y+1 <= height-1:  # 상
        next_list.append((x, y+1))
    return next_list


if __name__ == '__main__':
    m, n, k = map(int, input().split())
    rectangles = [list(map(int, input().split())) for _ in range(k)]

    # NxM인 mat을 1로 초기화
    mat = [[1 for _ in range(m)] for _ in range(n)]

    # 사각형을 하나씩 가져오며
    for x1, y1, x2, y2 in rectangles:
        for i in range(x2-x1):  # width
            for j in range(y2-y1):  # height
                # 사각형은 방문할 수 없으므로 0
                mat[x1+i][y1+j] = 0

    result = []
    for i, row in enumerate(mat):  # width
        for j, v in enumerate(row):  # height
            if v == 1:  # 방문하지 않았다면 1
                # dfs 시작
                result.append(dfs((i, j), mat))

    # 영역의 개수
    print(len(result))

    # sorting된 각 영역의 넓이
    print(" ".join(map(str, sorted(result))))
