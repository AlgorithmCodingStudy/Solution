"""
16919 봄버맨 2

1. 봄버맨이 일부 칸에 폭탄설치
2. 1초 쉬고
3. 1초동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치
4. 1초가 지난 후 3초전에 설치된 폭탄 모두 폭발

알고리즘: 시뮬레이션


"""

import sys
read = sys.stdin.readline

r, c, n = map(int, read().split())
state = [list(read().strip()) for _ in range(r)]
if not n%2:
    for _ in range(r):
        print('O'*c)
else:
    if n%4 == 1:
        for line in state:
            print("".join(line))
    else:
        remove = set()
        for i in range(r):
            for j in range(c):
                if state[i][j] == 'O':
                    remove.add((i, j))
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = i+dx, j+dy
                        if not (0 <= nx < r and 0 <= ny < c):
                            continue
                        remove.add((nx, ny))
        result = [['O']*c for _ in range(r)]
        for i, j in remove:
            result[i][j] = '.'

        for line in result:
            print("".join(line))
