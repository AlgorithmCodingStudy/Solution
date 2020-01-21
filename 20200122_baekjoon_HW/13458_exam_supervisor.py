"""
13458 시험 감독

N개의 시험장
응시자수들 A
총감독관 감시가능 B 시험장당 오직 1명만
부감독관 감시가능 C 시험장당 여러명 가능

필요한 최소 감독 수 출력

알고리즘: 시뮬레이션

1. 반 수 대로 총감독관을 한명씩 다 뿌린다.
2. 남은 학생수를 커버할 수 있을 만큼의 부감독관을 뿌린다.
"""
from math import ceil
import sys
read = sys.stdin.readline

n = int(read().strip())
a = list(map(int, read().strip().split()))
b, c = map(int, read().strip().split())

result = 0
result += n
a = list(map(lambda x: x-b if x-b >= 0 else 0, a))
for students in a:
    result += ceil(students / c)

print(result)
