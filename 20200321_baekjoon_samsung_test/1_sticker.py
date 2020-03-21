"""
1 스티커 붙이기

1. 주어진 스티커를 차례대로 붙인다.
    1. 최대한 위 최대한 왼쪽에 붙인다.
    2. 붙일 수 없다면 시계방향으로 90도 회전한다.
    3. 그래도 못 붙인다면 버린다.
2. 다 붙인 후 스티커가 붙어있는 칸의 수를 출력

알고리즘 : 시뮬레이션

123
456
789

741
852
963

12345
67890

61
72
83
94
05
"""

import sys
read = sys.stdin.readline

n, m, k = map(int, read().split())
notebook = [[0]*m for _ in range(n)]
result = 0


def attach(x, y):
    for a in range(r):
        for b in range(c):
            nx, ny = x+a, y+b
            if sticker[a][b] and notebook[nx][ny]:
                return 0

    n_sticker = 0
    for a in range(r):
        for b in range(c):
            nx, ny = x+a, y+b
            notebook[nx][ny] = sticker[a][b]
            n_sticker += sticker[a][b]
    return n_sticker


def rotate():
    new_sticker = [[0]*r for _ in range(c)]
    for a in range(r):
        for b in range(c):
            new_sticker[b][-(a+1)] = sticker[a][b]
    return new_sticker


for _ in range(k):
    r, c = map(int, read().split())
    sticker = [list(map(int, read().split())) for _ in range(r)]

    success = False
    for d in range(4):
        for i in range(n-r+1):
            for j in range(m-c+1):
                if success:
                    break
                num = attach(i, j)
                if num and not success:
                    success = True
                    result += num
                    break

        if success:
            break
        sticker = rotate()
        r, c = c, r

print(result)