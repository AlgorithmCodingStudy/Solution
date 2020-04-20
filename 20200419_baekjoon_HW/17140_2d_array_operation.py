"""
17140 2차원 배열과 연산

r >= c 일때는 r연산
r < c 일때는 c연산

정렬을 하면 빈도횟수, 수의 크기를 오름차순으로 정렬한다.
가장 긴 행과 열을 기준으로 0을 채운다.
100개가 넘어가면 100개까지만 사용한다.
A[r][c] == k가 되는 시간을 구하자.

알고리즘: 시뮬레이션
"""

import sys
read = sys.stdin.readline

r, c, k = map(int, read().split())
a = [list(map(int, read().split())) for _ in range(3)]


def operation(now_a, r_or_c):
    def op():
        new_a, max_length = [], 0
        for row in now_a:
            cnt = {}
            for v in row:
                if v == 0:
                    continue
                if v in cnt:
                    cnt[v] += 1
                else:
                    cnt[v] = 1
            new_line = []
            for key in sorted(cnt, key=lambda x: (cnt[x], x)):
                new_line.extend([key, cnt[key]])
            new_a.append(new_line)
            max_length = max(max_length, len(new_line))

        for i, line in enumerate(new_a):
            new_a[i] = line + [0]*(max_length-len(line))
        for i, line in enumerate(new_a):
            new_a[i] = line[:100]

        return new_a, len(new_a), len(new_a[0])

    def transpose(a_):
        a_ = [list(line) for line in zip(*a_)]
        return a_

    global max_r, max_c
    if r_or_c:
        now_a, max_r, max_c = op()
    else:
        now_a = transpose(now_a)
        max_r, max_c = max_c, max_r
        now_a, max_r, max_c = op()
        now_a = transpose(now_a)
        max_r, max_c = max_c, max_r

    return now_a


time = 0
max_r, max_c = 3, 3
while True:
    try:
        if a[r-1][c-1] == k:
            break
    except IndexError:
        pass
    a = operation(a, max_r >= max_c)
    time += 1
    if time > 100:
        time = -1
        break

print(time)
