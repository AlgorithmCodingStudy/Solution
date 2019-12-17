#-*- coding:utf-8 -*-

"""
12761 돌다리

동규 N에서 주미 M으로 최소한의 이동 횟수
가는 방법:
1. +1 -1
2. +A -A
3. +B -B
4. *A *B

알고리즘: BFS

알고리즘이 BFS니깐 BFS로 고민을 해보면
1. 이동할 수 있는 경우가 8가지
2. 그 중 멀어지는 것 제외 (현재 남은 거리로 체크?)
3. 이런식으로 BFS로 구하다 제일 먼저 end에 도달하면 종료하고 그때 path의 length를 출력?
"""

import sys


def bfs(start, end, a, b):
    q = [(start, 0)]
    visit = {}

    while q:
        node, length = q.pop(0)
        if node == end:
            return length
        else:
            next_list = [node + 1, node - 1, node + a, node - a, node + b, node - b, node * a, node * b]
            for nxt in next_list:
                if 0 <= nxt <= 100000 and nxt not in visit:
                    visit[nxt] = True
                    q.append((nxt, length+1))


if __name__ == '__main__':
    a1, b1, n, m = map(int, sys.stdin.readline().split())

    print(bfs(n, m, a1, b1))

