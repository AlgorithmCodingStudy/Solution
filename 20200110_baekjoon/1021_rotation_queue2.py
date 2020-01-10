"""
1021 회전하는 큐

연산 3가지
1. popleft
2. rotate left
3. rotate right

큐의 크기 N
뽑아내려고 하는 개수 M
위치 1 2 3

알고리즘: 시뮬레이션

1. 위치를 sorting한다.
2. 만약 q.front가
    1. 위치에 속한다면 popleft
    2. 아니면
        1. min 위치가 left와 가깝다면 2 연산 연타
        2. max 위치가 right와 가깝다면 3 연산 연타
"""
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
position = list(map(int, read().strip().split()))
n_operation = 0

q = list(range(1, n+1))
while position:
    if q[0] == position[0]:
        position.pop(0)
        q.pop(0)
    else:
        where = q.index(position[0])
        q = q[where:] + q[:where]
        if where > len(q) / 2:
            where = len(q) - where
        n_operation += where
print(n_operation)
