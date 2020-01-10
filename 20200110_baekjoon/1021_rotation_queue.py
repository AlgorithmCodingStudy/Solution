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
from collections import deque
from copy import deepcopy
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
position = list(map(int, read().strip().split()))

first_q = deque()
first_q.extend(list(range(1, n+1)))

result = []


def dfs(found, n_operation, q):
    if found == m:
        return result.append(n_operation)
    now_q = deepcopy(q)
    now = now_q.popleft()
    if now == position[found]:
        dfs(found+1, n_operation, now_q)
    else:
        left_q = deepcopy(q)
        right_q = deepcopy(q)
        for i in range(1, n):
            tmp = left_q.popleft()
            if tmp == position[found]:
                dfs(found+1, n_operation+i-1, left_q)
                break
            else:
                left_q.append(tmp)
        for i in range(1, n):
            tmp = right_q.pop()
            if tmp == position[found]:
                dfs(found+1, n_operation+i, right_q)
                break
            else:
                right_q.appendleft(tmp)


dfs(0, 0, first_q)
print(min(result))
