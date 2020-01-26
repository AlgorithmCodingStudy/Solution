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
import sys
read = sys.stdin.readline

n = int(read().strip())
a = list(map(int, read().strip().split()))
addition, subtraction, multiplication, division = map(int, read().strip().split())


def dfs(idx, result, add, sub, mul, div):
    if idx == n:
        global max_result, min_result
        max_result = max(result, max_result)
        min_result = min(result, min_result)
    else:
        if add:
            dfs(idx+1, result+a[idx], add-1, sub, mul, div)
        if sub:
            dfs(idx+1, result-a[idx], add, sub-1, mul, div)
        if mul:
            dfs(idx+1, result*a[idx], add, sub, mul-1, div)
        if div:
            dfs(idx+1, int(result/a[idx]), add, sub, mul, div-1)

max_result = -1000000000
min_result = 1000000000

dfs(1, a[0], addition, subtraction, multiplication, division)

print(max_result)
print(min_result)
