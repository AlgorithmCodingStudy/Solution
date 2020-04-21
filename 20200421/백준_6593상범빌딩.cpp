#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>

using namespace std;

struct info { int floor,x,y,time; };
int L, R, C;
info S; info E;
bool check[35][35][35];
queue<info>Q;
int dx[] = { -1,1,0,0,0,0 };
int dy[] = { 0,0,-1,1,0,0 };
int dh[] = { 0,0,0,0,-1,1 };

int BFS(char Building[35][35][35]);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	while (1) 
	{
		char Building[35][35][35];
		S = { 0,0,0 }; E = { 0,0,0 };
		L = 0, R = 0; C = 0;
		while (!Q.empty())
		{
			Q.pop();
		}
		
		memset(check, false, sizeof(check));
		cin >> L >> R >> C;
		if (L == 0 && R == 0 && C == 0)break;


		int floor = L-1;
		for (int k = L; k >= 1; k--) 
		{
			for (int i = 0; i < R; i++)
			{
				for (int j = 0; j < C; j++)
				{
					cin >> Building[k][i][j];
					if (Building[k][i][j] == 'S')
					{
						Building[k][i][j] = '.';
						S = {k,i,j };
					}
					else if (Building[k][i][j] == 'E')
					{
						Building[k][i][j] = '.';
						E = { k,i,j };
					}
				}
			}
		}

		int result = BFS(Building);
		if (result > 0) cout <<"Escaped in "<<result<<" minute(s)." << endl;
		else cout << "Trapped!" << endl;
	}
	return 0;
}

int BFS(char Building[35][35][35])
{
	Q.push({ S.floor,S.x,S.y,0 });
	check[S.floor][S.x][S.y] = true;

	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int cf = Q.front().floor;
		int ct = Q.front().time;
	//	cout << cx << " " << cy << " " << cf <<"  "<<ct<<endl;
		Q.pop();

		if (cx == E.x && cy == E.y && cf == E.floor) return ct;

		for (int i = 0; i < 6; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			int nf = cf + dh[i];

			if (nx < 0 || ny < 0 || nx >= R || ny >= C || nf<0 || nf>L)continue;
			if (!check[nf][nx][ny] && Building[nf][nx][ny] == '.')
			{
				Q.push({ nf,nx,ny,ct+1 });
				check[nf][nx][ny] = true;
			}
		}
	}

	return -1;
}
