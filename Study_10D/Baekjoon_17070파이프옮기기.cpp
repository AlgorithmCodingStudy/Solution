#include<iostream>
#include<queue>
 /*
 0: 빈칸, 1: 벽, 2:파이프
 */

using namespace std;

int N;
int house[20][20] = { 0 };
bool visit[20][20];
struct Pipe { int x1, x2, y1, y2; };
queue < pair <Pipe,int> >Q;

int Direction(int x1, int x2, int y1, int y2)
{
    if (x1 == x2) //가로일경우
    {
        return -1;
    }
    if (y1 == y2) // 세로일경우
    {
        return -2;
    }
    if (abs(x1 - x2) > 0 && abs(y1 - y2) > 0)//대각선일경우
    {
        return -3;
    }
}

int BFS()
{
    while (!Q.empty())
    {
        int cx1 = Q.front().first.x1;
        int cy1 = Q.front().first.y1;
        int cx2 = Q.front().first.x2;
        int cy2 = Q.front().first.y2;
        int cnt = Q.front().second;

        int dir = Direction(cx1,cx2,cy1,cy2);

        cout << cx1<<" " << cy1<<" " << cx2 <<" "<< cy2 << endl;
        cout << dir << endl;

        Q.pop();

        if ((cx2 == N && cy2 == N) )
        {
            return cnt;
        }

        if (dir == -1) // 가로
        {
            int nx1 = cx1;
            int nx2 = cx2;
            int ny1 = cy1 + 1;
            int ny2 = cy2 + 1;
            if ( ny1 > N || ny2 > N)continue;
            if (house[nx2][ny2] == 0)
            {
                //cout << nx1 << nx2 << ny1 << ny2 << endl;
                Q.push({ { nx1,nx2,ny1,ny2},cnt + 1 });
                house[nx1][ny1] = 2;
                house[nx2][ny2] = 2;
            }

            nx1 = cx1;
            nx2 = cx2 + 1;
            ny1 = cy1 + 1;
            ny2 = cy2 + 1;
            if ( nx2 > N || ny1 > N || ny2 > N)continue;
            if (house[nx1][ny1] == 0 && house[nx2][ny2] == 0 && house[nx1][ny1 + 1] == 0 && house[nx2][ny1] == 0)
            {
                Q.push({ { nx1,nx2,ny1,ny2 },cnt + 1 });
                house[nx1][ny1] = 2;
                house[nx2][ny2] = 2;
            }
        }

        if (dir == -2) //세로
        {
            int nx1 = cx1 + 1;
            int nx2 = cx2 + 1;
            int ny1 = cy1;
            int ny2 = cy2;
            if (nx2 > N || nx1 > N)continue;
            if (house[nx2][ny2] == 0)
            {
                Q.push({ { nx1,nx2,ny1,ny2 },cnt + 1 });
                house[nx1][ny1] = 2;
                house[nx2][ny2] = 2;
            }

            nx1 = cx1 + 1;
            nx2 = cx2 + 1;
            ny1 = cy1;
            ny2 = cy2 + 1;
            if (nx1> N || nx2 > N || ny2 > N)continue;
            if (house[nx1][ny1] == 0 && house[nx2][ny2] == 0 && house[nx1 + 1][ny1] == 0 && house[nx1][ny2] == 0)
            {
                Q.push({ { nx1,nx2,ny1,ny2 },cnt + 1 });
                house[nx1][ny1] = 2;
                house[nx2][ny2] = 2;
            }
        }

        if (dir == -3) //대각선
        {
            int nx1 = cx2;
            int nx2 = cx2;
            int ny1 = cy2;
            int ny2 = cy2 + 1;
            if (ny2 > N)continue;
            if (house[nx2][ny2] == 0)
            {
                Q.push({ { nx1,nx2,ny1,ny2 },cnt + 1 });
                house[nx1][ny1] = 2;
                house[nx2][ny2] = 2;
            }
             
            nx1 = cx2;
            nx2 = cx2 + 1;
            ny1 = cy2;
            ny2 = cy2;

            if (nx2 > N)continue;
            if (house[nx2][ny2] == 0)
            {
                Q.push({ { nx1,nx2,ny1,ny2 },cnt + 1 });
                house[nx1][ny1] = 2;
                house[nx2][ny2] = 2;
            }
            nx1 = cx2;
            nx2 = cx2 + 1;
            ny1 = cy2;
            ny2 = cy2 + 1;
            if (nx2 > N || ny2 > N)continue;
            if (house[nx2][ny2] == 0 && house[nx1][ny2] == 0 && house[nx2][ny1] == 0)
            {
                Q.push({ { nx1,nx2,ny1,ny2 },cnt + 1 });
                house[nx1][ny1] = 2;
                house[nx2][ny2] = 2;
            }
        }
    }
    return -1;
}
int main()
{
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin>>house[i][j];
        }
    }
    
    house[1][1] = 2;
    house[1][2] = 2;
    Q.push({ {1,1,1,2},0 });
    int result = BFS();

    if (result == -1) {
        cout << '0';
        return 0;
    }
    else {
        cout << result;
        return 0;
    }
}
