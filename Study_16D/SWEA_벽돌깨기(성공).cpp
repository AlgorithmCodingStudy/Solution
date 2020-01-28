/* 
  이차원배열 두개로 복사하니까 성공!
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

int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
queue<int>temp[15];
struct info { int x, y, num; };
queue<info>Q;

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
	bool check[20][15] = {false};
	//부수기
	for (int i = 0; i < H; i++)
	{
		if (map2[i][idx] == 1) {
			map2[i][idx] = 0;
			break;
		}
		else if (map2[i][idx] > 1)
		{
			check[i][idx] = true;
			Q.push({ i,idx,map2[i][idx] });
			break;
		}
	}
	
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int cn = Q.front().num - 1;
		
		map2[cx][cy] = 0;
		Q.pop();

		if (cn == 0)continue;

		for (int j = 0; j < 4; j++)
		{
			int nx = cx;
			int ny = cy;

			for (int i = 0; i < cn; i++)
			{
				nx += dx[j];
				ny += dy[j];

				if (nx < 0 || ny < 0 || nx >= H || ny >= W)continue;

				if (check[nx][ny] == false &&map2[nx][ny] >= 1 ) {

					if (map2[nx][ny] == 1)
						map2[nx][ny] = 0;
					Q.push({ nx,ny,map2[nx][ny] });
					check[nx][ny] = true;
				}
			}
		}

	}


	//빈칸없애기 (내생각)
	for (int i = 0; i < W; i++)
	{
		for (int j = H - 1; j >= 0; j--)
		{
			if (map2[j][i] != 0)
			{
				temp[i].push(map2[j][i]);
			}
		}
	}
	memset(map2, 0, sizeof(map2));
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
  
  /* (다른사람 아이디어)
  
   for (int i = 0; i < W; i++) {
		int sx = H - 1;
		for (int j = H - 1; j >= 0; j--) {
			if (map2[j][i] != 0) {
				int temp = map2[j][i];
				map2[j][i] = 0;
				map2[sx][i] = temp;
				sx--;
			}
		}
    
  */
	
  
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
