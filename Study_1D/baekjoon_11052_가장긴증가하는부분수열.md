
# 문제링크

         https://www.acmicpc.net/problem/11053
      
--------------------------------------------------------------------------------------------------

### 접근 방법

     ==> 백준 '상자 넣기' 문제와 같음 //LIS연습!
     
--------------------------------------------------------------------------------------------------

### 설명 ( 코드 진행 )


<img width="200" alt="1" src="https://user-images.githubusercontent.com/29946480/70213469-c06d6600-177c-11ea-8ee5-0031e20f8b35.PNG">
# ▼
<img width="186" alt="2" src="https://user-images.githubusercontent.com/29946480/70213470-c06d6600-177c-11ea-8459-f3ac02dc2f4f.PNG">
# ▼
<img width="165" alt="3" src="https://user-images.githubusercontent.com/29946480/70213472-c105fc80-177c-11ea-8a4f-a92fcd6b2146.PNG">
# ▼
<img width="172" alt="4" src="https://user-images.githubusercontent.com/29946480/70213473-c105fc80-177c-11ea-8277-6f3f68085585.PNG">
# ▼
<img width="138" alt="5" src="https://user-images.githubusercontent.com/29946480/70213475-c105fc80-177c-11ea-9152-a5cda4258f16.PNG">
# ▼
# ...

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
