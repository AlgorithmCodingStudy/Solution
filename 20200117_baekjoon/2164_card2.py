"""
2164 카드2

1~N 장의 카드가 1이 제일 위 N이 제일 아래로 놓여져있다.
반복
    1. 맨위 버리기
    2. 그다음꺼 제일 아래로 보내기

마지막에 남게 되는 카드는 무엇인가

알고리즘: 시뮬레이션

1. 1~N deque
2. 카드팩의 length를 체크하며 반복
    1. popleft()
    2. popleft() and append()
    3. length가 1이면 break
3. 남은 한장 출력
"""

from collections import deque
import sys
read = sys.stdin.readline

n = int(read().strip())

card = deque()
card.extend(list(range(1, n+1)))

while len(card) > 1:
    card.popleft()
    now = card.popleft()
    card.append(now)

print(card[0])
