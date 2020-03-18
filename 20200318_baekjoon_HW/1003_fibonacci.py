"""
1003 피보나치 함수

fibonacci
0   1 0
1   0 1
2   1 1
3   1 2
4   2 3

위와 같이 이전 결과를 더해간다.

근데 매번 호출해서 더하면 같은 동작이 반복되므로 메모이제이션을 사용하자.

알고리즘: DP
"""

import sys
read = sys.stdin.readline

memo = {0: [1, 0], 1:[0, 1]}

t = int(read().strip())
for _ in range(t):
    n = int(read().strip())
    if n not in memo:
        last = max(memo.keys())
        for i in range(last+1, n+1):
            a0, a1 = memo[i-2]
            b0, b1 = memo[i-1]
            memo[i] = [a0+b0, a1+b1]
    print("{} {}".format(*memo[n]))
