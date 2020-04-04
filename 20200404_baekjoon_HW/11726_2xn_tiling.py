"""
11726 2xn 타일링

2x1의 타일로 2xn의 타일을 채우는 방법의 가지수는?
1 1
2 2
3 3
4 5
5 8
6 13
7 21
8 34
9 55
f[n] = f[n-1]+f[n-2]

알고리즘: DP
"""

import sys
read = sys.stdin.readline

dp = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
n = int(read())
if len(dp) <= n:
    for i in range(len(dp), n+1):
        dp.append((dp[i-1]+dp[i-2])%10007)
print(dp[n])
