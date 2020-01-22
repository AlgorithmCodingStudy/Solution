#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;

int N, M;
int industry[10][10];
int copy_industry[10][10];
struct info { int x, y; };
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
queue<info>Q;
vector<int>result;

void virus();
void safety();

void DFS(int x, int y, int wall)
{
	if (wall == 3)
	{
		virus(); //바이러스 퍼트림
		safety(); //안전영역구함
		return;
	}

	for (int i = x; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (industry[i][j] == 0 && wall < 3)
			{
				industry[i][j] = 1;
				DFS(i, j, wall + 1);
				industry[i][j] = 0;
			}
		}
	}

}
int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin>>N>>M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin>>industry[i][j];
		}
	}


	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (industry[i][j] == 0)
			{
				DFS(i, j, 0);
			}
		}
	}

	int R = *max_element(result.begin(), result.end());
	cout<<R;

	return 0;
}

void virus()
{
	bool check[10][10] = {false,};
	memcpy(&copy_industry, &industry, sizeof(industry));

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (industry[i][j] == 2)
			{
				Q.push({ i,j });
				check[i][j] = true;
			}
		}
	}

	while (!Q.empty())
	{
		int curx = Q.front().x;
		int cury = Q.front().y;
		Q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = curx + dx[i];
			int ny = cury + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= M)continue;
			if (industry[nx][ny] == 0 && check[nx][ny] == false)
			{
				Q.push({ nx,ny });
				check[nx][ny] = true;
				copy_industry[nx][ny] = 2;
			}
		}
	}
}

void safety()
{
	int cnt = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (copy_industry[i][j] == 0)
			{
				cnt++;
			}
		}
	}
	result.push_back(cnt);
}
