"""
17140 2차원 배열과 연산

정렬을 하면 등장한 횟수가 작은 수부터 같으면 수가 작은수부터 나열한다.

"""
from itertools import chain
import sys
read = sys.stdin.readline

r, c, k = map(int, read().strip().split())
a = [[0]*100 for _ in range(100)]
for o in range(3):
    a[o][0], a[o][1], a[o][2] = map(int, read().strip().split())


def opr(row, col):
    length = 0
    for i in range(row):
        cnt = {}
        for j in range(col):
            v = a[i][j]
            if v == 0: continue
            if v in cnt:
                cnt[v] += 1
            else:
                cnt[v] = 1
        cnt = list(chain(*sorted(cnt.items(), key=lambda key: (key[1], key[0]))))[:100]
        for j, v in enumerate(cnt):
            a[i][j] = v
        for j in range(len(cnt), col):
            a[i][j] = 0
        length = max(len(cnt), length)

    return length


time = 0
max_row, max_col = 3, 3
while a[r-1][c-1] != k:
    if max_row >= max_col:
        max_col = opr(max_row, max_col)
    else:
        a = list(map(list, zip(*a)))
        max_row = opr(max_col, max_row)
        a = list(map(list, zip(*a)))

    time += 1

    if time > 100:
        print(-1)
        sys.exit(0)

print(time)
