```c
#include <string>
#include <vector>
#include<iostream>

using namespace std;
int visit[210][210] = { 0 };
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

void DFS(int x, int y, int n, vector<vector<int>> computers)
{
    visit[x][y] = 1;
    
	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= n)continue;
		if (computers[nx][ny] == 1 && visit[nx][ny] == 0)
		{
			DFS(nx, ny, n, computers);
		}
	}

}

int solution(int n, vector<vector<int>> computers) {
    
	int answer = 0;
  
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
            if(computers[i][j] == 0)continue;
			if (visit[i][j] == 0)
			{
				//visit[i][j] = 1;
				DFS(i, j, n, computers);
				answer++;
			}
		}
	}
    
    
	return answer;
}
```
