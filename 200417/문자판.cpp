#include <iostream>
#include <queue>
#include <string>
using namespace std;

int N, M, K, s[100][100], rs, dy[4] = { -1,0,1,0 }, dx[4] = { 0,1,0,-1 };
queue<pair<int,int>> q;
char a[100][100];
string st;

int bfs(int y, int x) {
    s[y][x] += 1;    
    q.push({ y,x });
    int len = 1;
    while (!q.empty()) {
        int a = q.front().first;
        int b = q.front().second; 
        q.pop();
        for (int i = 1; i <= K; i++) {
            for (int j = 0; j < 4; j++) {
                int ny = a + (dy[j] * i);
                int nx = b + (dx[j] * i);
                if (ny < 0 || ny >= N || nx < 0 || nx >= M)continue;
                if (a[ny][nx] != st[len])continue;
                if (len == st.length() - 1) continue;
                s[ny][nx] += 1;
                q.push({ ny,nx });
            }
        }
        len++;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (a[i][j] == st[st.length() - 1]) rs += s[i][j];
        }
    }
    return rs;
}

int main()
{
    cin >> N >> M >> K;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> a[i][j];
        }
    }
    cin >> st;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (a[i][j] == st[0]) {
                rs=bfs(i, j);
                break;
            }
        }
    }
}
