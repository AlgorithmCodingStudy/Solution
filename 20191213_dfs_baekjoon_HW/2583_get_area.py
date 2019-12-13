#-*- coding:utf-8 -*-

"""
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
    count = 0
    stack = [start]

    while stack:
        node = stack.pop()

        if matrix[node[0]][node[1]] == 1:
            matrix[node[0]][node[1]] = 0
            stack.extend(check_next(node[0], node[1], len(matrix), len(matrix[0])))
            count += 1

    return count


def check_next(x, y, width, height):
    next_list = []
    if x-1 >= 0:
        next_list.append((x-1, y))
    if y-1 >= 0:
        next_list.append((x, y-1))
    if x+1 <= width-1:
        next_list.append((x+1, y))
    if y+1 <= height-1:
        next_list.append((x, y+1))
    return next_list


if __name__ == '__main__':
    m, n, k = map(int, input().split())
    rectangles = [list(map(int, input().split())) for _ in range(k)]

    mat = [[1 for _ in range(m)] for _ in range(n)]

    for x1, y1, x2, y2 in rectangles:
        for i in range(x2-x1):
            for j in range(y2-y1):
                mat[x1+i][y1+j] = 0
    result = []
    for i, row in enumerate(mat):
        for j, v in enumerate(row):
            if v == 1:
                result.append(dfs((i, j), mat))

    print(len(result))
    print(" ".join(map(str, sorted(result))))
