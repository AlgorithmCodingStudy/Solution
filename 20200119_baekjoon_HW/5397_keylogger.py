"""
5397 키로거

입력으로 키보드입력이 들어온다.
<는 왼쪽 화살표
>는 오른쪽 화살표
-는 백스페이스

비밀번호를 알아내는 프로그램을 구현하라.

알고리즘: 시뮬레이션

1. 입력을 받고 현재 입력과 위치를 선언한다.
2. 전체 입력에서 하나씩 가져와 현재 입력과 위치를 업데이트한다.
"""

import sys
read = sys.stdin.readline

t = int(read().strip())
for _ in range(t):
    keyboard_input = list(read().strip())

    prefix = []
    postfix = []

    for c in keyboard_input:
        if c == '<':
            if prefix:
                postfix.append(prefix.pop())

        elif c == '>':
            if postfix:
                prefix.append(postfix.pop())

        elif c == '-':
            if prefix:
                prefix.pop()
        else:
            prefix.append(c)
    postfix.reverse()
    print("".join(prefix+postfix))
