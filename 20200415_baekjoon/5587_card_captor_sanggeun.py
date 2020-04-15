"""
5587 카드 캡터 상근이

1-2n까지 카드가 있고
반반 나눠 갖는다.
내는 규칙은
    1. 없으면 아무거나
    2. 있으면 그 카드보다 작은거중에 제일 작은거
    3. 못내면 순서 넘어가고 카드는 사라지기
둘 중 한명이 카드 다 내면 종료
상대방이 갖고 있는 카드의 합이 점수
상근이와 근상이의 점수를 출력하자.

알고리즘: 시뮬레이션

1. 입력 받고 set을 이용해 근상이의 카드팩도 만든다.
2. sorting하자.
3. 하니씩 내면서 결과를 기다린다.
"""

import sys
read = sys.stdin.readline

n = int(read())
sanggeun = list(sorted([int(read()) for _ in range(n)], reverse=False))
geunsang = list(sorted(set(range(1, 2*n+1)) - set(sanggeun), reverse=False))
cards = [sanggeun, geunsang]

turn = False
before_card = 0
while cards[0] and cards[1]:
    idx = -1
    for i, card in enumerate(cards[turn]):
        if card > before_card:
            idx = i
            break

    if idx > -1:
        before_card = cards[turn].pop(idx)
    else:
        before_card = 0

    turn = not turn

print(sum(cards[1]))
print(sum(cards[0]))
