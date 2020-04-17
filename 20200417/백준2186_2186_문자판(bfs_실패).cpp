#include<iostream>
#include<queue>
#include<string>

using namespace std;

struct info { int x, y, cnt; };
queue<info>Q;
string Final;
int N, M, K;
int Num;
int Result;
char Map[110][110];
int memo[110][110];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

void writenum(int x,int y,int cnt);
void FindAns();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M >> K;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> Map[i][j];
		}
	}
	cin >> Final;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (Map[i][j] == Final[0])
				Q.push({ i,j,1 });
			else if (Map[i][j] == Final[Final.length()-1])
			{
				Num++;
				writenum(i,j,1);
			}
		}
	}
	//cout << Num << endl;
	FindAns();

	cout << Result << endl;

	return 0;
}

void writenum(int x,int y,int cnt)
{
	int Finalcnt = 0;
	for (int i = 0; i < 4; i++)
	{
		int count = K;
		int nx = x;
		int ny = y;
		while (count--)
		{
			nx += dx[i];
			ny += dy[i];
			if (nx < 0 || ny < 0 || nx >= N || ny >= M)continue;
			if (Map[nx][ny] == Final[Final.length() - 2])
				Finalcnt++;
		}
	}

	memo[x][y] = Finalcnt;
}

void FindAns()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int cnum = Q.front().cnt;
		Q.pop();

		for (int i = 0; i < 4; i++)
		{
			int count = K;
			int nx = cx;
			int ny = cy;

			while (count--)
			{
				nx += dx[i];
				ny += dy[i];
				if (nx < 0 || ny < 0 || nx >= N || ny >= M)continue;
				/*
				if (Map[nx][ny] == Final[Final.length() - 1])
				{
					if (Num > 0) {
						Num--;
						Result += memo[nx][ny];
					}
					else if (Num == 0) return;
				}*/
				if (Map[nx][ny] == Final[cnum])
				{
					if (cnum == Final.length() - 1 && Num > 0)
					{
						Num--;
						Result+=memo[nx][ny];
					}
					else {
						Q.push({ nx,ny,cnum + 1 });
					}
				}
				if (Num == 0)return;
			}
		}
	}
}
