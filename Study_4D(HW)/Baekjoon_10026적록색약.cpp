#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

//적록색약은 빨강 == 초록 (같은구역)
//N*N배열
//R,G,B중 구역의 색
//DFS=> map을 돌면서 체크안한곳 방문 -> 이어지는곳 탐색

int N;
char map[110][110] = { 0 };
bool check[110][110] = { 0 };
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
bool second = false; //정상과 적록색약 dfs돌릴때 구분해주기 위해
vector<int>result;

void input();
void Find();

int main()
{
	input();
	Find(); //정상인사람 dfs
	Find(); //적록색약 dfs

	for (int i = 0; i < 2; i++)
	{
		cout << result[i] << " ";
	}

	return 0;
}

void DFS(int curx,int cury, char now)
{
	for (int i = 0; i < 4; i++) {

		int nx = curx + dx[i];
		int ny = cury + dy[i];

		if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
		
		if (second == false)  // 정상인사람 dfs
		{
			if (check[nx][ny] == false && now == map[nx][ny]) //방문한적 없고, 다음구역이 같은색이면
			{
				check[nx][ny] = true;
				DFS(nx, ny, map[nx][ny]);
			}
		}
		
		if (second == true) //적록색약인사람 dfs
		{
			if (check[nx][ny] == false) //방문한적 없고,
			{
				if (now == 'R' && (map[nx][ny] == 'G' || map[nx][ny] == 'R')) { //현재구역이 R일때, 다음구역이 G나 R이면
					check[nx][ny] = true;  //방문체크 후,
					DFS(nx, ny, map[nx][ny]); //DFS
				}
				if (now == 'G' && (map[nx][ny] == 'G' || map[nx][ny] == 'R')) { //현재구역이 G일때, 다음구역이 G나 R이면
					check[nx][ny] = true;   //방문체크 후,
					DFS(nx, ny, map[nx][ny]); //DFS
				}
				if (now == 'B' && map[nx][ny] == 'B') { //현재구역이 B일때, 다음구역이 B이면
					check[nx][ny] = true;   //방문체크 후,
					DFS(nx, ny, map[nx][ny]); //DFS
				}
			}
		}
	}
}
void input()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> map[i][j];
		}
	}
}

void Find()
{
	int cnt = 0;
	memset(check, 0, sizeof(check)); //check배열 초기화
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (check[i][j] == 0) { //방문한적 없으면 dfs
				
				DFS(i, j, map[i][j]);
				cnt++;
			}
		}
	}

	result.push_back(cnt);
	second = true; //적록색약일때의 dfs돌리기 위해
}
