"""
4811 알약

N개의 약을 먹는데 반씩 먹는다.
꺼낸 알이 새거면 W
반개짜리면 H
2N 동안

1 2 1 wh
2 4 2 wwhh 1+1
      whwh
3 6 5 wwwhhh 2+2+1
      wwhhwh wwhwhh
      whwhwh whwwhh
4 8 14 wwwwhhhh 5+5+3+1
       wwwhwhhh wwwhhwhh wwwhhhwh
       wwhwhwhh wwhwwhhh wwhhwwhh wwhhwhwh wwhhwhwh
       whwhwhwh whwwwhhh whwwhwhh whwwhhwh whwhwwhh
5 10 42 14+14+9+4+1
6 12 132 42+42+28+14+5+1

1 whwhwh whwwhh 2 * 1
2 wwhhwh wwhwhh 2 * 1
3 wwwhhh 1



"""
from itertools import permutations
import sys
read = sys.stdin.readline

n = int(read())
s = ['w']*n + ['h']*n
result = []
cases = set(permutations(s, 2*n))
for i, test_s in enumerate(list(cases)):
    w, h = 0, 0
    flag = True
    for c in test_s:
        if c == 'w':
            w += 1
        else:
            h += 1
        if w < h:
            flag = False
            break

    if flag:
        result.append(test_s)

result = sorted(set(result))
pass