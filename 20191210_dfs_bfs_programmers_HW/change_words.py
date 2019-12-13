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
    # tar와 dst의 같지 않은 수를 리턴
    n_equal = sum(map(lambda x, y: True if x != y else False, list(tar), list(dst)))

    # 하나만 같을 경우 True
    if n_equal == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    # target이 words에 없으면 변환할 수 없으므로 answer = 0
    if target not in words:
        answer = 0
    else:
        answer = bfs(begin, target, words)
    return answer


if __name__ == '__main__':
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))