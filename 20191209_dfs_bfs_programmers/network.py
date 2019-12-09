global_visit = {}


def dfs(graph, start):
    global global_visit
    visit = {}
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visit:
            visit[node] = True
            global_visit[node] = True
            stack.extend(graph[node])

    return 1


def solution(n, computers):
    answer = 0

    graph1 = {i: set() for i in range(n)}
    for i, com in enumerate(computers):
        for j, c in enumerate(com):
            if i == j: continue
            if c == 1:
                graph1[i].add(j)
                graph1[j].add(i)

    for i, com in enumerate(graph1):
        if i not in global_visit:
            answer += dfs(graph1, i)

    return answer

if __name__ == '__main__':
    # print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))