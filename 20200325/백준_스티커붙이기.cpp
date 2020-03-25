#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>

using namespace std;

int N, M, K;
int map[45][45];
int sticker[45][45]; 

void Rotate(int C, int R);
bool Can_Patch(int sx, int sy, int C, int R);
void Patch(int sx, int sy, int C, int R);

int main()
{
	cin >> N >> M >> K;
	for (int q = 0; q < K; q++)
	{
		//초기화
		memset(sticker, 0, sizeof(sticker));
		int C, R;
		

		//주어진 입력
		cin >> C >> R;
		for (int i = 0; i < C; i++)
		{
			for (int j = 0; j < R; j++)
			{
				cin >> sticker[i][j];
			}
		}
		
			if (C > N || R > M)
			{
				Rotate(C, R);
			}
		
		while (1) {

			bool flag = false;
			bool cannotpatch = true;

			for (int i = 0; i < N; i++)
			{
				for (int j = 0; j < M; j++)
				{
					if (map[i][j] == 0)
					{
						if (Can_Patch(i, j, C, R))
						{
							flag = true;
							cannotpatch = false;
							Patch(i, j, C, R);
							break;
						}
						else continue;
					}
				}
				if (flag) break;
			}

			if (cannotpatch)
			{
				Rotate(C, R);
				continue;
			}
			else break;
		}

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				cout << map[i][j] << " ";
			}
			cout << endl;
		}
	}
	
	

	return 0;
}

void Rotate(int C, int R)
{
	queue<int>Q;
	int temp[45][45] = { 0 };

	cout << "회전" << endl;
	for (int i = 0; i < C; i++)
	{
		for (int j = 0; j < R; j++)
		{
			Q.push(sticker[i][j]);
			cout << sticker[i][j] << " ";
		}
		cout << endl;
	}

	
	for (int i = C-1; i >= 0; i--)
	{
		for (int j = 0; j <R; j++)
		{
			temp[j][i] = Q.front();
			Q.pop();
			if (Q.empty())break;
		}
	}

	
	memcpy(&sticker, &temp, sizeof(temp));

	
	cout << endl;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cout << sticker[i][j] << " ";
		}
		cout << endl;
	}
}

bool Can_Patch(int sx, int sy, int C, int R)
{

	for (int i = sx; i < sx + C; i++)
	{
		for (int j = sy; j < sy + R; j++)
		{
			if (i >= N || j >= M|| map[i][j]==1)return false;
		}
	}

	return true;

}

void Patch(int sx, int sy, int C, int R)
{
	queue<int>Q;
	for (int i = 0; i < C; i++)
	{
		for (int j = 0; j < R; j++)
		{
			Q.push(sticker[i][j]);
		}
	}

	for (int i = sx; i < sx + C; i++)
	{
		for (int j = sy; j < sy + R; j++)
		{
			map[i][j] = Q.front();
			Q.pop();
			if (Q.empty())break;
		}
	}

}
