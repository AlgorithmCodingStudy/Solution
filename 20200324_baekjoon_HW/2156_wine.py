"""
2156 포도주 시식

포도주를 연속해서 3잔 마실 수는 없다.

알고리즘: DP

dp[n] = max(dp[n-1], dp[n-2]+wine[n], dp[n-3]+wine[n]+wine[n-1])
"""

import sys
read = sys.stdin.readline

n = int(read())
dp = [0]*n
wine = [int(read()) for _ in range(n)]
dp[0] = wine[0]
if n == 1:
    print(dp[0])
    sys.exit(0)
dp[1] = wine[0]+wine[1]
if n == 2:
    print(dp[1])
    sys.exit(0)
dp[2] = max(wine[0]+wine[2], wine[0]+wine[1], wine[1]+wine[2])
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])
print(dp[-1])
