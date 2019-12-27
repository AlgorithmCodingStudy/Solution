#include<iostream>
#include<queue>
#include<cstring> //memset사용하려고

using namespace std;

struct info { int x; int y; };
int box[1100][1100] = { 0 };
int check[1100][1100] = { 0};
int N, M;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int Count = 0;
queue<info>Q;

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
      if (nx <= -1 || ny <= -1 || nx >= N || ny >= M) continue; //map의 범위 벗어났을 때, 처리 해줘야함!!
			if (box[nx][ny] == 0 && check[nx][ny] == -1)
			{
				check[nx][ny] = check[cx][cy] + 1;
				Q.push({ nx,ny });
			}
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int tomatocnt = 0;
	memset(check, -1, sizeof(check)); //방문체크배열 -1로 초기화 --> 방문하지 않으면 -1

	cin >> M >> N;
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> box[i][j];
			if (box[i][j] == 1) { // 입력받으면서 토마토가 있으면
				tomatocnt++;  // 토마토개수++
				Q.push({ i,j }); // Q에 토마토좌표를 값으로 넣음
				check[i][j] = 0; // 방문처리 (check배열을 초기값-1로 설정해서 0으로해도 방문처리가됨!)
			}
		}
	}

	if (tomatocnt == 0) cout << -1; //초기에 토마토개수가 없으면 -1출력

	else
	{
		BFS();
    
		int MMin = -9999; //초기값
    
    // BFS 후, 탐색을 돌면서 토마토가익을수 있는데 방문하지 않은 점을을 찾거나, 배열의 최댓값(최소걸린수)을 찾음 
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (check[i][j] == -1 && box[i][j] != -1) // 토마토가익을수 있는데 방문하지 않은 점
				{
					cout << -1 << "\n"; // -1출력하고
					return 0;          // main함수를 끝낸다.
				}	
				if (check[i][j] > MMin) // 배열의 최댓값(최소걸린 수) 찾는 조건문
					MMin = check[i][j];
			}
		}
    
		cout << MMin << "\n"; //최소 걸린수 출력
	}
	return 0;
}
