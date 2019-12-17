/*
 지훈이가 불에타기전에 탈출할수 있는지, 탈출시간이 얼마인지

 1. 불은 네방향으로 확산 
 2. 지훈이는 가장자리에 접하면 탈출가능
 3. 지훈이와 불은 벽을만나면 통과못함
 4. 지훈이 통과못하면 ==> IMPOSSIBLE출력
 5. 지훈이 통과하면 ==> 가장빠른탈출시간

 R:행 / C:열 / #:벽 / .:지나갈수있음 / J : 지훈 / F :불


 1. 불과 지훈이의 이동이 동시에 (queue두개)
 2. 가장자리가 벽이아닐경우 지훈이 통과  ==>  .이고 가장자리일경우

*/

#include<iostream>
#include<queue>

using namespace std;


int R, C;
char map[1001][1001];
bool visitJ[1001][1001] = { false };


int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int jx, jy, fx, fy;
struct dirJ { int jx, jy, cnt; };
struct dirF { int fx, fy; };
queue<dirJ>J;
queue<dirF>F;

void input();
bool can(int jx, int jy);

int BFS()
{
	while (!J.empty())
	{
		int jx = J.front().jx;
		int jy = J.front().jy;
		int cnt = J.front().cnt;
		int fx = F.front().fx;
		int fy = F.front().fy;

		J.pop();
		F.pop();
		
		if (map[jx][jy] == '.')
		{
			if (can(jx, jy))
			{
				return cnt;
			}
		}

		for (int i = 0; i < 4; i++)
		{
			
			int nfx = fx + dx[i];
			int nfy = fy + dy[i];

			if (nfx < 0 || nfy < 0 || nfx >= R || nfy >= C)continue;
			if (map[nfx][nfy] == '.')
			{
				map[nfx][nfy] = 'F';
				F.push({ nfx,nfy });
			}
		}
		for (int i = 0; i < 4; i++)
		{

			int njx = jx + dx[i];
			int njy = jy + dy[i];

			if (njx < 0 || njy < 0 || njx >= R || njy >= C)continue;
			if (map[njx][njy] == '.' && visitJ[njx][njy] == false)
			{
				visitJ[njx][njy] = true;
				J.push({ njx,njy });
			}
		}
	}

	return -1;

}


int main()
{
	input();
	int ans = BFS();
	cout << ans << endl;
	if (ans > 0)
		cout << ans;
	else
		cout << "IMPOSSIBLE";


	return 0;
}


bool can(int jx, int jy)
{
	if (jx == 0 || jx == R)
	{
		return true;
	}
	if (jy == 0 || jy == C)
	{
		return true;
	}
	return false;
}

void input()
{
	cin >> R >> C;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == 'J')
			{
				jx = i; jy = j;
				map[i][j] = '.';
			}
			if (map[i][j] == 'F')
			{
				fx = i; fy = j;
			}
		}
	}
}
