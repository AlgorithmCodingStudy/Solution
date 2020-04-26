"""
채널링

(s1, e1), (s2, e2)와 같은 식으로 데이터가 주어진다.
s2 < s1 < e2면 1번은 2번을 공격할 수 있다.
공격할 수 있는 수를 구하라.

알고리즘: 시뮬레이션

1. 입력을 받아 (시간, 번호, 0은 시작 1은 종료)와 같은 식으로 list에 추가한다.
2. sorting
3. 모든 참가자에 대해
    1. s1과 e1 사이에 있는 s는 모두 각각 1씩 추가
    2. 차례로 반복
"""

import sys
read = sys.stdin.readline

n = int(read())
data, timing = [], []
for i in range(1, n+1):
    s, e = map(int, read().split())
    data.append((i, s, e))
    timing.append((s, i, 0))
    timing.append((e, i, 1))

timing.sort()
result = [0]*n
for i, s, e in data:
    si = timing.index((s, i, 0))
    ei = timing.index((e, i, 1))
    for time, j, state in timing[si+1:ei]:
        if time == s or time == e: continue
        if state == 0:
            result[j-1] += 1

print("\n".join(map(str, result)))
