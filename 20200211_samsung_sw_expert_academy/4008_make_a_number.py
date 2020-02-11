"""
4008 숫자 만들기

N개의 숫자가 나열되고 그 사이사이에 연산자 +-*/를 넣어 값을 계산한다.
그중 최소와 최대의 차이를 구해 출력한다.

알고리즘: 시뮬레이션, 재귀, DFS

1. 숫자들과 연산자의 종류를 입력받는다.
2. 경우에 따라
    1. +가 남아있으면 +를 쓰고 재귀호출
    2. -가 남아있으면 -를 쓰고 재귀호출
    3. *가 남아있으면 *를 쓰고 재귀호출
    4. /가 남아있으면 /를 쓰고 재귀호출
    5. 다썼으면 최대 최소 비교
"""

import sys
sys.stdin = open("input.txt", "r")


def calculate(result, idx, add, sub, mul, div):
    if not (add or sub or mul or div):
        global max_result, min_result
        max_result = max(result, max_result)
        min_result = min(result, min_result)
        return
    else:
        global numbers
        if add:
            calculate(result+numbers[idx], idx+1, add-1, sub, mul, div)
        if sub:
            calculate(result-numbers[idx], idx+1, add, sub-1, mul, div)
        if mul:
            calculate(result*numbers[idx], idx+1, add, sub, mul-1, div)
        if div:
            calculate(int(result/numbers[idx]), idx+1, add, sub, mul, div-1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    operations = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_result = -100000000
    min_result = 100000000

    calculate(numbers[0], 1, *operations)

    print("#{} {}".format(test_case, max_result-min_result))
