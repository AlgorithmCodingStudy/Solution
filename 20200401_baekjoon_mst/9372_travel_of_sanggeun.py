"""
9372 상근이의 여행

상근이가 여행을 하는데 비행기를 최소로 타서 모든 도시를 가고 싶다.
비행기 종류의 최소개수를 출력하라.

알고리즘: 최소 신장 트리

가중치는 없고 모든 정점을 방문하는데 최소한의 간선을 사용해야한다.
다시 방문했던 국가를 방문할 수 있다.
BFS로 모든 간선으로 나아가며 다 계산해보다가 모든 정점을 방문한 것이 확인되면 그때 간선을 사용한 횟수를 리턴하면 되지 않을까?

그러면 queue에 방문한 국가들을 넣자.

가 아니라 spanning tree의 간선은 무조건 n-1이다...
"""
import sys
read = sys.stdin.readline

t = int(read())
for _ in range(t):
    n, m = map(int, read().split())
    _ = [read() for _ in range(m)]
    print(n-1)
