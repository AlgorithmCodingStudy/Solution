#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
 
using namespace std;
 
int map[10][10];
int result;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
bool visit[10][10][2]; //[][][0]:등산로안깍은거, [][][1]:등산로깍은거
int T, N, K;
struct info {
    int x, y, len;
};
vector<info>V;
 
void print()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << visit[i][j][0];
        }
        cout << endl;
    }
    cout << endl;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << visit[i][j][1];
        }
        cout << endl;
    }
    cout << endl;
}
void DFS(info cur, int broken, int count, int no);
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    cin >> T;
    for (int q = 1; q <= T; q++)
    {
        //초기화
        N = 0; K = 0;
        result = -99999999;
        int mmax = -99999999;
        V.clear();
        memset(map, 0, sizeof(map));
        memset(visit, false, sizeof(visit));
 
        //입력
        cin >> N >> K;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                cin >> map[i][j];
                mmax = max(mmax, map[i][j]);
            }
        }
 
        //시작점찾기
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (map[i][j] == mmax)
                    V.push_back({ i,j,mmax });
            }
        }
 
        for (int i = 0; i < V.size(); i++)
        {
            visit[V[i].x][V[i].y][0] = true;
            DFS(V[i], 0, 1, 0);
            visit[V[i].x][V[i].y][0] = false;
        }
 
        cout <<'#'<<q<<' '<< result << endl;
    }
 
    return 0;
}
 
 
void DFS(info cur, int broken, int count, int no)
{
 
    for (int i = 0; i < 4; i++)
    {
        int nx = cur.x + dx[i];
        int ny = cur.y + dy[i];
 
        if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
 
        if (broken == 0 && !visit[nx][ny][broken]) // 한번도 안깍은경우
        {
            if (cur.len <= map[nx][ny])//산을 깍을때,
            {
                for (int j = 1; j <= K; j++) {
 
                    int changelen = map[nx][ny] - j;
                    if (cur.len > changelen)
                    {
                        visit[nx][ny][broken + 1] = true;
                        DFS({ nx,ny,changelen }, broken + 1, count + 1, 0);
                        visit[nx][ny][broken + 1] = false;
                        continue;
                    }
                }
 
            }
            else if (cur.len > map[nx][ny])//산을 안깍을때
            {
                visit[nx][ny][broken] = true;
                DFS({ nx,ny,map[nx][ny] }, broken, count + 1, 0);
                visit[nx][ny][broken] = false;
                continue;
            }
        }
        else if (broken == 1 && !visit[nx][ny][broken])
        {
            if (cur.len > map[nx][ny])
            {
                visit[nx][ny][broken] = true;
                DFS({ nx,ny,map[nx][ny] }, broken, count + 1, 0);
                visit[nx][ny][broken] = false;
                continue;
            }
        }
 
        if (result < count)
            result = count;
 
    }
 
}
