#include <iostream>
#include <queue>
using namespace std;

int vAll,kAll,R, C, visited[250][250], dx[4] = { -1,1,0,0 }, dy[4] = { 0,0,-1,1 };
char arr[250][250];
queue<pair<int, int>> q;
void bfs(int x, int y) {
    int v = 0, k = 0;
    q.push({ x,y });
    visited[x][y] = 1;
    if (arr[x][y] == 'v') v++;
    if (arr[x][y] == 'k')k++;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= R || ny<0 || ny>=C)continue;
            if (visited[nx][ny] == 1 || arr[nx][ny] == '#')continue;
            if (arr[nx][ny] == 'v') v++;
            if (arr[nx][ny] == 'k')k++;
            q.push({ nx,ny });
            visited[nx][ny] = 1;
        }

    }
    if (v < k) {
        kAll += k;
        
        
    }
    else {
        vAll += v;
       
    }
}
int main()
{
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> arr[i][j];
        }
    }
   
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (visited[i][j] == 0) {
                if (arr[i][j] == 'v' || arr[i][j] == 'k') {
                    bfs(i, j);

                }
            }
            
        }
    }

    cout << kAll << " " << vAll;
}
