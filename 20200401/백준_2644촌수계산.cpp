#include<iostream>
#include<queue>
#include<cstring>
#include<vector>

using namespace std;


int Ans[110];
int N,M;
int finda, findb;

queue<int>Q;
vector<int>Connect[110];

void BFS();

int main()
{
	memset(Ans, -1, sizeof(Ans));

	cin >> N;
	cin >> finda >> findb;
	cin >> M;

	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		Connect[a].push_back(b);
		Connect[b].push_back(a);
	}

	Q.push(finda);
	Ans[finda] = 0;

	BFS();

	cout << Ans[findb] << endl;

	return 0;
}

void BFS()
{
	while (!Q.empty())
	{
		int cur = Q.front();
		Q.pop();

		for (int i = 0; i < Connect[cur].size(); i++)
		{
			if (Ans[Connect[cur][i]] != -1)continue;
			Ans[Connect[cur][i]] = Ans[cur] + 1;
			Q.push(Connect[cur][i]);
		}
	}
}
