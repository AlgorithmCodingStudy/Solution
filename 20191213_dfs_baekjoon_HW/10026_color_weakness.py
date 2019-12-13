#-*- coding:utf-8 -*-

"""
10026 적록색약

NxN 그리드에 RGB로 그린 그림
몇 개의 구역은 같은 색으로 이루어짐
상하좌우 인접한 색은 같은 구역
일반인이 보는 구역의 개수와 적록색약이 보는 구역의 개수를 출력

알고리즘: DFS

1. 적록색약이 보는 그림을 얻기
2. dfs로 그림을 RGB 하나씩 모두 살펴보는데 방문한 곳은 X로 치환
3. 구역 수 얻기
"""


def dfs(start, picture):
    stack = [start]
    # 단순히 True False가 아닌 RGB이기 때문에 처음 시작하는 color를 저장
    color = picture[start[0]][start[1]]

    while stack:
        node = stack.pop()

        # 만약 처음 color와 현재 node의 색이 같다면
        if picture[node[0]][node[1]] == color:
            # 방문했으니깐 X로 치환
            picture[node[0]][node[1]] = 'X'
            # check_next로 다음 가능한 상하좌우를 stack에 추가
            stack.extend(check_next(node[0], node[1], len(picture), len(picture[0])))

    # dfs가 끝난다는 것은 경로 하나가 나온 것이므로 1을 리턴
    return 1


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
    n = int(input())
    pic = [list(input()) for _ in range(n)]

    # 적록색약이 보는 그림
    pic_weak = [[] for _ in range(n)]
    for i, row in enumerate(pic):
        for j, v in enumerate(list(row)):
            # 값이 G면
            if v == "G":
                # G가 아니라 R로 저장
                pic_weak[i].append("R")
            else:
                # R, B는 그대로 저장
                pic_weak[i].append(v)

    # 구역 개수 초기화
    normal, weak = 0, 0
    for i, row in enumerate(pic):
        for j, v in enumerate(row):
            # 정상인의 그림의 값이 X가 아니면, 즉 방문하지 않았으면
            if v != "X":
                # 현 위치에서 dfs 시작 및 return된 1 추가
                normal += dfs((i, j), pic)

            # 적록색약의 그림의 값이 X가 아니면, 즉 방문하지 않았으면
            if pic_weak[i][j] != "X":
                # dfs 시작
                weak += dfs((i, j), pic_weak)

    print("{} {}".format(normal, weak))