#-*- coding:utf-8 -*-

"""
2293 동전 1

n가지의 가치는 지닌 동전들로 k원을 만들고 싶다.
각각의 동전은 여러번 사용할 수 있다.
사용한 동전의 구성이 같다면 같은 경우이다.
경우의 수를 출력

알고리즘: 다이나믹 프로그래밍

1. Top-down 하면서 거를건 거르고 구할건 구하는 방식으로 가야할까?
    1. 큰수부터 고르는데 큰 수를 고르고나면 다음 수에서 본인보다 큰 수를 고를 수 없다.
    --> 시간 초과

2. Bottom-up 으로 구할 수 있는 점화식이 존재할까?
            0   1   2   3   4   5   6   7   8   9   10
    1원 추가  1   1   1   1   1   1   1   1   1   1   1
    2원 추가  1   1   2   2   3   3   4   4   5   5   6
    5원 추가  1   1   2   2   3   4   5   6   7   8   10
    f2[n] = f1[n] + f2[n-2]
    f5[n] = f2[n] + f5[n-5]
"""

import sys
read = sys.stdin.readline

n, k = map(int, read().strip().split())
coins = [int(read().strip()) for _ in range(n)]

dp = [0 for i in range(10001)]
dp[0] = 1
for i in coins:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])


'''
f = [[0 for _ in range(k+1)] for _ in range(n)]
for j in range(k+1):
    if j % coins[0] == 0:
        f[0][j] = 1

for i in range(1, n):
    for j in range(k+1):
        if j < coins[i]:
            f[i][j] = f[i-1][j]
        else:
            f[i][j] = f[i-1][j] + f[i][j-coins[i]]

print(f[-1][-1])
'''

