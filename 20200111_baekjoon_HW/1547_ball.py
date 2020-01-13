"""
1547 공

3개의 컵중 1번자리에 공을 넣고 섞을 것이다.
섞을 때는 컵을 들고 섞어서 공의 위치가 안변한다.
즉 M번 섞은 후 1번째 자리에 와있는 컵의 번호를 알아내면 된다.

알고리즘: 시뮬레이션

1. 123이 들어있는 리스트를 만든다.
2. 순서에 따라 두 숫자를 스왑한다.
3. 0번째 값을 출력한다.
"""

import sys
read = sys.stdin.readline

cups = list(range(1, 4))

t = int(read().strip())

for _ in range(t):
    t1, t2 = map(int, read().strip().split())
    cups[t1-1], cups[t2-1] = cups[t2-1], cups[t1-1]

print(cups.index(1)+1)
