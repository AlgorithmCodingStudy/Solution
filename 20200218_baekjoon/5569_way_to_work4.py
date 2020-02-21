"""
5569 출근 경로

(1, 1)에서 (w, h)로 가는데 북쪽과 동쪽으로만 이동가능하다.
한번 꺾고나면 1블럭 초과 꼭 가야한다.
갈 수 있는 출근 경로를 100000으로 나눈 나머지를 출력하라.

알고리즘: 시뮬레이션, 브루트 포스, DFS

1. 동쪽, 북쪽으로 이동
2. 꺽으면 인자로 turn=false
3. turn이 false면 무조건 직진
4. turn이 true면 두가지 가능

2 3
1 3 1
1 2 2
2 2 1
3 2

"""

import sys
read = sys.stdin.readline

w, h = map(int, read().strip().split())

dp = [[[[0, 0], [0, 0]] for _ in range(101)] for _ in range(101)]

for i in range(2, h+1):
    dp[i][1][0][0] = 1

for i in range(2, w+1):
    dp[1][i][0][1] = 1

for i in range(2, h+1):
    for j in range(2, w+1):
        dp[i][j][0][0] = (dp[i-1][j][0][0] + dp[i-1][j][1][0]) % 100000
        dp[i][j][0][1] = (dp[i][j-1][0][1] + dp[i][j-1][1][1]) % 100000
        dp[i][j][1][0] = (dp[i-1][j][0][1]) % 100000
        dp[i][j][1][1] = (dp[i][j-1][0][0]) % 100000

result = (dp[h][w][0][0] + dp[h][w][0][1] + dp[h][w][1][0] + dp[h][w][1][1]) % 100000
print(result)
