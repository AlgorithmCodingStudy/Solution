#-*- coding:utf-8 -*-

"""
수영장

계획에 따라 가장 적은 금액을 사용하는 경우를 출력. 금액을 출력
ex)
1일 이용권 10원
1달 이용권 40원 매달 1일부터 시작
3달 이용권 100원 매달 1일부터 시작 11월 12월에도 사용가능
1년 이용권 300원

입력
테스트케이스 t
이용금액 10 40 100 300
사용 계획 0 1 23 4 2 ... 0

1. day * 10 > 40이면 day는 4일 이상. 그러니깐 한달에 4일 이상일경우 한달이용권이 이득
2. day1 * 10 or 40 + day2 * 10 or 40 + day3 * 10 or 40 > 100이면 3달이용권이 이득
3. 위 조건에 의해 결정된 1년 가격과 1년 이용권 가격과 비교해서 작은것이 최소금액?
"""

import sys
read = sys.stdin.readline

t = int(read().strip())
case = []
for _ in range(t):
    price = list(map(int, read().strip().split()))
    plan = [0] + list(map(int, read().strip().split()))
    case.append((price, plan))


def dfs(month, fee):
    global min_fee
    if month > 12:
        if fee < min_fee:
            min_fee = fee
    else:
        dfs(month+1, fee + price[0]*plan[month])
        dfs(month+1, fee + price[1])
        dfs(month+3, fee + price[2])
        dfs(month+12, fee + price[3])


for i, (price, plan) in enumerate(case):
    min_fee = 10000000
    dfs(0, 0)
    print("#{} {}".format(i+1, min_fee))
