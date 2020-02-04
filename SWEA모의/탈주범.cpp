#include<iostream>
#include<vector>
#include<cstring>
#include<queue>

using namespace std;

struct info { int x, y; };
int dx[] = { -1,0,1,0 };
int dy[] = { 0,1,0,-1 };
int T, N, M, R, C, L;
int initmap[55][55];
bool check[55][55];

vector<info>Cmap[55][55];
queue<pair<info, int>>Q;

void BFS();
bool can(int nx, int ny, int cx, int cy);
void connect(int x, int y, int num);

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		//초기화
		N = 0, M = 0, R = 0, C = 0, L = 0;
		memset(check, false, sizeof(check));
		memset(initmap, 0, sizeof(initmap));
		//입력
		cin >> N >> M >> R >> C >> L;

		
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				cin >> initmap[i][j];
			}
		}

		//map값구하기
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (initmap[i][j] <= 0)continue;
				if (initmap[i][j] == 1)
				{
					for (int k = 0; k < 4; k++)
						connect(i, j, k);
				}
				else if (initmap[i][j] == 2)
				{
					connect(i, j, 0);
					connect(i, j, 2);
				}
				else if (initmap[i][j] == 3)
				{
					connect(i, j, 1);
					connect(i, j, 3);
				}
				else if (initmap[i][j] == 4)
				{
					connect(i, j, 0);
					connect(i, j, 1);
				}
				else if (initmap[i][j] == 5)
				{
					connect(i, j, 1);
					connect(i, j, 2);
				}
				else if (initmap[i][j] == 6)
				{
					connect(i, j, 2);
					connect(i, j, 3);
				}
				else if (initmap[i][j] == 7)
				{
					connect(i, j, 0);
					connect(i, j, 3);
				}
			}
		}

		while (!Q.empty())
		{
			Q.pop();
		}

		//시간에따른 장소
		check[R][C] = true;
		Q.push({ {R,C},1 });
		BFS();

		
		int result = 0;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				//cout << check[i][j];
				if (check[i][j] == true) {
					result++;
				}
			}
			//cout << endl;
		}

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				Cmap[i][j].clear();
			}
		}
		
		cout << '#' << q << ' ' << result << "\n";
	}

	return 0;
}

bool can(int nx, int ny, int cx, int cy)
{
	bool one = false;
	bool two = false;

	for (int i = 0; i < Cmap[nx][ny].size(); i++)
	{
		if (Cmap[nx][ny][i].x == cx && Cmap[nx][ny][i].y == cy) {
			one = true;
			break;
		}
	}
	for (int i = 0; i < Cmap[cx][cy].size(); i++)
	{
		if (Cmap[cx][cy][i].x == nx && Cmap[cx][cy][i].y == ny) {
			two = true;
			break;
		}
	}

	if (one&&two) return true;

	return false;
}

void connect(int x, int y, int num)
{
	int nx = x + dx[num];
	int ny = y + dy[num];

	Cmap[x][y].push_back({ nx,ny });
}


void BFS()
{
	while (!Q.empty())
	{
		int cx = Q.front().first.x;
		int cy = Q.front().first.y;
		int time = Q.front().second;
		//cout << "cx"<<cx <<"cy"<< cy <<"t"<< time << endl;
		Q.pop();

		if (time == L) return;

		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= M)continue;
			if (check[nx][ny] == false && initmap[nx][ny] > 0)
			{
				if (can(nx, ny, cx, cy))
				{
					check[nx][ny] = true;
					Q.push({ {nx,ny},time + 1 });
				}
			}
		}

	}
}
