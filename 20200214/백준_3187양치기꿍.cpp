#include<iostream>

using namespace std;

int R, C;
char Map[300][300];
bool check[300][300];
int V, K;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

void DFS(int sx, int sy);

int main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> R >> C;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> Map[i][j];
		}
	}

	//배열전체돌면서 dfs영역구함
	int totalV=0, totalK=0;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (check[i][j] == true)continue;
			if (Map[i][j] != '#')
			{
				V = 0; K = 0;
				check[i][j] = true;
				if (Map[i][j] == 'v') V++;
				else if (Map[i][j] == 'k')K++;
				DFS(i,j);
				if (K > V)V = 0;
				else if (K <= V)K = 0;
				totalK += K;
				totalV += V;
			}
		}
	}

	cout << totalK << " "<<totalV << endl;

	return 0;
}

void DFS(int sx,int sy)
{
	for (int i = 0; i < 4; i++)
	{
		int nx = sx + dx[i];
		int ny = sy + dy[i];

		if (nx < 0 || ny < 0 || nx >= R || ny >= C)continue;
		if (Map[nx][ny] != '#' && check[nx][ny] == false)
		{
			check[nx][ny] = true;
			if (Map[nx][ny] == 'v')V++;
			else if (Map[nx][ny] == 'k')K++;
			DFS(nx, ny);
		}
	}

}
