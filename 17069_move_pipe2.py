"""
17069 파이프 옮기기

파이프를 옮길 수 있는 방법을 모두 구하여라.

알고리즘: DFS
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
house = [list(map(int, read().strip().split())) for _ in range(n)]

pipe = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
pipe[0][1][0] = 1
for i, x in enumerate(pipe[0][2:]):
    if house[0][i+2]:
        break
    pipe[0][i+2][0] = pipe[0][i+1][0]

for i in range(1, n):
    for j in range(1, n):
        if house[i][j]:
            continue
        pipe[i][j][0] = pipe[i][j-1][0]+pipe[i][j-1][1]
        pipe[i][j][2] = pipe[i-1][j][1]+pipe[i-1][j][2]
        if house[i-1][j] or house[i][j-1]:
            continue
        pipe[i][j][1] = sum(pipe[i-1][j-1])

print(sum(pipe[n-1][n-1]))
