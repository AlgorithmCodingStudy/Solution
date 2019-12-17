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
    q = [(start, [start])]
    visit = {}
    while q:
        node, path = q.pop(0)
        visit[node] = True
        if node == end:
            print(len(path)-1)
            return
        else:
            next_list = [node + 1, node - 1, node + a, node - a, node + b, node - b, node * a, node * b]
            for nxt in next_list:
                if nxt not in path and nxt not in visit:
                    q.append((nxt, path + [nxt]))


def get_next(node, end, a, b):
    next_node = [node+1, node-1, node+a, node-a, node+b, node-b, node*a, node*b]

    diff = list(map(lambda x: abs(end-x), next_node))
    # if diff
    min_diff = 100000
    for i, d in enumerate(diff):
        if d < min_diff:
            min_diff = d
            min_idx = i
    return next_node[min_idx]


if __name__ == '__main__':
    a1, b1, n, m = map(int, sys.stdin.readline().split())

    bfs(n, m, a1, b1)

