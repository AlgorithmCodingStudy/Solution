"""
16235 나무 제태크

상도가 나무로 제태크를 한다.
가장 처음에는 모든 칸의 양분이 5다.
이후 K년 만큼 사계절을 반복한다.
    봄
        나무가 자신의 나이만큼 양분을 먹고 나이 += 1
        어린 나무부터 먹는다.
        먹을 양분이 없으면 죽는다.
    여름
        봄에 죽은 나무들이 양분으로 추가
        나무 나이 // 2씩 추가
    가을
        나무가 주변 8칸에 번식한다.
        번식할 수 있는 나무는 나이가 5의 배수다.
    겨울
        A배열 만큼씩 양분을 추가한다.

알고리즘: 시뮬레이션
"""
import sys
read = sys.stdin.readline

n, m, k = map(int, read().split())
A = [list(map(int, read().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
area = [[5]*n for _ in range(n)]
trees_pos = set()
cnt = m

for _ in range(m):
    x, y, z = map(int, read().split())
    trees[x-1][y-1].append(z)
    trees_pos.add((x-1, y-1))


def spring():
    global cnt
    nxt_trees_pos = set()
    for tx, ty in trees_pos:
        nxt_tzs, dead_trees = [], []
        trees[tx][ty].sort()
        for tz in trees[tx][ty]:
            if area[tx][ty] >= tz:
                area[tx][ty] -= tz
                nxt_tzs.append(tz+1)
                nxt_trees_pos.add((tx, ty))
            else:
                dead_trees.append(tz)
                cnt -= 1

        for tz in dead_trees:
            area[tx][ty] += tz//2
        trees[tx][ty] = nxt_tzs

    return nxt_trees_pos


# def summer():
#     for tx, ty, tz in d_trees:
#         area[tx][ty] += tz//2


def fall():
    global cnt
    nxt_trees_pos = set()
    # new_trees = []
    for tx, ty in trees_pos:
        new_tzs = []
        for tz in trees[tx][ty]:
            if tz % 5 == 0:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx, ny = tx + dx, ty + dy
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    trees[nx][ny].append(1)
                    nxt_trees_pos.add((nx, ny))
                    cnt += 1
            new_tzs.append(tz)
        trees[tx][ty] = new_tzs
        nxt_trees_pos.add((tx, ty))

    # for tx, ty in new_trees:
    #     trees[tx][ty].append(1)
    #     nxt_trees_pos.add((tx, ty))

    return nxt_trees_pos


def winter():
    for i in range(n):
        for j in range(n):
            area[i][j] += A[i][j]


for _ in range(k):
    trees_pos = spring()
    # summer()
    trees_pos = fall()
    winter()

# result = 0
# for x, y in trees_pos:
#     result += len(trees[x][y])
print(cnt)
