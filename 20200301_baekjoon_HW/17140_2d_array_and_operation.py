"""
17140 2차원 배열과 연산

정렬을 하면 등장한 횟수가 작은 수부터 같으면 수가 작은수부터 나열한다.

"""
from itertools import chain
import sys
read = sys.stdin.readline

r, c, k = map(int, read().strip().split())
a = [list(map(int, read().strip().split())) for _ in range(3)]


def opr():
    nxt, length = [], 0
    for line in a:
        cnt = {}
        for v in line:
            if v in cnt:
                cnt[v] += 1
            else:
                cnt[v] = 1
        if 0 in cnt:
            cnt.pop(0)
        cnt = list(chain(*sorted(cnt.items(), key=lambda key: (key[1], key[0]))))
        nxt.append(cnt)
        length = max(len(cnt), length)

    length = 100 if length > 100 else length
    for idx, line in enumerate(nxt):
        if len(line) < length:
            line += [0]*(length-len(line))
        else:
            nxt[idx] = line[:100]

    return nxt


if a[r-1][c-1] == k:
    print(0)
    sys.exit(0)

time = 0
while True:
    if len(a) >= len(a[0]):
        a = opr()
    else:
        a = list(map(list, zip(*a)))
        a = opr()
        a = list(map(list, zip(*a)))

    time += 1
    try:
        if a[r-1][c-1] == k:
            print(time)
            sys.exit(0)
        if a[r-1][c-1] > 100:
            print(-1)
            sys.exit(0)
    except:
        pass
