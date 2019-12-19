#include<iostream>
#include<queue>

using namespace std;

int R, C; //행,열
char map[1010][1010];
bool checkJH[1010][1010] = { false }; //지훈이 방문체크
bool checkF[1010][1010] = { false }; //불 방문체크
int startx, starty; //지훈이 초기위치
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
struct info { int x, y, move; string name; }; //x,y,움직인수, 지훈인지 불인지

queue<info>Q;

void input();
int BFS();

int main()
{
	input(); //입력

	int result = BFS(); //결과 값
  
	if (result == -1000) //결과가 -1000이면 지훈이 탈출실패
		cout << "IMPOSSIBLE";
	
	else
		cout << result << endl;


	return 0;
}

void input() //입력받으면서 지훈이, 불의 위치 큐에 넣어줌! (불이 먼저 움직여야함)
{
	cin >> R >> C;
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == 'J')
			{
				startx = i; starty = j; //지훈이위치는 startx,starty에 저장해 놨다가 BFS함수 시작하고 큐에 넣어줌
				checkJH[i][j] = true;
				map[i][j] = '.';
			}
			if (map[i][j] == 'F')
			{
				checkF[i][j] = true;
				Q.push({ i,j,0,"F" }); //불은 큐에 넣어줌
			}
		}
	}
}

int BFS()
{
	Q.push({ startx,starty,0,"JH" }); //지훈이 위치 큐에 넣어주고 시작 

	while (!Q.empty())
	{
		int cx = Q.front().x; //x값
		int cy = Q.front().y; //y값
		int cm = Q.front().move; //움직인 시간
		string cn = Q.front().name; //지훈인지 불인지 구분
		Q.pop();

		if (cn == "F") { //큐에서 뺀 정보가 불 일때,

			for (int i = 0; i < 4; i++)
			{
				int fnx = cx + dx[i];
				int fny = cy + dy[i];

				if (fnx <= 0 || fny <= 0 || fnx > R || fny > C)continue; //map사이즈 벗어나면 패스
				if (checkF[fnx][fny] == false && map[fnx][fny] == '.') //다음위치에 불이 간적이 없고, 벽이 아니면
				{
					checkF[fnx][fny] = true; 
					map[fnx][fny] = 'F'; //map에 불표시해줌(지훈이가 움직일때, 불을 피하기위해서)
					Q.push({ fnx,fny,cm,"F" }); //조건만족하면 큐에 넣어줌
				}
			}
		}

		if (cn == "JH") { //큐에서 뺀 정보가 지훈이 일때,

			if (cx == 1 || cy == 1 || cx == R || cy == C) //현재 위치가 map의 경계이면 지훈이가 탈출성공
			{
				return cm + 1; //현재 움직인 시간에서 map범위 밖으로 나가는 시간1초 더해줌
			}

			for (int i = 0; i < 4; i++)
			{
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				int nm = cm + 1; //지훈이 움직인 시간+1

				if (nx <= 0 || ny <= 0 || nx > R || ny > C)continue;
				if (checkJH[nx][ny] == false && map[nx][ny] == '.')
				{
					checkJH[nx][ny] = true;
					Q.push({ nx,ny,nm,"JH" });
				}
			}
		}
	}
	return -1000; //큐가 빌때까지 돌았는데 리턴하지 못했으면 ==> 지훈이 탈출 실패 ==> -1000 리턴
}
