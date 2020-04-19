#include<iostream>
#include<cstring>
#include<set>
#include<vector>
#include<algorithm>

using namespace std;

int T;
int N, K, Split;
int init_pass[30];

bool desc(int a, int b)
{
	return a > b;
}

set<int>S;

void Cal_ten();
void Rotate();

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++) 
	{
  //테케여러개돌릴때 초기화잘해주기!
    S.clear();
		N = 0; K = 0,Split = 0;
		memset(init_pass, 0, sizeof(init_pass));

		cin >> N >> K;
		for (int i = 0; i < N; i++)
		{
			char num;
			cin >> num;
			if (num == 'A')init_pass[i] = 10;
			else if (num == 'B')init_pass[i] = 11;
			else if (num == 'C')init_pass[i] = 12;
			else if (num == 'D')init_pass[i] = 13;
			else if (num == 'E')init_pass[i] = 14;
			else if (num == 'F')init_pass[i] = 15;
			else init_pass[i] = num - '0';
		}
		Split = N / 4;


		for (int i = 0; i < Split; i++)
		{
			Cal_ten();
			Rotate();
		}

		vector<int>Result;
		set<int>::iterator iter;
		int count = 0;
		for (iter = S.begin(); iter != S.end(); iter++)
		{
			Result.push_back(*iter);
		}
		for (int i = Result.size() - 1; i >= 0; i--)
		{
			if (count == K - 1)
			{
				cout << '#' << q << " " << Result[i] << endl;
				break;
			}
			count++;
		}
	}
	return 0;
}

void Cal_ten()
{
	int cnt = Split;
	int idx = 0;

	for (int i = 0; i < 4; i++)
	{
		int Save = 0;
		while (cnt--)
		{
			Save += (init_pass[idx] * pow(16, cnt));
			idx++;
		}
		cnt = Split;
		S.insert(Save);
	}
}

void Rotate()
{
	int rot_pass[30];
	rot_pass[0] = init_pass[N - 1];
	for (int i = 1; i < N; i++)
	{
		rot_pass[i] = init_pass[i - 1];
	}

	memcpy(init_pass, rot_pass, sizeof(rot_pass));
}
