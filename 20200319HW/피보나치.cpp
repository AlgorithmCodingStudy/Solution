#include<iostream>
#include<cstring>

using namespace std;

struct info { int zero, one; };
int T;
info memo[45];

void fibo(int N);

int main()
{

	cin >> T;
	
	for (int q = 0; q < T; q++)
	{
		memset(memo, 0, sizeof(0));
		memo[0] = { 1,0 };
		memo[1] = { 0,1 };
		int N = 0;

		cin >> N;

		fibo(N);

		cout << memo[N].zero << " " << memo[N].one << endl;

	}

	return 0;

}

void fibo(int N)
{
	for (int i = 2; i <= N; i++)
	{
		memo[i].zero = memo[i - 1].zero + memo[i - 2].zero;
		memo[i].one = memo[i - 1].one + memo[i - 2].one;
	}
}
