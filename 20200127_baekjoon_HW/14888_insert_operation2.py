"""
14888 연산자 끼워넣기

N개의 수
N-1개의 연산자
N개의 수 사이에 N-1개의 연산자를 끼워넣을 것이다.
연산자의 우선순위는 무시하고 앞에서부터 계산한다.
나눗셈은 몫을 취한다.
음수의 나눗셈은 양수로 바꾼후 몫을 구한후 음수를 취한다.

알고리즘: 시뮬레이션, 재귀, DFS, 브루트 포스

1. 재귀함수로 풀어보자.
"""
from copy import deepcopy
import sys
read = sys.stdin.readline

n = int(read().strip())
a = list(map(int, read().strip().split()))
addition, subtraction, multiplication, division = map(int, read().strip().split())
operations = ['+']*addition + ['-']*subtraction + ['*']*multiplication + ['/']*division


def permutations(arr, k):
    def generate(chosen, remain):
        if len(chosen) == k:
            global max_result, min_result
            res = operate(chosen)
            if res > max_result:
                max_result = res
            if res < min_result:
                min_result = res
        else:
            for i in remain:
                next_remain = deepcopy(remain)
                next_remain.remove(i)
                generate(chosen+[i], next_remain)
    generate([], arr)


def operate(opers):
    result = a[0]
    for oper, ai in zip(opers, a[1:]):
        if oper == '+':
            result += ai
        elif oper == '-':
            result -= ai
        elif oper == '*':
            result *= ai
        else:
            if result >= 0:
                result //= ai
            else:
                result = -result // ai
    return result


max_result = 0
min_result = 100000000

permutations(operations, n-1)

print(max_result)
print(min_result)
