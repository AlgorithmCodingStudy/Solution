"""
2579 계단 오르기

계단을 오를때 한칸 혹은 두칸 오를수 있고 연속해서 3칸 오르면 안된다.
최대로 얻을 수 있는 점수는?

알고리즘: DP

점화식 : dp[n] = max(dp[n-1], dp[n-2]+stair[n], dp[n-3]+stair[n]+stair[n-1])
"""

# import sys
# read = sys.stdin.readline
#
# n = int(read())
# dp = [0]*n
# stair = [int(read()) for _ in range(n)]
#
# dp[0] = stair[0]
# if n == 1:
#     print(dp[-1])
#     sys.exit(0)
# dp[1] = stair[0]+stair[1]
# if n == 2:
#     print(dp[-1])
#     sys.exit(0)
# dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])
# for i in range(3, n):
#     dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i]+stair[i-1])
# print(dp[-1])

from sys import stdin

a,b,c = 0,0,0

n = int(stdin.readline())

for _ in range(n):
    pb = int(stdin.readline())
    a,b,c = max(b,c),a+pb,b+pb

print(max(b, c))