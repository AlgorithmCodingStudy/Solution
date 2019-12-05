```c
#include<iostream>
#include<algorithm>

using namespace std;

int N;
int box[1001] = {0};
int dp[1001] = {0};

void selectbox()
{
	for (int i = 1; i <= N; i++) //1~N까지
	{
		int mmax = 0; 
		for (int j = i; j > 0; j--)// 기준이 되는 i번째 값 이전의 값들 중 최대 수열의 길이을 구한다
		{
			if (box[i] > box[j]) //현재(i)값이 이전의 값보다 클경우
			{
				mmax = max(mmax, dp[j]); //mmax와, 이전의 값 중 큰값구하기 //0~i-1까지 반복하면서 제일 큰 dp값구하기
			}
		}
		dp[i] = mmax + 1; //구한 최대값 + 1해줌
	}
}


int main()
{
	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		cin >> box[i]; //배열 인덱스 1부터 수열 입력받음
	}

	selectbox(); //최장수열 구하는 함수.

	int result = *max_element(dp, dp + N + 2); //최장수열길이 구하고 출력

	cout << result << endl;
	return 0;
} 
```
