/*
 * : 벽 (빛통과x)
 ! : 거울 ==> 45도
 . : 아무것도 없음 ( 빛통과o)
 # : 문(2개)
 N : 집크기(1~50)

 - 거울만날때마다 +90회전, -90회전
 - 입력받을때 처음 #의 위치 저장 후, '.'로 초기화 -> 마지막 나갈때 문만 map에 남음
 - 북 : 동서 / 남 : 동서 / 동: 북남 / 서 : 북남
 - 거울설치하면 +90, -90 / 거울설치 안하면 현재방향유지
 */

#include<iostream>
#include<cstring>
#include<queue>

using namespace std;

int N;
char map[51][51];
int wall[51][51] = { 0 };
int endx, endy;
int dx[] = {0,0,1,-1};
int dy[] = { 1,-1,0,0 };
struct info { int x, y, dir; char a; };
queue<info>Q;

void input();
void BFS();


int main()
{
	input();
	BFS();
	return 0;
}

void input()
{
	cin >> N;
	int startx, starty = 0;
	int cnt = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == '#' && cnt == 0)
			{
				cnt++; 
				map[i][j] = '.';
			}
		}
	}
	memset(wall, -1, sizeof(wall));
	wall[startx][starty] = 0;

	for (int i = 0; i < 4; i++)
	{
		int nx = startx + dx[i];
		int ny = starty + dy[i];

		if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
		if (map[nx][ny] != '*') //다음위치방향이 벽이아닐경우 초기값 큐에 넣어줌
		{
			Q.push({ startx,starty,i,map[nx][ny]});
		}
	}
}


void BFS()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int dir = Q.front().dir;

		Q.pop();

		if (map[cx][cy] == '#')
		{
			endx = cx; endy = cy;
			return;
		}

		if (map[cx][cy] == '!')
		{
			if (dir == 0 || dir == 1)
			{
				for (int i = 2; i <= 3; i++)
				{
					int nx = cx + dx[i];
					int ny = cy + dy[i];
					int nd = i;
					if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
					if (map[nx][ny] == '!' && wall[nx][ny] == -1)
					{
						wall[nx][ny] = wall[cx][cy];
						Q.push({ nx,ny,nd,map[nx][ny] });
					}
					if (map[nx][ny] == '.' && wall[nx][ny] == -1)
					{
						wall[nx][ny] = wall[cx][cy] + 1;
						Q.push({ nx,ny,nd,map[nx][ny] });
					}
				}
			}
			if (dir == 2 || dir == 3)
			{
				for (int i = 0; i <= 1; i++)
				{
					int nx = cx + dx[i];
					int ny = cy + dy[i];
					int nd = i;
					if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
					if (map[nx][ny] == '!' && wall[nx][ny] == -1)
					{
						wall[nx][ny] = wall[cx][cy];
						Q.push({ nx,ny,nd,map[nx][ny] });
					}
					if (map[nx][ny] == '.' && wall[nx][ny] == -1)
					{
						wall[nx][ny] = wall[cx][cy] + 1;
						Q.push({ nx,ny,nd,map[nx][ny] });
					}
				}
			}
		}

		if (map[cx][cy] == '.')
		{
			int nx = cx + dx[dir];
			int ny = cy + dy[dir];
			int nd = dir;

			if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
			if (map[nx][ny] == '!' && wall[nx][ny] == -1)
			{
				wall[nx][ny] = wall[cx][cy];
				Q.push({ nx,ny,nd,map[nx][ny] });
			}
			if (map[nx][ny] == '.' && wall[nx][ny] == -1)
			{
				wall[nx][ny] = wall[cx][cy] + 1;
				Q.push({ nx,ny,nd,map[nx][ny] });
			}
		}

	}
}
