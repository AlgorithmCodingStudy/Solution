"""
1057 토너먼트

N명이 토너먼트를 진행하는데 홀수면 맨 마지막 번호는 자동으로 다음 라운드로 진출한다.
김지민과 임한수의 번호가 주어지면 대결하는 라운드 번호를 출력하라.

알고리즘: 시뮬레이션

    1
   1 2
 1 2 3 4
12345678
1. 번호에 1을 더한 것을 2로 나눈 몫이 다음 숫자다.
2. 다음 라운드로 왔으면 두 수의 차가 1이고 작은 수가 홀수면 끝
3. 라운드 번호 출력
"""

import sys
read = sys.stdin.readline

n, a, b = map(int, read().strip().split())

n_round = 1
while not(abs(a-b) == 1 and min(a, b) % 2 == 1):
    a, b = (a+1)//2, (b+1)//2
    n_round += 1

print(n_round)
