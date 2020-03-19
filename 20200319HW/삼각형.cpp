#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n;
int memo[510][510];
int Tri[510][510];

int main()
{
	cin >> n;
	
	for (int i = 1; i <= n; i++)
	{
		for (int k = 1; k <= i; k++)
		{
			cin >> Tri[i][k];
		}
	}

	memo[1][1] = Tri[1][1];

	//cout << memo[1][1] << endl;
	for (int i = 2; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			memo[i][j] = max(memo[i][j], max(memo[i - 1][j - 1] + Tri[i][j], memo[i - 1][j] + Tri[i][j]));
		}
	}

	int ans = -10e9;
	for (int i = 1; i <= n; i++)
	{
		ans = max(ans, memo[n][i]);  //이부분 *max_element(memo[n],memo[n]+n)이용하니까 100%에서 틀림
		                             //*max_element사용하려면 memo[n]+(n+1)로!!
	}

	cout << ans << endl;

	return 0;
}
