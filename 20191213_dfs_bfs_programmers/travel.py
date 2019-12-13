#-*- coding:utf-8 -*-

# 모든 도시를 방문
# ICN에서 출발
# Ticket 2차원 배열
# [a, b]는 a에서 b로
# 주어진 항공권 모두 사용
# 경로가 두개면 알파벳 순서가 앞서는 경로를 return
# 불가능한 경로 X


def get_path(start, tickets):
    path_result = []
    q = [(start, [start])]

    while q:
        city, path = q.pop(0)

        if len(path) == len(tickets):
            path_result.append(path)
        else:
            for t in tickets:
                if t[0] == city[1] and t not in path:
                    q.append((t, path + [t]))
    return path_result


def solution(tickets):
    starts = [x for x in tickets if x[0] == 'ICN']
    paths = []
    for s in starts:
        path_now = get_path(s, tickets)
        for p in path_now:
            tmp = []
            for q in p:
                tmp.append(q[0])
            tmp.append(p[-1][1])
            paths.append(tmp)

    answer = sorted(paths)[0]
    return answer


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))