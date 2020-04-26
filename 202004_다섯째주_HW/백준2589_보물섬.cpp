//얼떨결에 맞음 왜 BFS?

#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstring>

using namespace std;

struct info { int x, y, cnt; };
struct info2 { int sx, sy,fx,fy,cnt;
bool operator<(const info2& a)
{
	return cnt > a.cnt;
}
};
int N, M;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
char Map[55][55];
bool Region[55][55];
vector<info>Start;
vector<info2>Big;
queue<info>Q;

void BFS(int startx, int starty);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> Map[i][j];
			if (Map[i][j] == 'L')
				Start.push_back({ i,j,0 });
		}
	}

	for (int i = 0; i < Start.size(); i++)
	{
		BFS(Start[i].x, Start[i].y);
		memset(Region, false, sizeof(Region));
	}
	
	sort(Big.begin(), Big.end());

	int mmax = Big[0].cnt;
	cout << mmax << endl;

	return 0;
}

void BFS(int startx, int starty)
{
	Q.push({ startx,starty,0 });
	Region[startx][starty] = true;

	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int ct = Q.front().cnt;
		Q.pop();

		bool check = false;
		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= M)continue;
			if (Map[nx][ny] == 'L' && !Region[nx][ny])
			{
				check = true;
				Region[nx][ny] = true;
				Q.push({ nx,ny,ct + 1 });
			}
		}

		if (check)continue;
		Big.push_back({ startx,starty,cx,cy,ct });
	}
	return;

}
