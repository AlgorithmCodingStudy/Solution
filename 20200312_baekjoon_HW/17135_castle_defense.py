"""
17135 캐슬 디펜스

적들이 성을 향해 몰려오고 궁수들은 적을 잡는다.
궁수를 N+1칸에 3명 배치시킨다.
궁수는 D이하 거리의 적중에 가장 왼쪽 적을 공격한다.
동시에 같은 적을 공격할수도 있다.
공격이 끝나면 적들은 아래로 한칸 이동한다.
성으로 적이 들어오면 제외된다.
모든 적이 제외되면 경기가 끝난다.
최대로 제거할 수 있는 적을 출력

알고리즘: 시뮬레이션

1. 궁수 세팅 경우 계산
2. 경우에 따라
    0. 죽인 적 = 0
    1. 턴을 기준으로 while 반복
        1. 남은 적 = 0이면 break
        2. 궁수 3명에 대해 가장 가까운 적 측정, 겹칠 수 있음
        3. 제거
        4. 적 아래로 한칸 이동
    2. 죽인 적 max 비교
3. max 출력
"""
from copy import deepcopy
from itertools import combinations
import sys
read = sys.stdin.readline

n, m, d = map(int, read().strip().split())
enemies, remain = [], 0
area = []
for i in range(n):
    area.append(list(map(int, read().strip().split())))
    for j in range(m):
        if area[i][j] == 1:
            enemies.append((i, j))
            remain += 1


def get_kill():
    def get_distance(x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    def get_close_enemy():
        kills = []
        for arrow in arrow_now:
            min_d, close_enemy = sys.maxsize, None
            for enemy in enemy_now:
                now_d = get_distance(*arrow, *enemy)
                if now_d > d:
                    continue
                if now_d < min_d:
                    close_enemy = enemy
                    min_d = now_d
                elif now_d == min_d:
                    if enemy[1] < close_enemy[1]:
                        close_enemy = enemy
                        min_d = now_d

            if close_enemy not in kills:
                kills.append(close_enemy)
        return kills

    remain_now, arrow_now, enemy_now = deepcopy(remain), deepcopy(arrows), deepcopy(enemies)

    kill = 0
    while True:
        if remain_now == 0:
            break

        kill_enemy = get_close_enemy()

        for k in kill_enemy:
            if k == None:
                continue
            enemy_now.remove(k)
            remain_now -= 1
            kill += 1

        enemy_nxt = []
        for enemy in enemy_now:
            nx, ny = enemy[0]+1, enemy[1]
            if nx == n:
                remain_now -= 1
            else:
                enemy_nxt.append((nx, ny))
        enemy_now = enemy_nxt

    return kill


max_kill = 0
for case in combinations(range(m), 3):
    arrows = []
    for c in case:
        arrows.append((n, c))

    now_kill = get_kill()
    max_kill = max(now_kill, max_kill)

print(max_kill)
