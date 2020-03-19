#include<iostream>
#include<algorithm>

using namespace std;

int memo[3][1010][35]; //자두나무종류, 시간, 움직인횟수
int Jadu[1010];
int T, W;

int main()
{
	cin >> T >> W;
	for (int i = 1; i <= T; i++)
	{
		cin >> Jadu[i];
	}

	for (int i = 1; i <= T; i++)
	{
		for (int j = 1; j <= W+1; j++)
		{
			if (Jadu[i] == 1)
			{
				memo[1][i][j] = max(memo[1][i - 1][j] + 1, memo[2][i - 1][j - 1] + 1);
				memo[2][i][j] = max(memo[2][i - 1][j], memo[1][i - 1][j - 1]);
			}
			else
			{
				if (i == 1 && j == 1)continue; //초기값 자두1번아래에 위치
				memo[1][i][j] = max(memo[1][i - 1][j], memo[2][i - 1][j - 1]);
				memo[2][i][j] =  max(memo[2][i - 1][j]+1, memo[1][i - 1][j - 1]+1);
			}
		}
	}

	int result = -10e9;
	for (int i = 1; i <= W+1; i++)
	{
		result = max(result, max(memo[1][T][i], memo[2][T][i]));
	}

	cout << result << endl;
	return 0;
}
