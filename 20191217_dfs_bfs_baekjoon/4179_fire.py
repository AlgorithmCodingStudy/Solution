#-*- coding:utf-8 -*-

"""
4179 불!

미로에서 탈출을 해야하는데 불이 번진다.
불은 사방으로 한칸씩 번진다.
#은 벽, .는 지나갈 수 있는 공간, J는 출발지점, F는 불의 출발지점

불에 따라잡히면 IMPOSSIBLE
탈출하면 가장 짧은 시간

알고리즘: DFS or BFS

최단시간이면 BFS 아닌가?

1. 불을 확장시킨다.
2. 지훈이가 움직일 수 있는 곳을 파악하고 이동한다.
3. 반복하며 가장자리에 도달한다면 그때 path의 length를 출력한다.
"""
import sys
from queue import Queue
from copy import deepcopy
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def update_miro(miro):

    fire_update = set()
    for i, row in enumerate(miro):
        for j, v in enumerate(row):
            if v == 'F':
                for x, y in zip(dx, dy):
                    if miro[i+x][j+y] == 'F':
                        fire_update.add((i+x, j+y))
    for i, j in fire_update:
        miro[i][j] = 'F'


def bfs(node, miro, depth):
    if node[0] == 0 or node[0] == len(miro)-1 or node[1] == 0 or node[1] == len(miro[0])-1:
        print(depth+1)
        return 1
    update_miro(miro)
    for x, y in zip(dx, dy):
        if miro[node[0]+x][node[1]+y] == '.':
            if bfs((node[0]+x, node[1]+y), deepcopy(miro), depth+1) == 1: return 1
    return 0


if __name__ == '__main__':
    r, c = map(int, sys.stdin.readline().split())
    m = [list(sys.stdin.readline())[:-1] for _ in range(r)]
    for i, row in enumerate(m):
        for j, v in enumerate(row):
            if v == 'J':
                if bfs((i, j), m, 0) == 0:
                    print("IMPOSSIBLE")
