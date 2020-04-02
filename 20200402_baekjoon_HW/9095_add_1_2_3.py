"""
9095 1, 2, 3 더하기

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
dp[5] = 13
dp[6] = 24
dp[7] = 44
...
dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
"""

import sys
read = sys.stdin.readline

dp = [0, 1, 2, 4, 7, 13, 24, 44]

for _ in range(int(read())):
    n = int(read())
    if len(dp) <= n:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n])