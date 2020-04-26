#include<iostream>
#include<cstring>

using namespace std;

int dx[] = { 0,0,1,1 };
int dy[] = { 0,1,1,0 };
int N;
int Count;
int Map[50][50];

void DFS(int x, int y, int num);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cin >> Map[i][j];
		}
	}
	Map[1][1] = 1;
	Map[1][2] = 1;

	DFS(1, 2, 1); //x,y,num -> num : 1가로 2대각선 3세로

	cout << Count << endl;
	return 0;
}

void DFS(int x, int y, int num)
{
	if (x == N && y == N)
	{
		Count++;
		return;
	}

	if (num == 1)
	{
		int nx = x + dx[1];
		int ny = y + dy[1];
		if (nx >= 1 && ny >= 1 && nx <= N && ny <= N && Map[nx][ny]==0) 
		{
			//Map[nx][ny] = 1;
			DFS(nx, ny, 1);
			//memcpy(Map, cpy, sizeof(cpy));
		}

		nx = x + dx[2];
		ny = y + dy[2];
		if (nx >= 1 && ny >= 1 && nx <= N && ny <= N && Map[nx][ny] == 0 && Map[x+dx[1]][y+dy[1]] == 0&&Map[x + dx[3]][y + dy[3]] == 0)
		{
			//Map[nx][ny] = 1;
			DFS(nx, ny, 2);
			//memcpy(Map, cpy, sizeof(cpy));
		}
		return;
	}
	else if (num == 2)
	{
		int nx = x + dx[1];
		int ny = y + dy[1];
		if (nx >= 1 && ny >= 1 && nx <= N && ny <= N && Map[nx][ny] == 0)
		{
			//Map[nx][ny] = 1;
			DFS(nx, ny, 1);
			//memcpy(Map, cpy, sizeof(cpy));
		}

		nx = x + dx[2];
		ny = y + dy[2];
		if (nx >= 1 && ny >= 1 && nx <= N && ny <= N && Map[nx][ny] == 0 && Map[x + dx[1]][y + dy[1]] == 0 && Map[x + dx[3]][y + dy[3]] == 0)
		{
			//Map[nx][ny] = 1;
			DFS(nx, ny, 2);
			//memcpy(Map, cpy, sizeof(cpy));
		}

		nx = x + dx[3];
		ny = y + dy[3];
		if (nx >= 1 && ny >= 1 && nx <= N && ny <= N && Map[nx][ny] == 0)
		{
			//Map[nx][ny] = 1;
			DFS(nx, ny, 3);
			//memcpy(Map, cpy, sizeof(cpy));
		}
		return;
	}

	else if (num == 3)
	{
		int nx = x + dx[2];
		int ny = y + dy[2];
		if (nx >= 1 && ny >= 1 && nx <= N && ny <= N && Map[nx][ny] == 0 && Map[x + dx[1]][y + dy[1]] == 0 && Map[x + dx[3]][y + dy[3]] == 0)
		{
			//Map[nx][ny] = 1;
			DFS(nx, ny, 2);
			//memcpy(Map, cpy, sizeof(cpy));
		}

		nx = x + dx[3];
		ny = y + dy[3];
		if (nx >= 1 && ny >= 1 && nx <= N && ny <= N && Map[nx][ny] == 0)
		{
			//Map[nx][ny] = 1;
			DFS(nx, ny, 3);
			//memcpy(Map, cpy, sizeof(cpy));
		}
		return;
	}

}
