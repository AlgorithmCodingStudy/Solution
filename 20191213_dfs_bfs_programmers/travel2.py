#-*- coding:utf-8 -*-

# 모든 도시를 방문
# ICN에서 출발
# Ticket 2차원 배열
# [a, b]는 a에서 b로
# 주어진 항공권 모두 사용
# 경로가 두개면 알파벳 순서가 앞서는 경로를 return
# 불가능한 경로 X

# DFS

# 알고보니 명시되지 않은 조건이 있었다...
# 같은 티켓이 두 개 존재할 수 있음.
# ex) [["ICN", "JFK"], ["ICN", "JFK"], ["JFK", "ICN"], ["JFK", "ABC"]]
#     --> ["ICN", "JFK", "ICN", "JFK", "ABC"]
# 단순히 방문했다고 제외해버리면 티켓 두 개를 모두 쓸 수 없음.

from copy import deepcopy


def get_path(tickets):
    path_result = []
    for start in tickets:
        if start[0] == 'ICN':
            q = [(start, [start])]

            while q:
                city, path = q.pop(0)

                if len(path) == len(tickets):
                    path_result.append(make_path(path))
                else:
                    residual_tickets = deepcopy(tickets)
                    for t in path:
                        if t in tickets:
                            residual_tickets.remove(t)

                    for t in residual_tickets:
                        if t[0] == city[1]:
                            q.append((t, path + [t]))

    return sorted(path_result)[0]


def make_path(path):
    result = []
    for p in path:
        result.append(p[0])
    result.append(path[-1][1])
    return result


def solution(tickets):
    answer = get_path(tickets)
    return answer


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["ICN", "JFK"], ["JFK", "ICN"], ["JFK", "ABC"]]))
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))