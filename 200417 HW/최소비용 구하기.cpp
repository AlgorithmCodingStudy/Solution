#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int INF = 987654321;
typedef pair<int, int> P;

priority_queue<P> pq;
vector<P> adj[1005];
vector<int> dist(1005, INF);

int n, m,u,v,w,A,B;
void dijkstra(int st) {
    dist[st] = 0;
    pq.push({ 0,st });
    while (!pq.empty()) {
        int now = pq.top().second;
        int cost = -pq.top().first;
        pq.pop();
        if (dist[now] < cost)continue;
        for (auto& e : adj[now]) {
            int nv = e.first;
            int nw = e.second;
            if (dist[nv] > nw + cost) {
                dist[nv] = cost + nw;
                pq.push({ -(cost + nw),nv });
            }
        }

    }
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        adj[u].push_back({ v,w });
    }
    
    cin >> A >> B;
    dijkstra(A);
    cout << dist[B];
}
