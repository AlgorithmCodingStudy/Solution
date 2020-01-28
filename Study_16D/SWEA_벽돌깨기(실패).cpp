/*

<< 런타임에러(메모리초과)+시간초과 >>

1. 메모리초과랑 시간초과는 이차원배열을 3개쓰려해서 초과난듯..
         +
2. 106번째부터 같은 숫자 돌고있음 

*/

#include<iostream>
#include<cstring>
#include<algorithm>
#include<queue>

using namespace std;

int T,N,W,H;
int MMin = 999999999;
int map[20][15];
int map2[20][15];
int sel_num[10];
bool check[20][15];
int mapcpy[20][15];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
queue<int>temp[15];
struct info { int x, y, num; };

void copy(int a[20][15], int b[20][15]);
void Broken(int idx);
void DFS(int select);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		//초기화
		memset(map, 0, sizeof(map));
		memset(map2, 0, sizeof(map2));
		memset(sel_num, 0, sizeof(sel_num));
		MMin = 999999999;

		cin >> N >> W >> H;

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				cin >> map[i][j];
			}
		}

		DFS(0);


		cout << '#' << q << ' ' << MMin << "\n";
	}

	return 0;
}

void copy(int a[20][15], int b[20][15])
{
	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < W; j++)
		{
			a[i][j] = b[i][j];
		}
	}
}

void Broken(int idx)
{
	queue<info>Q;
	memset(check, false, sizeof(check));
	memset(mapcpy, 0, sizeof(mapcpy));

	copy(mapcpy, map2);

	//부수기
	for (int i = 0; i < H; i++)
	{
		if (mapcpy[i][idx] > 0)
		{
			Q.push({ i,idx,mapcpy[i][idx] });
			break;
		}
	}
	
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int cn = Q.front().num - 1;
		check[cx][cy] = true;
		mapcpy[cx][cy] = 0;
		Q.pop();

		if (cn == 0)continue;

		for (int i = 0; i < cn; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int nx = cx + dx[j];
				int ny = cy + dy[j];

				if (nx < 0 || ny < 0 || nx >= H || ny >= W)continue;

				if (check[nx][ny] == false && mapcpy[nx][ny] > 0)
					Q.push({ nx,ny,mapcpy[nx][ny] });
			}
		}

	}


	//빈칸없애기
	for (int i = 0; i < W; i++)
	{
		for (int j = H - 1; j >= 0; j--)
		{
			if (mapcpy[j][i] != 0)
			{
				temp[i].push(mapcpy[j][i]);
			}
		}
	}

	for (int i = 0; i < W; i++)
	{
		int S = H - 1;
		while (!temp[i].empty())
		{
			int a = temp[i].front();
			temp[i].pop();
			map2[S][i] = a;
			S--;
		}
	}
}


void DFS(int select)
{
	if (select == N)
	{ 
		//벽돌부수기
		copy(map2, map);

		for (int i = 0; i < N; i++)
		{
			Broken(sel_num[i]);
		}

		//map2의 벽돌갯수세기
		int cnt = 0;
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				if (map2[i][j] > 0) cnt++;
			}
		}

		MMin = min(MMin, cnt);

		return;
	}

	for (int i = 0; i < W; i++)
	{
		sel_num[select] = i;
		DFS(select + 1);
	}
}
