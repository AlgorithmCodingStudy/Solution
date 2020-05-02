#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;

int dx[] = { 0,-1,0,1 };
int dy[] = { -1,0,1,0 };
struct info { int x, y, dir; };
vector<info>Wall; //벽의 정보저장
vector<int> Map[110][110]; //각 위치별로 갈수있는 방향정보 저장
int M, N;
bool check[110][110];
bool visit[110][110];
int BigRoom = -1;
int BigNewRoom = -1;

void DFS2(int x, int y);
void Save_Wall(int x, int y, int Num);
void DFS(int x, int y);
int Count();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			int a; 
			cin >> a;
			Save_Wall(i,j,a);
		}
	}

	int AllRoom = 0;
	for(int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (!check[i][j])
			{
				memset(visit, false, sizeof(visit));
				check[i][j] = true;
				visit[i][j] = true;
				DFS(i, j);
				AllRoom++;
				int result = Count();
				BigRoom = max(BigRoom, result);
			}
		}
	}

	
	for (int i = 0; i < Wall.size(); i++)
	{
		memset(visit, false, sizeof(visit));
		int cx = Wall[i].x;
		int cy = Wall[i].y;
		int wall = Wall[i].dir;
		
		Map[cx][cy].push_back(wall);
		DFS2(cx,cy);
		int result = Count();
		BigNewRoom = max(BigNewRoom, result);
		Map[cx][cy].pop_back();
	}
	
	cout << AllRoom << "\n";
	cout << BigRoom << "\n";
	cout << BigNewRoom << "\n";
	//cout << AllRoom << " " << BigRoom << endl;

	return 0;
}


void Save_Wall(int x, int y, int Num)
{
	if (Num == 1)
	{
		Wall.push_back({ x,y,0 });
		Map[x][y].push_back(1);
		Map[x][y].push_back(2);
		Map[x][y].push_back(3);
	}
	else if (Num == 2)
	{
		Wall.push_back({ x,y,1 });
		Map[x][y].push_back(0);
		Map[x][y].push_back(2);
		Map[x][y].push_back(3);
	}
	else if (Num == 4)
	{
		Wall.push_back({ x,y,2 });
		Map[x][y].push_back(0);
		Map[x][y].push_back(1);
		Map[x][y].push_back(3);
	}
	else if (Num == 8)
	{
		Wall.push_back({ x,y,3 });
		Map[x][y].push_back(0);
		Map[x][y].push_back(1);
		Map[x][y].push_back(2);
	}
	else if (Num == 3)
	{
		Wall.push_back({ x,y,0 });
		Wall.push_back({ x,y,1 });
		Map[x][y].push_back(2);
		Map[x][y].push_back(3);
	}
	else if (Num == 6)
	{
		Wall.push_back({ x,y,1 });
		Wall.push_back({ x,y,2 });
		Map[x][y].push_back(0);
		Map[x][y].push_back(3);
	}
	else if (Num == 12)
	{
		Wall.push_back({ x,y,2 });
		Wall.push_back({ x,y,3 });
		Map[x][y].push_back(0);
		Map[x][y].push_back(1);
	}
	else if (Num == 9)
	{
		Wall.push_back({ x,y,0 });
		Wall.push_back({ x,y,3 });
		Map[x][y].push_back(1);
		Map[x][y].push_back(2);
	}
	else if (Num == 10)
	{
		Wall.push_back({ x,y,1 });
		Wall.push_back({ x,y,3 });
		Map[x][y].push_back(0);
		Map[x][y].push_back(2);
	}
	else if (Num == 5)
	{
		Wall.push_back({ x,y,0 });
		Wall.push_back({ x,y,2 });
		Map[x][y].push_back(1);
		Map[x][y].push_back(3);
	}
	else if (Num == 7)
	{
		Wall.push_back({ x,y,0 });
		Wall.push_back({ x,y,1 });
		Wall.push_back({ x,y,2 });
		Map[x][y].push_back(3);
	}
	else if (Num == 14)
	{
		Wall.push_back({ x,y,1 });
		Wall.push_back({ x,y,2 });
		Wall.push_back({ x,y,3 });
		Map[x][y].push_back(0);
	}
	else if (Num == 13)
	{
		Wall.push_back({ x,y,0 });
		Wall.push_back({ x,y,2 });
		Wall.push_back({ x,y,3 });
		Map[x][y].push_back(1);
	}
	else if (Num == 11)
	{
		Wall.push_back({ x,y,0 });
		Wall.push_back({ x,y,1 });
		Wall.push_back({ x,y,3 });
		Map[x][y].push_back(2);
	}
	else if (Num == 15)
	{
		Wall.push_back({ x,y,3 });
		Wall.push_back({ x,y,1 });
		Wall.push_back({ x,y,2 });
		Wall.push_back({ x,y,0 });
	}
}

void DFS(int x, int y)
{
	if (Map[x][y].empty())return;
	for (int i = 0; i < Map[x][y].size(); i++)
	{
		int nx = x + dx[Map[x][y][i]];
		int ny = y + dy[Map[x][y][i]];

		if (nx < 0 || ny < 0 || nx >= M || ny >= N)continue;
		if (!check[nx][ny] && !visit[nx][ny])
		{
			visit[nx][ny] = true;
			check[nx][ny] = true;
			DFS(nx, ny);
		}
		else if (check[nx][ny] && !visit[nx][ny])
		{
			visit[nx][ny] = true;
			DFS(nx, ny);
		}
	}
}


void DFS2(int x, int y)
{
	visit[x][y] = true;

	if (Map[x][y].empty())return;
	for (int i = 0; i < Map[x][y].size(); i++)
	{
		int nx = x + dx[Map[x][y][i]];
		int ny = y + dy[Map[x][y][i]];

		if (nx < 0 || ny < 0 || nx >= M || ny >= N)continue;
		if (!visit[nx][ny])
		{
			visit[nx][ny] = true;
			DFS2(nx, ny);
		}
	}

	return;
}


int Count()
{
	int hap = 0;
	
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (visit[i][j])hap++;
		}
	}

	return hap;

}

