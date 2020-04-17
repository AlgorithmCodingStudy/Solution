#include<iostream>
#include<string>
#include<vector>

using namespace std;

struct info { int x, y; };
int N, M, K;
int result;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
char Map[110][110];
string Final;
vector<info>Start;


void DFS(int x, int y, int cnt);

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
			if (Final[0] == Map[i][j])
			{
				Start.push_back({ i,j });
			}
		}
	}

	for (int i = 0; i < Start.size(); i++) {

		DFS(Start[i].x, Start[i].y, 1);
	}

	cout << result << endl;
	return 0;
}

void DFS(int x, int y, int cnt)
{
	if (cnt == Final.length())
	{
		result++;
		return;
	}

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
			if (Map[nx][ny] == Final[cnt])
			{
				DFS(nx, ny, cnt + 1);
			}
		}
	}
}
