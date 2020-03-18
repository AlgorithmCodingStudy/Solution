"""
1932 정수 삼각형

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
과 같이 정수 삼각형이 존재할때
하나씩 정수를 더해가며 내려올때 가장 큰 값은? 현 위치로부처 좌하우하만 선택가능

알고리즘: DP

1. 5x5 DP 배열
2. n = 0, 1을 원래 수로 초기화
3. dp[n, m] = max(dp[n-1, m-1], dp[n-1, m]) + dp[n, m]
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
dp = []
for i in range(n):
    dp.append(list(map(int, read().strip().split())))

for i in range(1, n):
    for j, v in enumerate(dp[i]):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif 0 < j < len(dp[i])-1:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
        else:
            dp[i][j] += dp[i-1][j-1]

print(max(dp[n-1]))
