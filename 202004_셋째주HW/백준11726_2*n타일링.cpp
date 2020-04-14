#include<iostream>

using namespace std;

int N;
int memo[1010];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	memo[1] = 1;
	memo[2] = 2;

	for (int i = 3; i <= N; i++)
	{
		memo[i] = (memo[i - 1] + memo[i - 2]) % 10007; //계산하면서 오버플로우 발생할 수 있어서 마지막에 나머지를 나눠주는게 아니라
		                                               //계산하면서 나머지를 계속 나눠줘야함
	}

	cout << memo[N]<< endl;

	return 0;
}
