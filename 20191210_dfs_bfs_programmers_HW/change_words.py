def bfs(begin, target, words):
    q = [(begin, [begin])]

    while q:
        node, path = q.pop(0)
        if node == target:
            return len(path) - 1
        else:
            for w in words:
                if check_next(node, w) and w not in set(path):
                    q.append((w, path + [w]))


def check_next(tar, dst):
    n_equal = sum(map(lambda x, y: True if x != y else False, list(tar), list(dst)))

    if n_equal == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        count = 0
    else:
        count = bfs(begin, target, words)
    answer = count
    return answer


if __name__ == '__main__':
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))