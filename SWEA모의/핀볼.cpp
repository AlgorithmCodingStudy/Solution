#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

struct info { int x, y; };
struct info2 { int x, y, dir; };
int T,N;
int allMMax = -99999999;
int map[110][110];
int dx[] = { 0,-1,0,1,0 };
int dy[] = { 0,0,1,0,-1 };
vector<info>Wormhole[11];
vector<info2>Start;


void playGame(int standx, int standy, int standdir);

int main()
{

	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		allMMax = -99999999;
		memset(map, 0, sizeof(map));
		Start.clear();
		for (int i = 6; i < 11; i++)
		{
			Wormhole[i].clear();
		}

		cin >> N;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				cin >> map[i][j];
				if (map[i][j] >= 6 && map[i][j] <= 10)
				{
					Wormhole[map[i][j]].push_back({ i,j });
				}
				else if (map[i][j] == 0)
				{
					for (int k = 1; k <= 4; k++)
					{
						Start.push_back({ i,j,k });
					}
				}
			}
		}

		
		bool flag = false;
		for (int i = 0; i < Start.size(); i++)
		{
			//cout << "st" << endl;
			playGame(Start[i].x, Start[i].y, Start[i].dir);
			
		}

		cout <<'#'<<q<<' '<<allMMax << endl;

	}
	return 0;
}

void playGame(int standx, int standy, int standdir)
{
	
	 int score = 0;
	 int nx = standx; int ny = standy; int nd = standdir;
	while (1)
	{
		nx += dx[nd];
		ny += dy[nd];
		
		if ((nx == standx && ny == standy) || map[nx][ny] == -1)
		{
			break;
		}

		if (nx < 0 || ny < 0 || nx >= N || ny >= N || map[nx][ny] == 5)
		{
			if (nd == 1)nd = 3;
			else if (nd == 2)nd = 4;
			else if (nd == 3)nd = 1;
			else if (nd == 4)nd = 2;
			score++;
			continue;
		}

		else if (map[nx][ny] == 1)
		{
			if (nd == 1)nd = 3;
			else if (nd == 2)nd = 4;
			else if (nd == 3)nd = 2;
			else if (nd == 4)nd = 1;
			//nx += dx[nd];
			//ny += dy[nd];
			score++;
			continue;
		}
		else if (map[nx][ny] == 2)
		{
			if (nd == 1)nd = 2;
			else if (nd == 2)nd = 4;
			else if (nd == 3)nd = 1;
			else if (nd == 4)nd = 3;
			//nx += dx[nd];
			//ny += dy[nd];
			score++;
			continue;
		}
		else if (map[nx][ny] == 3)
		{
			if (nd == 1)nd = 4;
			else if (nd == 2)nd = 3;
			else if (nd == 3)nd = 1;
			else if (nd == 4)nd = 2;
			//nx += dx[nd];
			//ny += dy[nd];
			score++;
			continue;
		}
		else if (map[nx][ny] == 4)
		{
			if (nd == 1)nd = 3;
			else if (nd == 2)nd = 1;
			else if (nd == 3)nd = 4;
			else if (nd == 4)nd = 2;
			//nx += dx[nd];
			//ny += dy[nd];
			score++;
			continue;
		}
		else if (map[nx][ny] >= 6 && map[nx][ny] <= 10)
		{
			int cidx = map[nx][ny];
			if (Wormhole[cidx][0].x == nx && Wormhole[cidx][0].y == ny)
			{
				nx = Wormhole[cidx][1].x;
				ny = Wormhole[cidx][1].y;
			}
			else
			{
				nx = Wormhole[cidx][0].x;
				ny = Wormhole[cidx][0].y;
			}
			continue;
		}


	}
	
	//cout << score << endl;
	allMMax = max(allMMax,score);
}
