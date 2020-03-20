"""
2167 2차원 배열의 합

i, j에서 x, y까지의 합을 구하라.

알고리즘 : DP

이게 왜 DP지
그냥 풀어보자.

는 시간초과

sum(i-x, j-y) = sum(0-x, 0-y) - sum(0-i, 0-y) - sum(0-x, 0-j) + sum(0-i, 0-j)
"""
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(n)]
for j in range(1, m):
    arr[0][j] += arr[0][j-1]
for i in range(1, n):
    arr[i][0] += arr[i-1][0]
    for j in range(1, m):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
k = int(read())

for _ in range(k):
    i, j, x, y = map(lambda f: int(f)-1, read().split())
    if i == 0 and j != 0:
        result = arr[x][y] - arr[x][j-1]
    elif i != 0 and j == 0:
        result = arr[x][y] - arr[i-1][y]
    elif i == 0 and j == 0:
        result = arr[x][y]
    else:
        result = arr[x][y] - arr[x][j-1] - arr[i-1][y] + arr[i-1][j-1]
    print(result)
