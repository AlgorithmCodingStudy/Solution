"""
1043 거짓말

지민이는 파티에서 진실과 거짓을 말할 수 있다.
근데 진실을 아는 사람들이 있다.
진실을 아는 사람들이 파티에 있을때는 진실을 얘기할 수 밖에 없다.
거짓말을 할 수 있는 파티의 최댓값을 구하라.

알고리즘: 시뮬레이션


                  1
            2           2
        3       3   3       3
1. 파티를 하나씩 가져오며 재귀
    1. 진실을 아는 사람이 있다면 false
    2. 없으면 true or false
        1. true하려는데 진실을 아는 사람이 현재 파티에 있으면 false
            1. 진실을 아는 사람 리스트에 추가
        2. false면 진행


4 3
0
2 1 2
1 3
3 2 3 4

4 3
1 1
2 1 2
1 3
3 2 3 4

거짓
거짓
거짓
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
party = []
for i in range(m+1):
    tmp = read().strip()
    if tmp == '0':
        num, people = 0, []
    else:
        tmp = list(map(int, tmp.split()))
        num, people = tmp[0], tmp[1:]

    if i == 0:
        smart = set(people)
    else:
        party.append(set(people))


def dfs(truth, untruth, depth, cnt):
    if depth == m:
        global max_cnt
        max_cnt = max(max_cnt, cnt)
        return

    now_party = party[depth]
    if now_party.intersection(truth):
        if now_party.intersection(untruth):
            return
        else:
            dfs(truth | now_party, untruth, depth + 1, cnt)
    else:
        if now_party.intersection(untruth):
            dfs(truth, untruth | now_party, depth + 1, cnt + 1)
        else:
            dfs(truth | now_party, untruth, depth + 1, cnt)
            dfs(truth, untruth | now_party, depth + 1, cnt + 1)


max_cnt = 0
dfs(smart, set([]), 0, 0)
print(max_cnt)
