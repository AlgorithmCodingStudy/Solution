"""
2240 자두나무

좌우로 왔다갔다 최대 W번 할 수 있다.
왔다갔다하면서 먹을 수 있는 최대 자두 수를 출력

알고리즘: DP

1. 3x7
2. n=0 0, 1
3. dp[n, m] = max(dp[n-1, m], dp[n-1, m-1]) + tree[n, m]
"""
import sys
read = sys.stdin.readline

t, w = map(int, read().strip().split())
tree = [0]
for _ in range(t):
    tree.append(int(read().strip())-1)

dp = [[0]*(w+1) for _ in range(t+1)]
for i in range(1, t+1):
    dp[i][0] = dp[i - 1][0] + (tree[i]==0)
    for j in range(1, min(i+1, w+1)):
        if tree[i] == 0 and j%2==0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif tree[i] == 1 and j%2==1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))
