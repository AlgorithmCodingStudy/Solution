"""
1647 도시 분할 계획

도시를 두개로 분할하려고 한다.
분할한 두 구역끼리는 연결되어 있어야하며 유지비의 합이 최소가 되어야한다.
도시 전체의 최소신장트리를 구하고 가장 큰 유지비를 가지는 길을 끊으면 그게 도시를 두 구역으로 나누는 가장 합리적 방법이 아닐까

알고리즘: MST

1. edge를 모두 입력 받고 오름차순으로 sort한다.
2. 하나씩 가져오며 입력하는데
    1. union-find 알고리즘을 사용한다.
    2. 현재 노드의 부모의 부모의 루트까지 확인했는데 그 루트가 현재 노드가 아니면 사이클이 아니다.
3. 최소신장트리에서 가장 큰 유지비를 가지는 길을 지운다.
4. 유지비의 합을 출력

1234567

12 4567
 3

12 45 7
 3 6

 2 45 7
 3 6
 1

   45 7
   62
    3
    1

    5 7
   42
   63
    1
"""
class Tree(object):
    def __init__(self, value, child=None):
        self.value = value
        self.child = []
        if child is not None:
            for c in child:
                self.add_child(c)
    def __repr__(self):
        return self.value
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.child.append(node)


import sys
read = sys.stdin.readline

def union(x, y):
    def find(z):

        return parent

    root_x, root_y = find(x), find(y)
    if root_x == root_y:
        return False
    global p
    p[root_y] = root_x
    return True


n, m = map(int, read().split())

edges = [list(map(int, read().split())) for _ in range(m)]
edges = sorted(edges, key=lambda x: x[-1])
p = [Tree(i) for i in range(n)]
spanning_tree = []
for from_point, to_point, weight in edges:
    flag = union(from_point, to_point)

    if flag:
        spanning_tree.append(weight)
    if len(spanning_tree) == n-1:
        break
print(sum(spanning_tree[:-1]))