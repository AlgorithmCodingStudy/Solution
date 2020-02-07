#include<iostream>
#include<vector>
#include<queue>
#include<cstring>

using namespace std;


struct info { int idx, order; };
int T;
int Magnet[5][10];
bool check[5];
vector<info>Ro;

void Rotate(int idx, int order);
void checkrotate(int idx, int order);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		int K;
		cin >> K;

		for (int i = 1; i <= 4; i++)
		{
			for (int j = 0; j < 8; j++)
			{
				cin >> Magnet[i][j];
			}
		}

		for (int i = 0; i < K; i++)
		{
			int idx, order = 0;
			cin >> idx >> order;

			//초기화
			memset(check, false, sizeof(check));
			Ro.clear();

			check[idx] = true;
			Ro.push_back({ idx,order }); //원래 실행해야하는 명령 푸시
			checkrotate(idx,order);
			
			for (int j = 0; j < Ro.size(); j++)
			{
				Rotate(Ro[j].idx, Ro[j].order);
			}
			/*
			cout << "\n";
			for (int j = 1; j <= 4; j++)
			{
				for (int k = 0; k <= 7; k++)
				{
					cout << Magnet[j][k] << " ";
				}
				cout << "\n";
			}
			cout << "\n";*/
		}

		int ans = 0;
		if (Magnet[1][0] == 1) ans += 1;
		if (Magnet[2][0] == 1) ans += 2;
		if (Magnet[3][0] == 1) ans += 4;
		if (Magnet[4][0] == 1) ans += 8;

		cout << '#' << q << ' ' << ans << "\n";
	}

	return 0;
}

void checkrotate(int idx, int order)
{
	
	if (idx == 1)
	{
		if (Magnet[idx][2] != Magnet[idx + 1][6] && check[idx+1]==false)
		{
			check[idx+1] = true;
			Ro.push_back({ idx+1,0-(order) }); //원래 실행해야하는 명령 푸시
			checkrotate(idx + 1, 0 - (order));
		}
		return;
	}

	else if (idx == 2 || idx == 3)
	{
		if (Magnet[idx][6] != Magnet[idx - 1][2] && check[idx-1]==false)
		{
			check[idx-1] = true;
			Ro.push_back({ idx - 1,0 - (order) }); //원래 실행해야하는 명령 푸시
			checkrotate(idx - 1, 0 - (order));
		}
		if (Magnet[idx][2] != Magnet[idx + 1][6]&&check[idx + 1] == false)
		{
			check[idx+1] = true;
			Ro.push_back({ idx + 1,0 - (order) }); //원래 실행해야하는 명령 푸시
			checkrotate(idx + 1, 0 - (order));
		}
		return;
	}

	else if (idx == 4)
	{
		if (Magnet[idx][6] != Magnet[idx - 1][2]&&check[idx - 1] == false)
		{
			check[idx-1] = true;
			Ro.push_back({ idx - 1,0 - (order) }); //원래 실행해야하는 명령 푸시
			checkrotate(idx - 1, 0 - (order));
		}
		return;
	}
}


void Rotate(int idx, int order)
{
	queue<int>temp;

	for (int i = 0; i < 8; i++)
	{
		temp.push(Magnet[idx][i]);
	}

	if (order == 1)
	{
		for (int j = 1; j < 8; j++)
		{
			Magnet[idx][j] = temp.front();
			temp.pop();
		}

		Magnet[idx][0] = temp.front();
		temp.pop();
	}

	else if (order == -1)
	{
		Magnet[idx][7] = temp.front();
		temp.pop();

		for (int j = 0; j < 7; j++)
		{
			Magnet[idx][j] = temp.front();
			temp.pop();
		}
	}
}
