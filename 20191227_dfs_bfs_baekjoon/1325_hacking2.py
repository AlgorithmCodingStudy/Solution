import sys
read = sys.stdin.readline
n, m = map(int, read().strip().split())
line = [tuple(map(int, read().strip().split())) for _ in range(m)]
if n == 1:
    print(1)

graph = {i: set() for i in range(1, n+1)}
for l in line:
    graph[l[1]].add(l[0])


def dfs(start):
    stack = [start]
    visit = {}
    n_com = 0

    while stack:
        node = stack.pop()

        if node not in visit:
            visit[node] = True
            stack.extend(list(graph[node]))
            n_com += len(graph[node])
    return n_com


def get_parent():
    parent = set()
    child = set()
    for l in line:
        parent.add(l[1])
        child.add(l[0])
    return parent - child


max_value = 0
max_idx = []
for i in get_parent():
    tmp = dfs(i)
    if max_value < tmp:
        max_value = tmp
        max_idx = [i]
    elif max_value == tmp:
        max_idx.append(i)


max_idx.sort()
print(" ".join(map(str, max_idx)))

pass