
# 문제링크

         https://www.acmicpc.net/problem/11053
      
--------------------------------------------------------------------------------------------------

### 접근 방법

     ==> 백준 '상자 넣기' 문제와 같음 //LIS연습!
     
--------------------------------------------------------------------------------------------------

### 설명

     
     
     
--------------------------------------------------------------------------------------------------


```c
#include<iostream>
#include<algorithm>

using namespace std;

int N;
int A[1010] = { 0 };
int dp[1010] = { 0 };

void getLength()
{
	for (int i = 1; i <= N; i++)
	{
		int maxlength = 0;

		for (int j = i-1; j >= 0; j--)
		{
			if (A[i] > A[j])
			{
				maxlength = max(maxlength, dp[j]);
			}
		}
		dp[i] = maxlength + 1;
	}
}




int main()
{
	
	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		cin >> A[i];
	}

	getLength();

	int ans = *max_element(dp, dp + (N + 2));

	cout << ans << endl;

	return 0;
}
```
