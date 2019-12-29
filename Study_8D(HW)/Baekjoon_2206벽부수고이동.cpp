/*
3원체크배열 --> check[][][벽안부숨], check[][][벽부숨] ---> 이해잘안감....이렇게 풀면 왜 빠르지...???????????????????????
시작값 --> 1,1,0
만약에 N,M에도달하면 해당위치의 값을 리턴
큐 끝날때까지 종료위치 도달못하면 -1
*/

#include<iostream>
#include<queue>
#include<cstdio>

using namespace std;


int N, M;
int MMap[1010][1010] = { 0 };
int check[1010][1010][2] = { 0 };
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
struct info { int x, y, broken; }; //broken이 0일경우 벽안부순경우 , 1일경우 부순경우

queue<info>Q;

int BFS()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int broken = Q.front().broken;
		Q.pop();

		if (cx == N && cy == M) //목적지 달성한경우, 현재값을 리턴
			return check[cx][cy][broken];
		
		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			int nbroken = broken + 1;

			if (nx <= 0 || ny <= 0 || nx > N || ny > M)continue;
			if (MMap[nx][ny] == 0) //다음에 벽이 없으면, 벽안부숴도됨
			{
				if (check[nx][ny][broken] == 0)
				{
					Q.push({ nx,ny,broken }); 
					check[nx][ny][broken] = check[cx][cy][broken] + 1;
				}
			}
			if (MMap[nx][ny] == 1) //다음이 벽일경우 벽부숴도되고, 안부숴도됨 
			{
				if (check[nx][ny][broken] == 0 && broken == 0) //벽은 한번부술수있기때문에 이전에 부순경험이 없어야함 , broken==0
				{
					Q.push({ nx,ny,nbroken });
					check[nx][ny][nbroken] = check[cx][cy][broken] + 1;
				}
			}
		}
	}

	return -1; //큐를 다 돌았지만 목적지 달성 못했을경우 
	
}

int main()
{
	cin >> N >> M;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= M; j++)
		{
			scanf("%1d", &MMap[i][j]);
		}
	}
	
	Q.push({ 1,1,0 }); //x:1,y:1,벽안부순경우로 시작 ( 초기 값 )
	check[1][1][0] = 1;

	int result = BFS();

	/*
	for (int k = 0; k < 2; k++) 
  {
		for (int i = 1; i <= N; i++)
		{
			for (int j = 1; j <= M; j++)
			{
				cout << check[i][j][k];
			}
			cout << "\n";
		}
		cout << "\n";
	}*/


	cout << result << "\n";

	return 0;	
}
