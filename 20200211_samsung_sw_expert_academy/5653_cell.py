"""
5653 줄기세포배양

줄기세포가 점점퍼진다.
세포마다 생명력이 주어지는데
비활성상태로부터 X시간 후에 활성상태로 변하고
다시 X시간 후에 죽는다.
활성화된 줄기세포는 첫 시간동안 상하좌우로 퍼진다.
세포가 이미 있으면 안퍼지고
두개가 동시에 퍼지려고 하면 높은 생명력의 세포가 퍼진다.
K시간이 지난후 살아있는 세포의 수를 출력하라.

알고리즘: BFS 시뮬레이션

k가 최대 300인데 그러면 최소 사이클이 2이므로 최대 150칸 퍼질수있다.
(n+k//2)x(n+k//2)
생명력 배열 2차원 (x, y) -1: 죽음, 0: 미방문, else: 살아있음
큐에는 살아있는 세포만 (x, y, state, life)
state 0: 비활성, 1: 활성
life: 활성까지 남은 life or 비활성까지 남은 life
"""
from collections import deque
import sys
sys.stdin = open("input2.txt", "r")


def bfs():
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque(cells)

    for t in range(1, k+1):  # 1~t초까지
        qsize = len(q)
        nxt = []
        for _ in range(qsize):  # q에 있는 것들이 현재 시간에서 살아있는 세포들이므로
            x, y, state, life = q.popleft()  # 위치, 현상태, 남은 life
            if state == 0:  # 비활성 세포인데
                if life == 1:  # 남은 life가 1이면, 즉 다음시간에 활성이면
                    q.append((x, y, 1, area[x][y]))  # state를 1로 바꾸고 life를 원래 세포의 생명력으로 바꿔서 append
                else:  # life가 많이 남았다면
                    q.append((x, y, 0, life-1))  # life 1 깎고 append
            else:  # 활성 세포인데
                if life == area[x][y]:  # 처음이라면 상하좌우로 퍼져야함
                    for dx, dy in dxy:
                        nx, ny = x+dx, y+dy
                        if area[nx][ny] == 0:  # 미방문상태면
                            nxt.append((nx, ny, area[x][y]))  # 우선 nxt에만 추가
                if life == 1:  # 다음시간에 죽는다면
                    area[x][y] = -1  # -1로 바꿔 죽은거 처리
                else:  # life가 남았다면
                    q.append((x, y, 1, life-1))  # life 1 깎고 append

        # 살아있는 세포에 대해 업데이트가 끝났으면 상하좌우로 퍼질 세포들 처리
        for nx, ny, value in nxt:
            if area[nx][ny] < value:  # 겹쳐있을지라도 비교를 통해 더 큰 세포로
                area[nx][ny] = value  # 업데이트
                q.append((nx, ny, 0, value))  # 새로 퍼졌으니 append

    return len(q)  # k 시간이 흐른 후 q에 남아있는 세포들은 살아있는 세포


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    pad = k//2  # 최소 사이클이 2이므로 k를 2로 나눈 몫 만큼 최대로 퍼질 수 있다.
    area = [[0]*(m+pad*2) for _ in range(n+pad*2)]  # 상하좌우 pad만큼 즉 pad*2를 더한 만큼의 지역을 만든다.
    cells = []
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j]:  # 세포가 존재하면
                area[pad+i][pad+j] = line[j]  # padding이 된 area에 초기화
                cells.append((pad+i, pad+j, 0, line[j]))  # 세포의 위치,  비활성 상태, life를 저장

    print("#{} {}".format(test_case, bfs()))
