"""
5532 방학 숙제

방학 L일
수학 B 페이지 풀어야 하는데 하루에 D 페이지 가능
국어 A 페이지 풀어야 하는데 하루에 C 페이지 가능

알고리즘: 시뮬레이션

1. B / D와 A / C를 구한다.
2. 둘 중 큰 걸 구한다.
3. L에서 뺀다.
"""
from math import ceil
import sys
read = sys.stdin.readline

l = int(read().strip())
a = int(read().strip())
b = int(read().strip())
c = int(read().strip())
d = int(read().strip())

math, korean = ceil(b / d), ceil(a / c)
day = max(math, korean)
vacation = l - day
print(vacation)

