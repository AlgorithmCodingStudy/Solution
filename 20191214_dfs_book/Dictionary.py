#-*- coding:utf-8 -*-

"""
DICTIONARY 고대어 사전

입력으로 들어온 고대어 단어들을 기준으로 고대어의 알파벳 순서를 유추하는 문제
알파벳 순서의 모순이 있다면 INVALID HYPOTHESIS

ex)
gg
kia
lotte
lg
hanhwa

알고리즘: DFS, 위상정렬

1. dfs를 실행, 첫번째 문자들을 검사한다.
2. 다음 것과 같지 않으면 path에 추가
3. 같으면 첫번째 문자를 제외한 두 단어를 stack에 추가
"""


def make_graph(words):
    graph = []
    for i, w in enumerate(words):
        if i == 0:
            # graph.append(list(w)[0])
            continue
        w1, w2 = list(words[i-1]), list(w)
        length = min(len(w1), len(w2))
        w1_, w2_ = w1[:length], w2[:length]
        for c1, c2 in zip(w1_, w2_):
            if c1 == c2:
                graph.extend(make_graph([w1[1:], w2[1:]]))
            else:
                graph.append((c1, c2))
            break
    return graph


def dfs(start, graph):
    visit = {}
    stack = [start]
    path = [start[0]]

    while stack:
        node = stack.pop()

        if node not in visit:
            visit[node] = True
            path.append(node[1])
            for n in graph:
                if node[1] == n[0]:
                    stack.append(n)

    return path


if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    c = int(input())
    case = []
    for _ in range(c):
        n = int(input())
        words = [input() for _ in range(n)]
        case.append(words)

    for words in case:
        graph1 = make_graph(words)

        invalid = False
        for g in graph1:
            path = dfs(g, graph1)
            if len(path) != len(set(path)):
                invalid = True

            if len(path) == len(graph1) + 1:
                break

        if invalid:
            result = "INVALID HYPOTHESIS"
        else:
            result = path + sorted(list(set(alphabet) - set(path)))
        print("".join(result))