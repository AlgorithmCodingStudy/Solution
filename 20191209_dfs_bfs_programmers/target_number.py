from queue import Queue


def dfs(graph, start, end):
    result = []
    q = Queue()

    q.put((start, [start]))

    while q.qsize() > 0:
        node, path = q.get()

        if node == end:
            result.append(path)
        else:
            for m in graph[node] - set(path):
                q.put((m, path + [m]))

    return result


def dfs_2(graph, start, numbers):
    visit = {}
    q = Queue()

    q.put(start)

    count = 0
    result = 0

    while q.qsize() > 0:
        node = q.get()

        if q.qsize() == 0:
            result +=
        if node not in visit:
            visit[node] = True
            for next_node in graph[node]:
                q.put(next_node)

    return count




def solution(numbers, target):
    answer = 0

    graph = {0: set([1, -1])}
    for i, n in enumerate(numbers):
        graph[i+1] = set([i+2, -(i+2)])
        graph[-(i+1)] = set([i+2, -(i+2)])
    graph[len(numbers)] = set()
    graph[-len(numbers)] = set()

    result0 = dfs(graph, 0, 5)
    result1 = dfs(graph, 0, -5)
    result = result0 + result1

    for case in result:
        tmp = 0
        for v in case[1:]:
            if v > 0:
                tmp += numbers[v-1]
            else:
                tmp -= numbers[-v-1]
        if tmp == target:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))