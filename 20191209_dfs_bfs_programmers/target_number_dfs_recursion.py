from copy import deepcopy

count = 0


def dfs_recursion(graph, nodes, visit, result, target, numbers):
    global count
    if len(visit) == len(numbers):
        if result == target:
            count += 1
        return
    else:
        while nodes:
            node = nodes.pop()
            if node > 0:
                next_result = result + numbers[node-1]
            else:
                next_result = result - numbers[-node-1]
            if node not in visit:
                visit[node] = True
                dfs_recursion(graph, deepcopy(graph[node]), deepcopy(visit), next_result, target, numbers)
                visit.pop(node)


def solution(numbers, target):
    answer = 0

    graph = {0: set([1, -1])}
    for i, n in enumerate(numbers):
        graph[i+1] = set([i+2, -(i+2)])
        graph[-(i+1)] = set([i+2, -(i+2)])
    graph[len(numbers)] = set()
    graph[-len(numbers)] = set()

    dfs_recursion(graph, deepcopy(graph[0]), {}, 0, target, numbers)

    answer = count
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))