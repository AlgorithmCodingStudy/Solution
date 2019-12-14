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

alphabet = None
seen = None
order = None


def make_graph(words):
    global alphabet
    for i, w in enumerate(words):
        if i == 0: continue
        # 현재 단어와 이전 단어
        w1, w2 = list(w), list(words[i-1])
        # 짧은 길이로 설정
        length = min(len(w1), len(w2))
        w1_, w2_ = w1[:length], w2[:length]
        for c1, c2 in zip(w1_, w2_):
            if c1 != c2:  # 처음부터 가져와서 문자가 다르면
                a = ord(c1) - 97
                b = ord(c2) - 97
                alphabet[a][b] = 1
                break


def dfs(here):
    seen[here] = 1
    for there, seen_there in enumerate(seen):
        # 다음 문자가 가능하고 방문하지 않았다면
        if alphabet[here][there] and not seen_there:
            dfs(there)
    # 경로를 추가
    order.append(here)


def topologicalSort():
    global alphabet, seen, order
    seen = [0 for _ in range(26)]
    order = []

    for i, v in enumerate(seen):
        if not v:
            dfs(i)

    # 경로 뒤집기
    reversed(order)

    for i in range(len(alphabet)):
        for j in range(i+1, len(alphabet)):
            # 역방향 간선이 존재한다면 불가능
            if alphabet[order[i]][order[j]]:
                return []
    # 없으면 위상정렬 완료
    return order


if __name__ == '__main__':
    idx2char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    c = int(input())
    for _ in range(c):
        n = int(input())
        word = [input() for _ in range(n)]

        alphabet = [[0 for _ in range(26)] for _ in range(26)]

        make_graph(word)
        result = topologicalSort()

        if result:
            print("".join(map(lambda x: idx2char[x], result)))
        else:
            print("INVALID HYPOTHESIS")
