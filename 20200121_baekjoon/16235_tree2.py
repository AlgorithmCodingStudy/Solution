"""
NxN 땅을 1x1로 나누어놓고 (r, c)는 (1, 1)부터 시작
양분의 양을 조사해서 상도에게 보내는데 처음엔 모두 5
M개의 나무를 심는닫.
같은 1x1 칸에 여러 나무가 심어져 있을 수 있다.

봄
    봄에 자신의 나이만큼 양분 먹고 나이 += 1
    한 칸에 여러 나무 있다면 나이가 어린 나무부터 양분을 먹는다.
    땅에 양분이 부족하다면 즉시 죽는다.

여름
    봄에 죽은 나무가 양분으로
    죽은 나무의 나이 // 2 만큼 양분으

가을
    번식하는 나무는 나이가 5의 배수
    인접한 8칸에 나이가 1인 나무가 생긴다.

겨울
    S2D2가 양분을 추가한다.
    입력으로 주어진다.

N: 밭의 길이
M: 나무 개수
K: K년후
A: 겨울에 추가하는 양분들
x, y: 나무의 위치
z: 나무의 나이

알고리즘: 시뮬레이션?

0. 나무와 양분 세팅
1. k번의 반복
    1. 봄
        1. 어린 나무(나무들은 리스트, (나이, live flag)부터 양분 먹기
        2. 양분 부족한 나무 죽이기

    2. 여름
        1. 죽은 나무 체크해서 양분 더하기

    3. 가을
        1. 번식하는 나무 체크해서 번식시키기

    4. 겨울
        1. 양분 추가하기
2. 살아있는 나무 수 출력
"""
import heapq
import sys
read = sys.stdin.readline

n, m, k = map(int, read().strip().split())
a = [list(map(int, read().strip().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
energy = [[5]*n for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, read().strip().split())
    heapq.heappush(trees[x-1][y-1], z)


def spring():
    spread = []
    for i in range(n):
        for j in range(n):
            dead = []
            now = trees[i][j]
            if now:
                idx = 0
                while l < len(now):
                    if now[idx] <= energy[i][j]:
                        energy[i][j] -= now_v
                        now[idx] += 1
                        if now[idx] % 5 == 0:
                            spread.append((i, j))
                        idx += 1
                    else:
                        dead.append(now[idx])

                    now_v = heapq.heappop(now)
                    if now_v <= energy[i][j]:
                        energy[i][j] -= now_v

                for l in range(len(now)):
                    if now[idx] <= energy[i][j]:
                        energy[i][j] -= now[idx]
                        now[idx] += 1
                        if now[idx] % 5 == 0:
                            spread.append((i, j))
                        idx += 1
                    else:
                        dead.append(now[idx])
                        now.pop(idx)
            for age in dead:
                summer(i, j, age)
            winter(i, j)
    return spread


def summer(i, j, age):
    energy[i][j] += age // 2


dxy = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def fall(spread):
    for i, j in spread:
        for dx, dy in dxy:
            nx, ny = i+dx, j+dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            trees[nx][ny].append(1)


def winter(i, j):
    energy[i][j] += a[i][j]


for _ in range(k):
    spread_trees = spring()
    fall(spread_trees)

remain = 0
for c in range(n):
    for d in range(n):
        remain += len(trees[c][d])
print(remain)

