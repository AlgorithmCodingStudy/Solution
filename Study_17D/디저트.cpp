// 마름모모양만 체크하기! (4방향검사안해도됨) --> 고치기

#include<iostream>
#include<cstring>
#include<vector>

using namespace std;


int T;
int N;
int map[25][25];
int dx[] = { 1,1,-1,-1 };
int dy[] = { 1,-1,-1,1 };
int sx, sy;
vector<int>V;
int MMax;
int MMnum;

void DFS(int x, int y);
bool visit[25][25];

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		N = 0; MMnum = -9999; MMax = -999999; 
		memset(map, 0, sizeof(map));
		cin >> N;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				cin >> map[i][j];
			}
		}

		for (int i = 0; i < N-2; i++) {

			for (int j = 1; j < N - 1; j++)
			{
				V.clear();
				memset(visit, false, sizeof(visit));
				sx = i, sy = j;

				//visit[i][j] = true;
				V.push_back(map[i][j]);
				DFS(i, j); //시작점
			}
		}
		if (MMnum == -9999)
			cout <<'#'<<q<<' '<< -1 << endl;
		else
			cout <<'#'<<q<<' '<< MMnum << endl;

	}
	return 0;
}
void DFS(int x, int y)
{
	
	for (int i = 0; i < 4; i++)
	{
		bool can = false;
		
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx == sx && ny == sy)
		{
			if (V.size() < 4)continue;

			int hap = 0;
			for (int i = 0; i < V.size(); i++)
			{
				hap += V[i];
			}
			
			if (hap > MMax) {
				MMax = hap;
				MMnum = V.size();
			}

			return;
		}

		if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;


		for (int j = 0; j < V.size(); j++)
		{
			//cout << V[j] <<" ";
			if (V[j] == map[nx][ny]) {
				can = true;
				break;
			}
		}
		//cout << endl;
		if (can == true)continue;

		if (visit[nx][ny] == false)
		{
			visit[nx][ny] = true;
			V.push_back(map[nx][ny]);
			DFS(nx, ny);
			visit[nx][ny] = false;
			V.pop_back();
		}

	}

	return;

}
