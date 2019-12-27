#-*- coding:utf-8 -*-

"""
n개의 컴퓨터와 m개의 신뢰관계가 있다
A가 B를 신뢰하면 B가 A를 해킹 가능하다.
가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터를 오름차순으로 출력

알고리즘: dfs

1. 무식하게 풀어보기
    1. 모든 컴퓨터에 대해 DFS 돌려보기
    2. sorting과 max로 같은 컴퓨터를 오름차순으로 출력
"""
import sys
read = sys.stdin.readline
n, m = map(int, read().strip().split())
line = [tuple(map(int, read().strip().split())) for _ in range(m)]
if n == 1:
    print(1)


def dfs(start):
    stack = [start]
    visit = {}
    n_com = 0
    while stack:
        node = stack.pop()

        if node not in visit:
            visit[node] = True
            for l in line:
                if l[1] == node:
                    stack.append(l[0])
                    n_com += 1

    return n_com


def get_parent():
    parent = set()
    child = set()
    for l in line:
        parent.add(l[1])
        child.add(l[0])
    return parent - child


max_value = 0
max_idx = []
for i in get_parent():
    tmp = dfs(i)
    if max_value < tmp:
        max_value = tmp
        max_idx = [i]
    elif max_value == tmp:
        max_idx.append(i)


max_idx.sort()
print(" ".join(map(str, max_idx)))
