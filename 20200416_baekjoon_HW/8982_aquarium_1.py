"""
8982 수족관 1

수족관이 있고 구멍을 몇개 뚫어 남는 물의 양을 구해야한다.
수족관은 꼬불꼬불 생겨서 물이 다양하게 남는다.

알고리즘: 시뮬레이션

1. 수족관의 모양을 받는다.
2. 구멍의 위치를 받는다.
3. 구멍들중 높이 있는 구멍부터 차례로 가져온다.
    1. 맨위부터 구멍의 위치까지 한줄한줄 검토
        1. 내려오면서 좌우로 검토해서 벽이 있다면 거기까지만 물을 없앤다.
"""

import sys
read = sys.stdin.readline
n = int(read())
depth = []
x, y = map(int, read().split())
for _ in range((n-2)//2):
    x1, y1 = map(int, read().split())
    x2, y2 = map(int, read().split())
    for j in range(x1, x2):
        depth.append(y1)
width, y = map(int, read().split())

water = [0]*width
holes = []
for _ in range(int(read())):
    x1, y1, x2, y2 = map(int, read().split())
    holes.append(x1)

for hx in holes:
    now_depth = depth[hx]
    water[hx] = now_depth

    for j in range(hx-1, -1, -1):
        now_depth = min(now_depth, depth[j])
        water[j] = max(water[j], now_depth)

    now_depth = depth[hx]

    for j in range(hx+1, width):
        now_depth = min(now_depth, depth[j])
        water[j] = max(water[j], now_depth)

result = sum([d - w for d, w in zip(depth, water)])
print(result)
