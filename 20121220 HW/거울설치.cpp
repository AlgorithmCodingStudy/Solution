include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

struct mirror {
    int x, y, z; 
};

int n, ex, ey;
char a[50][50];
int dist[50][50][4];
queue<mirror> q;
const int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};

bool move(int x, int y, int z) {
    if (x < 0 || x >= n || y < 0 || y >= n) return false;
    if (dist[x][y][z] == '*') return false;
    return true;
}

void bfs() {
    while (!q.empty()) {
        int x = q.front().x, y = q.front().y, z = q.front().z; q.pop();
        if (x == ex && y == ey) {
            printf("%d\n", dist[x][y][z]);
            return;
        }
        int nx = x+dx[z], ny = y+dy[z];
        while (move(nx, ny, z) && a[nx][ny] == '.') {
            nx += dx[z], ny += dy[z];
        } 
        //이동 가능하고 거울을 놓을 수 있으면
        if (move(nx, ny, z) && a[nx][ny] == '!') {
            dist[nx][ny][z] = dist[x][y][z];
            // x좌표, y좌표, 이동방향 큐에 넣는다
            q.push({nx, ny, z});
            int k = z < 2 ? 2 : 0;
            for (int i=k; i<k+2; i++) {
                if (dist[nx][ny][i] == -1) {
                    dist[nx][ny][i] = dist[x][y][z]+1;
                    q.push({nx, ny, i});
                }
            }
        }
    }
}

int main() {
    scanf("%d", &n);
    memset(dist, -1, sizeof(dist));
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            scanf(" %1c", &a[i][j]);
            if (a[i][j] == '#') {
                if (q.empty()) {
                    for (int k=0; k<4; k++) {
                        q.push({i, j, k});
                        dist[i][j][k] = 0;
                    }
                } else {
                    ex = i, ey = j;
                }
                a[i][j] = '!';
            }
        }
    }
    bfs();
    return 0;
}


출처: https://rebas.kr/781 [PROJECT REBAS]
