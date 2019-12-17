## 실패 == > 인접행렬은 네방향탐색하면 안됨! (부당한방법!ㅋㅋㅋ)

### EX)

   <img width="417" alt="캡처" src="https://user-images.githubusercontent.com/29946480/70970546-f3e7b300-20e1-11ea-9adb-18005622cc1e.PNG">

			   
			   
			   
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

# 성공

```c
#include <string>
#include <vector>
 
using namespace std;
int visit[200] = {false};
int N = 0;
 
void DFS(int start, vector<vector<int>> tmp){
    if(visit[start]){
        return;
    }
    visit[start] = true;
    
    for(int i = 0; i<tmp[start].size(); i++){
        if(tmp[start][i]){
            DFS(i,tmp);   
        }
    }
}
 
int solution(int n, vector<vector<int>> computers) {
    int answer;
    for(int j = 0; j < n; j++){
        if(!visit[j]){
            DFS(j,computers);
            answer++;
        }
        
    }   
    
    return answer;
}

```

### 알고리즘문제해결전략 dfs책보고
```c
#include <string>
#include <vector>
#include <iostream>

using namespace std;
bool visit[200] = { false };

void DFS(int now, vector<vector<int>> computers) {
	
	if (visit[now])
	{
		return;
	}
	visit[now] = true;

	for (int i = 0; i < computers[now].size(); i++)
	{
		int next = computers[now][i];
		if (next == 0)continue;
		DFS(i, computers);
	}
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;
	for (int i = 0; i < computers.size(); i++)
	{
		if (visit[i])continue;
		DFS(i, computers);
		answer++;
	}
	return answer;
}

```
