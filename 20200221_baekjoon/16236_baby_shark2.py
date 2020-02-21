"""
16236 아기 상어

아기 상어가 물고기를 잡아 먹으러 다닌다.
자기보다 작은 물고기만 먹을 수 있다.
1초에 상하좌우로 이동가능
자기보다 큰 물고기가 있는 칸은 못 지나간다.
같은 크기의 물고기가 있는 칸은 지나간다.

더이상 먹을 수 있는 물고기가 없으면 끝
먹을 수 있는 물고기가
    1마리면 그거 먹음
    여러마리면 비교
        가장 가까운 물고기 먹음
            여러마리면
                가장 위에 물고기
                    여러마리면
                        가장 왼쪽 물고기
크기가 2인 물고기가 2마리 물고기 먹으면 3으로 성장

2 <= N <= 20
0 빈칸
1-6 물고기
9 아기상어

알고리즘: BFS

1. 물고기들의 크기와 위치를 저장하고 크기순으로 정렬
2. 반복
    1. 현위치로부터 먹을 수 있는 가장 가까운 물고기 찾고 거리 저장
    2. 그곳으로 위치이동 및 시간 추가
    3. 물고기 없애기
    4. 물고기 먹은 수 업데이트
        1. 크기만큼 먹었으면 크기 up
"""
from collections import deque
import sys
read = sys.stdin.readline

n = int(read().strip())

fishes = []
area = []
for a in range(n):
    area.append(list(map(int, read().strip().split())))
    for b, v in enumerate(area[a]):
        if v == 9:
            baby_shark = [2, a, b, 0]


dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_fish():
    age, sx, sy, _ = baby_shark
    visit = {(sx, sy): True}
    q = deque([([(sx, sy)], sx, sy)])
    fishes_tmp = []
    while q:
        path, x, y = q.pop()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            fish_age = area[nx][ny]
            if 0 < fish_age < age and (nx, ny) not in fishes_tmp:
                fishes_tmp.append((path+[(nx, ny)], nx, ny))
                visit[(nx, ny)] = True
            elif (fish_age == 0 or fish_age == age) and (nx, ny) not in visit:
                q.append((length+1, nx, ny))
                visit[(nx, ny)] = True

    if fishes_tmp:
        fishes_tmp = sorted(fishes_tmp)
        min_length = fishes_tmp[0][0]
        tmp = []
        for length, x, y in fishes_tmp[:]:
            if min_length == length:
                tmp.append((x, y))
        tmp = sorted(tmp)
        x, y = tmp[0]
        result = (area[x][y], x, y)
        return min_length, result

    return 0, 0


def grow():
    if baby_shark[0] == baby_shark[3]:
        baby_shark[0] += 1
        baby_shark[3] = 0


time = 0

while True:
    distance, fish = find_fish()
    if distance == 0:
        break

    baby_shark = [baby_shark[0], fish[1], fish[2], baby_shark[3]+1]

    grow()

    time += distance

    area[fish[1]][fish[2]] = 0


print(time)