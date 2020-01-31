"""
2383 점심 식사시간

사람들이 이동해서 빨리 계단을 내려가서 밥먹으러 가야한다.
계단까지 이동시간 + 계단을 내려가는 시간
계단에는 최대 3명까지만 존재

알고리즘: DFS

1. 계단과 사람의 위치 파악
2. 6C1~6C6까지 모든 조합 계산
3. DFS
    1. 한칸씩 이동하며 상황 파악
    2. 모든 사람들이 계단에 도착하면 종료
    3. 최소 비교
"""
from itertools import combinations
import sys
sys.stdin = open("input.txt", "r")


def get_time(group1, group2):
    def get_distance(x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    def get_group_time(group_d, stair_time):

        def forward(g):
            return list(map(lambda x: x - 1, g))

        def down_stair():
            for ii in range(len(stair_queue[:3])):
                stair_queue[ii] -= 1

        def arrive_stair():
            idx = 0
            for c in range(len(group_d)):
                if group_d[idx] == 0:
                    group_d.pop(0)
                    stair_queue.append(stair_time-1)
                else:
                    idx += 1

        def pop_stair():
            idx = 0
            for i in range(len(stair_queue[:3])):
                if stair_queue[idx] == 0:
                    stair_queue.pop(0)
                else:
                    idx += 1

        if len(group_d) <= 3:
            if group_d:
                return max(group_d) + stair_time + 1
            else:
                return 0
        else:
            time = 2
            group_d = sorted(group_d)
            stair_queue = []
            while group_d or stair_queue:
                group_d = forward(group_d)
                down_stair()
                pop_stair()
                arrive_stair()

                time += 1

            return time+1

    d1 = [get_distance(stair[0][0], stair[0][1], x, y) for x, y in group1]
    d2 = [get_distance(stair[1][0], stair[1][1], x, y) for x, y in group2]
    d1_time = get_group_time(d1, room[stair[0][0]][stair[0][1]])
    d2_time = get_group_time(d2, room[stair[1][0]][stair[1][1]])

    return max(d1_time, d2_time)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    room, human, stair = [], [], []
    for a in range(n):
        room.append(list(map(int, input().split())))
        for b in range(n):
            if room[a][b] == 1:
                human.append((a, b))
            elif room[a][b] > 1:
                stair.append((a, b))

    min_time = 10000000
    all_case = []
    for a in range(0, len(human)+1):
        cases = list(combinations(human, a))
        for case in cases:
            g1 = list(case)
            g2 = list(set(human) - set(case))
            all_case.append((g1, g2))

    for g1, g2 in all_case[:]:
        now_time = get_time(g1, g2)
        if now_time < min_time:
            min_time = now_time
        min_time = min(now_time, min_time)

    print("#{} {}".format(test_case, min_time))
    # ///////////////////////////////////////////////////////////////////////////////////

