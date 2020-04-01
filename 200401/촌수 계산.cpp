#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, from, to, m, x, y,cnt,visited[101];
vector<int> v[101];
queue<int> q;

int bfs(int start) {

    visited[start] = 1;
    q.push(start);
    while (!q.empty()) {
        start = q.front();
        //cout << start << "pop!" << "\n";
        q.pop();
        if (start == to) return visited[start]-1;
        for (int i = 0; i < v[start].size(); i++) {
            //cout << v[start][i] << "in" << "\n";
            int tem = v[start][i];
            if (visited[tem] == 0) {
                visited[tem] = visited[start] + 1;
                q.push(tem);
            }
            
        }
                     
    }
    return -1;
}

int main()
{
    cin >> n;
    cin >> from >> to;
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    cout<<bfs(from);
}

