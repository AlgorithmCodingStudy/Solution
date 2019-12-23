#-*- coding:utf-8 -*-

"""
포도주 잔이 여러개 있고 잔을 마셔서 최대로 마실 계획이다.
연속으로 3잔은 못마신다.
ex) 6 10 13 9 8 1 -> 6 10 9 8 -> 33

알고리즘: 다이나믹 프로그래밍

1. 재귀로 풀어볼까?
    1. 만약 depth == n이면 sum 저장
    2. 만약 drink == 3이면 안마시고 다음 함수 콜
    3. 마실 경우 안마실 경우 둘다 콜
"""
import sys
read = sys.stdin.readline

n = int(read().strip())

# wines[1~n]
wines = [0] + [int(read().strip()) for _ in range(n)]

# f[1~n]
f = [0 for _ in range(n+1)]
f[0] = wines[0]
f[1] = wines[0]+wines[1]

if n > 1:
    f[2] = max(wines[0] + wines[1], wines[1] + wines[2], wines[0] + wines[2])
    for i in range(3, n+1):
        f[i] = max(f[i - 1], f[i - 2] + wines[i], f[i - 3] + wines[i] + wines[i - 1])
print(f[n])


######################################################################################

max_wine = 0


def get_drinks(depth, sum_wine, drink, no_drink):
    global max_wine
    if depth == n-1:
        if sum_wine > max_wine:
            max_wine = sum_wine
        return
    if drink == 2:
        get_drinks(depth+1, sum_wine, drink=0, no_drink=no_drink+1)
    elif no_drink == 1:
        get_drinks(depth+1, sum_wine+wines[depth], 1, no_drink=0)
    else:
        get_drinks(depth+1, sum_wine+wines[depth], drink+1, no_drink=0)
        get_drinks(depth+1, sum_wine, drink=0, no_drink=no_drink+1)


# get_drinks(0, 0, 0, 0)
