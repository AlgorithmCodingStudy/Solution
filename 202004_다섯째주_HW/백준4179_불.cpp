//큐는 111222333이런순으로 돈다!

#include<iostream>
#include<vector>
#include<queue>

using namespace std;

struct info { int x, y, cnt; char name; };
int R, C;
char Map[1100][1100];
bool Fire[1100][1100];
bool Jihoon[1100][1100];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int sx, sy;
queue<info>All;

int BFS();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> R >> C;
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			cin >> Map[i][j];
			if (Map[i][j] == 'F') 
			{
				Fire[i][j] = true;
				All.push({ i,j ,0,'F'});
			}
			else if (Map[i][j] == 'J') 
			{
				Map[i][j] = '.';
				sx = i; sy = j; //Fire위치먼저 queue에 넣어주기위해 sx,sy에 
				Jihoon[i][j] = true;
			}
		}
	}

	All.push({ sx,sy,1,'J' });

	int result = BFS();

	if (result == -1)cout << "IMPOSSIBLE";
	else
		cout << result;

	return 0;
}

int BFS()
{
	while (!All.empty())
	{
		int cx = All.front().x;
		int cy = All.front().y;
		int ct = All.front().cnt;
		char cn = All.front().name;
		All.pop();
	

		if (cn == 'F')
		{
			for (int i = 0; i < 4; i++)
			{
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (nx<1 || ny<1 || nx>R || ny>C)continue;
				if (Map[nx][ny] == '.' && !Fire[nx][ny])
				{
					Map[nx][ny] = 'F';
					Fire[nx][ny] = true;
					All.push({ nx,ny,ct,cn });
				}
			}
		}

		else if (cn == 'J')
		{
			if (cx == 1 || cy == 1 || cx == R || cy == C)
			{
				return ct;
			}

			for (int i = 0; i < 4; i++)
			{
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (nx<1 || ny<1 || nx>R  || ny>C)continue;
				if (Map[nx][ny] == '.' && !Jihoon[nx][ny])
				{
					Jihoon[nx][ny] = true;
					All.push({ nx,ny,ct + 1,cn });
				}
			}
		}
	}

	return -1;
}
