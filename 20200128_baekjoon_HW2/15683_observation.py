"""
15683 감시

CCTV가 5종류 있다.
1 -> 1방향
2 <- -> 2방향
3 90도 2방향
4 3방향
5 4방향
6 벽
CCTV는 벽을 통과할 수 없고 CCTV는 통과할 수 있다.
CCTV 정보가 주어졌을때 각도를 조정해서 사각지대를 최소하는 경우의 넓이를 출력

알고리즘: 시뮬레이션

1. CCTV 위치를 확인
2. 재귀로 경우를 모두 확인
3. 감시영역을 업데이트
4. 사각지대 계산
5. 최소비교
"""
from copy import deepcopy
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
room = []
cctvs = []
for i in range(n):
    room.append(list(map(int, read().strip().split())))
    for j in range(m):
        if 0 < room[i][j] < 6:
            cctvs.append((i, j))

min_cnt = 64
dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def set_cctv(arr):
    def check_range(_x, _y):
        return 0 <= _x < n and 0 <= _y < m

    def generate(depth, now_room):
        def get_blind():
            result = 0
            for line in now_room:
                result += line.count(0)
            return result

        def observe(_dx, _dy):
            nx, ny = x, y
            while check_range(nx + _dx, ny + _dy):
                nx, ny = nx + _dx, ny + _dy
                if nxt_room[nx][ny] == 0:
                    nxt_room[nx][ny] = 7
                elif nxt_room[nx][ny] == 6:
                    break

        if depth == len(cctvs):
            cnt = get_blind()
            global min_cnt
            min_cnt = min(cnt, min_cnt)
            return

        x, y = arr[depth]
        now_cctv = room[x][y]

        if now_cctv == 1:
            for dx, dy in dxy:
                nxt_room = deepcopy(now_room)

                observe(dx, dy)

                generate(depth+1, nxt_room)

        elif now_cctv == 2:
            for dx, dy in dxy[:2]:
                nxt_room = deepcopy(now_room)

                observe(dx, dy)

                observe(-dx, -dy)

                generate(depth+1, nxt_room)

        elif now_cctv == 3:
            for idx, (dx, dy) in enumerate(dxy):
                nxt_room = deepcopy(now_room)

                observe(dx, dy)

                idx = idx+1 if idx < 3 else 0
                dx, dy = dxy[idx]
                observe(dx, dy)

                generate(depth+1, nxt_room)

        elif now_cctv == 4:
            for idx, (dx, dy) in enumerate(dxy):
                nxt_room = deepcopy(now_room)

                observe(dx, dy)

                idx = idx + 1 if idx < 3 else 0
                dx, dy = dxy[idx]
                observe(dx, dy)

                idx = idx + 1 if idx < 3 else 0
                dx, dy = dxy[idx]
                observe(dx, dy)

                generate(depth + 1, nxt_room)

        elif now_cctv == 5:
            nxt_room = deepcopy(now_room)

            for dx, dy in dxy:
                observe(dx, dy)

            generate(depth+1, nxt_room)

    generate(0, room)


set_cctv(cctvs)
print(min_cnt)
