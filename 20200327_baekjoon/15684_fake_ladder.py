"""
15684 사다리 조작

사다리를 타는데 i에서 출발하면 i에 도착할 수 있도록 조작해야한다.
사다리를 추가함으로써 조작할 수 있는데 추가한 사다리의 최솟값을 출력
추가해야하는 사다리가 4개이상이면 -1 출력

알고리즘: 시뮬레이션, 완전탐색

1. 입력을 받으면서 사다리를 세팅한다.
2. 0인 곳 확인
3. 3번반복
    1. combinations(1, 2, 3)
        1. 찾아진 조합중에 가로가 바로 옆인 경우는 제외
    2. 경우에 따라 사다리를 설치한 후 check
        1. 맞으면 break
4. 출력
"""
from itertools import combinations
import sys
read = sys.stdin.readline

n, m, h = map(int, read().split())
ladder = [[0]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, read().split())  # h, n
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = -1

empty = []
for i in range(h):
    for j in range(n-1):
        if ladder[i][j] == 0 and ladder[i][j+1] == 0:
            empty.append((i, j))

def check_available_case(c):
    before = c[0]
    for value in c[1:]:
        if before[0] == value[0] and before[1] + 1 == value[1]:
            return False
        before = value
    return True

def set_ladder(c):
    for x, y in c:
        ladder[x][y] = 1
        ladder[x][y+1] = -1

def remove_ladder(c):
    for x, y in c:
        ladder[x][y] = 0
        ladder[x][y+1] = 0

def check_ladder():
    for vertical in range(n):
        start = vertical
        for horizontal in range(h):
            if ladder[horizontal][vertical] == 1:
                vertical += 1
            elif ladder[horizontal][vertical] == -1:
                vertical -= 1
        if start != vertical:
            return False
    return True

if check_ladder():
    print(0)
    sys.exit(0)
success = False
for cnt in range(3):
    cases = list(sorted(combinations(empty, cnt+1)))
    for case in cases:
        if not check_available_case(case):
            continue
        set_ladder(case)

        if check_ladder():
            success = True
            break

        remove_ladder(case)
    if success:
        break

cnt = cnt+1 if success else -1
print(cnt)