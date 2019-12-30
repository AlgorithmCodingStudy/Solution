#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstring>

using namespace std;

int N, M;
int connect[110][110] = { 0 }; //인접행렬
int ans[110] = {0 };
queue<int>Q;


void BFS(int idx)
{
	Q.push(idx);
	ans[idx] = 0;

	while (!Q.empty())
	{
		int cur = Q.front();
		Q.pop();
		for (int i = 1; i <= N; i++)
		{
			if (connect[cur][i] != 1 || ans[i] >= 0)continue;
			Q.push(i);
			ans[i] = ans[cur] + 1;
		}
	}

}
int main()
{
	cin >> N >> M;

	for (int i = 1; i <= M; i++)
	{
		int a = 0; int b = 0;
		cin >> a >> b;
		connect[a][b] = 1;
		connect[b][a] = 1;
	}
	
	vector<int>result;
	for (int i = 1; i <= N; i++)
	{
		while (!Q.empty())
		{
			Q.pop(); //queue초기화
		}
		memset(ans, -1, sizeof(ans));
		BFS(i);
		int hap = 0;
		for (int i = 1; i <= N; i++)
		{
			hap += ans[i]; //각 인덱스의 케빈베이컨합을구함
		}
		result.push_back(hap);
	}
	int mmin = *min_element(result.begin(), result.end());
  
	for (int i = 0; i < result.size(); i++)
	{
		if (result[i] == mmin)
		{
			cout << i+1; //1~N까지 수를 벡터에 0~N-1로 저장해서
			return 0; //출력을했으면 바로종료 (해당 인덱스가 여러개일경우, 가장 작은 인덱스 출력하기위해서)
		}
	}
}
