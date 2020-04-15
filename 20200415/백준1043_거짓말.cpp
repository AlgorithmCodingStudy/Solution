#include<iostream>
#include<vector>

using namespace std;

int N, M;
int Trust;
vector<int>T;
int Party[60][60];
bool check[60];

int Find();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	cin >> Trust;
	for (int i = 0; i < Trust; i++)
	{
		int a;
		cin >> a;
		T.push_back(a);
	}

	for (int i = 0; i < M; i++)
	{
		int num;
		cin >> num;
		Party[i][0] = num;

		for (int j = 1; j <= num; j++)
		{
			cin >> Party[i][j];
		}
	}

	/*
	for (int i = 0; i < M; i++)
	{
		for (int j = 1; j <= Party[i][0]; j++) {
			cout << Party[i][j] << " ";
		}
		cout << endl;
	}*/

	if (Trust == 0)
	{
		cout << M << endl;
	}
	else
	{
		cout << Find() << endl;
	}
	return 0;
}

int Find()
{
	for (int k = 0; k < T.size(); k++)
	{
		int Tru = T[k];
		for (int i = 0; i < M; i++)
		{
			int L = Party[i][0];
			for (int j = 1; j <= L; j++)
			{
				if (Tru == Party[i][j])
				{
					check[i] = true;
					break;
				}
			}

		}
	}

	for (int i = 0; i < M; i++)
	{
		if (check[i] == true)
		{
			for (int j = 1; j <= Party[i][0]; j++)
			{
				for (int k = 0; k < T.size(); k++)
				{
					if (T[k] == Party[i][j])continue;
					else
					{
						T.push_back(Party[i][j]);
					}
				}
			}
		}
	}

	for (int k = 0; k < T.size(); k++)
	{
		int Tru = T[k];
		for (int i = 0; i < M; i++)
		{
			if (check[i])continue;
			for (int j = 1; j <= Party[i][0]; j++)
			{
				if (Tru == Party[i][j])
				{
					check[i] = true;
					break;
				}
			}

		}
	}

	int cnt = 0;
	for (int i = 0; i < M; i++)
	{
		if (!check[i])cnt++;
	}

	return cnt;
}
