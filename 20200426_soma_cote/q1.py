"""
가장 맛있는 귤 한박스

주어진 귤들중에 연속된 k개를 골라 합의 최댓값을 고르시오.

알고리즘: DP

max_result가 있고
양수면 더하기 시작
    양수면 무조건 더하기
        max 비교
    음수면 빼보다가 max result보다 작아지면 버리기
"""

import sys
read = sys.stdin.readline

n = int(read())
tmp = list(map(int, read().split()))
mandarins, before = [tmp[0]], tmp[0]
for m in tmp[1:]:
    if before*m >= 0:
        mandarins[-1] += m
    else:
        mandarins.append(m)
    before = m

max_result = 0
for i in range(len(mandarins)):
    result = 0
    for j, nxt in enumerate(mandarins[i:]):
        result += nxt
        max_result = max(max_result, result)

print(max_result)