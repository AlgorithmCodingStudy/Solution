#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

struct info { int x, y, k; };
int K,W,H;
int map[250][250];
int visit[250][250][35]; //x,y,k의값
int Mmin = 987654321;
int Hdx[] = { -2,-2,-1,-1,1,1,2,2 };
int Hdy[] = { -1,1,-2,2,-2,2,-1,1};
int Mdx[] = { -1,1,0,0 };
int Mdy[] = { 0,0,-1,1 };

queue<info>Q;

void BFS();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> K;
	cin >> W >> H;

	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < W; j++)
		{
			cin >> map[i][j];
		}
	}


	Q.push({ 0,0,0 });
	visit[0][0][0] = 1;

	BFS();

	if (Mmin == 987654321) cout << -1 << endl;
	else
		cout << Mmin-1 << endl;

	return 0;
}

void BFS()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int ck = Q.front().k;
		Q.pop();

		if (cx == H - 1 && cy == W - 1)
		{
			Mmin = min(Mmin, visit[cx][cy][ck]);
		}

		if (ck<K)
		{
			for (int i = 0; i < 8; i++) //말
			{
				int nx = cx + Hdx[i];
				int ny = cy + Hdy[i];
				int nk = ck + 1;

				if (nx < 0 || ny < 0 || nx >= H || ny >= W)continue;

				if (visit[nx][ny][nk] == 0 && map[nx][ny]== 0)
				{
					Q.push({ nx,ny,nk });
					visit[nx][ny][nk] = visit[cx][cy][ck] + 1;
				}
			}

			for (int i = 0; i < 4; i++) //원숭이
			{
				int nx = cx + Mdx[i];
				int ny = cy + Mdy[i];
				int nk = ck;

				if (nx < 0 || ny < 0 || nx >= H || ny >= W)continue;

				if (visit[nx][ny][nk] == 0 && map[nx][ny] == 0)
				{
					Q.push({ nx,ny,nk });
					visit[nx][ny][nk] = visit[cx][cy][ck] + 1;
				}
			}
		}

		else
		{
			for (int i = 0; i < 4; i++) //원숭이
			{
				int nx = cx + Mdx[i];
				int ny = cy + Mdy[i];
				int nk = ck;

				if (nx < 0 || ny < 0 || nx >= H || ny >= W)continue;

				if (visit[nx][ny][nk] == 0 && map[nx][ny] == 0)
				{
					Q.push({ nx,ny,nk });
					visit[nx][ny][nk] = visit[cx][cy][ck] + 1;
				}
			}
		}

	}


}
