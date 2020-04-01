import sys
read = sys.stdin.readline

n = int(read())
start, end = map(int, read().split())
m = int(read())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)


q = [start]
visit = {start: True}

num = 0
while q:
    new_q = []
    for now in q:
        if now == end:
            print(num)
            sys.exit(0)
        for nxt in graph[now]:
            if nxt not in visit:
                visit[nxt] = True
                new_q.append(nxt)
    q = new_q
    num += 1
print(-1)