#include<iostream>
#include<cstring>

using namespace std;

int T,M,N,K; //M:열 N:행
int Ground[55][55] = { 0 };
bool check[55][55] = {false};
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

void DFS(int x, int y)
{
	for (int i = 0; i < 4; i++) //4방향체크
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || ny < 0 || nx >= N || ny >= M)continue; //범위벗어나는지 체크
		if (Ground[nx][ny] == 1 && check[nx][ny] == false) //배추가 있고 방문안했으면
		{
			check[nx][ny] = true;
			DFS(nx, ny);
		}
	}
}

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		M = 0;  N = 0;  K = 0;

		cin >> M >> N >> K; //열,행 순서로 입력받음

		memset(Ground, 0, sizeof(Ground)); //초기와 반드시! testcase가 여러개이므로
		memset(check, false, sizeof(check));

		for (int i = 0; i < K; i++)
		{
			int a = 0; int b = 0;
			cin >> b >> a;     //좌표를 잘봐야함!! 입력을 1,0로주고 map에는 (열,행)으로 표시됨
			Ground[a][b] = 1;  //배추위치
		}

		int cnt = 0;

    //DFS_all
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (Ground[i][j] == 1 && check[i][j] == false)  //배추가있고, 방문안했으면
        {	
					check[i][j] = true; //방문체크
					DFS(i, j); //DFS
					cnt++; //배추가 모여있는 구역수 세기
				}	
			}
		}
		cout<<cnt<<"\n";
	}

	return 0;
}
