# 문제링크

      https://www.acmicpc.net/problem/11568

---------------------------------------------------------------------------------------------------

### LIS (최장증가부분수열)

---------------------------------------------------------------------------------------------------

```c
#include<iostream>
#include<algorithm>

using namespace std;


int N;
int Arr[1010] = { 0 };
int dp[1010] = { 0 };

void getLongLength()
{
	for (int i = 1; i <= N; i++)
	{
		int numLength = 0; //초기값
		for (int j = i - 1; j >= 0; j--)
		{
			if (Arr[i] > Arr[j])
			{
				numLength = max(numLength, dp[j]);
			}
		}
		dp[i] = numLength + 1;
	}
}

int main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		cin >> Arr[i];
	}

	getLongLength();

	int Ans = *max_element(dp, dp + (N + 2));

	cout << Ans << "\n";

	return 0;
}
```
