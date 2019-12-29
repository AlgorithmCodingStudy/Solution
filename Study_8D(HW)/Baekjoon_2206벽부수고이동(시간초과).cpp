/*
벽하나씩부수고 결과값 벡터에저장 (-1아닌값, 양수값만저장)
--> 벡터 비어있으면 도착못한거 ==> -1출력
--> 벡터의 최솟값 출력
*/

#include<iostream>
#include<queue>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;


int N, M;
int MMap[1010][1010] = { 0 };
int map_cpy[1010][1010] = { 0 };
int check[1010][1010] = { 0 };
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
struct info { int x, y; };

queue<info>Wall;
queue<info>Q;
vector<int>result;

void BFS()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		Q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if (nx <= 0 || ny <= 0 || nx > N || ny > M)continue;
			if (check[nx][ny] == 0 && map_cpy[nx][ny] == 0)
			{
				check[nx][ny] = check[cx][cy] + 1;
				Q.push({ nx,ny });
			}
		}
	}


}

int main()
{
	cin >> N >> M;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= M; j++)
		{
			scanf("%1d", &MMap[i][j]);
			if (MMap[i][j] == 1) Wall.push({ i,j });
		}
	}

	while (!Wall.empty())
	{
		int x = Wall.front().x;
		int y = Wall.front().y;
		Wall.pop();

		memcpy(map_cpy, &MMap, sizeof(MMap));
		memset(check, 0, sizeof(check));

		map_cpy[x][y] = 0;
		Q.push({ 1,1 });
		check[1][1] = 1;

		BFS();

		if(check[N][M] > 0)
			result.push_back(check[N][M]);

	}

	if (result.empty())
		printf("%d", -1);
	else
		printf("%d", *min_element(result.begin(), result.end()));

	return 0;	
}
