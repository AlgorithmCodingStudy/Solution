"""
3190 뱀

NxN 맵
뱀의 처음 길이는 1
처음에 오른쪽으로 향한다.
이동하는 칸에 사과가 있으면 사과를 먹고 길이가 1 늘어난다.
사과가 없으면 그냥 이동한다.
자신의 몸에 박아 몇초에 죽는지 출력

알고리즘: 시뮬레이션

1. 리스트 snake에 head부터 tail까지 다 담아두는 방식으로 진행한다.
    0. 초를 세며 꺾어야할 지점을 체크한다.
    1. 다음 칸으로 이동할 위치가 snake에 있다면 종료
    2. 없으면 사과가 있는지 없는지 체크
        1. 사과가 있으면 snake에 새로운 헤드만 추가
        2. 없으면 snake의 tail을 pop하고 새로운 헤드 추가

"""
from collections import deque
import sys
read = sys.stdin.readline

n = int(read().strip())
k = int(read().strip())
apples = [tuple(map(lambda func: int(func)-1, read().strip().split())) for _ in range(k)]
l = int(read().strip())
turns = [tuple(read().strip().split()) for _ in range(l)]
dxy = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # Left, Up, Right, Down

snake = deque()
snake.appendleft((0, 0))
time = 0
now_direction = 2


def straight(second):
    def game_over(a, b):
        if not (0 <= a < n and 0 <= b < n):
            print(time + 1)
            sys.exit(0)
        if (a, b) in snake:
            print(time + 1)
            sys.exit(0)

    def step(a, b):
        if (a, b) in apples:
            snake.appendleft((a, b))
            apples.remove((a, b))
        else:
            snake.appendleft((a, b))
            snake.pop()

    global time
    dx, dy = dxy[now_direction]
    while time < int(second):
        x, y = snake[0]
        nx, ny = x + dx, y + dy
        game_over(nx, ny)
        step(nx, ny)
        time += 1


def change_direction(direction):
    global now_direction
    if direction == 'L':
        now_direction -= 1
    else:
        now_direction += 1
    if now_direction == 4:
        now_direction = 0
    elif now_direction == -1:
        now_direction = 3


for i, (sec, direct) in enumerate(turns):
    straight(int(sec))
    change_direction(direct)

straight(1000000000)
