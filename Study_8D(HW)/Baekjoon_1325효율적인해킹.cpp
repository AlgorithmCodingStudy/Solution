//90퍼에서 틀림


#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

int comnum[10010]= { 0 };
bool check[10010];
int N, M;
int cnt = 0;
vector<int>Computer[10010];
bool many;

void DFS(int cur)
{
	for (int i = 0; i < Computer[cur].size(); i++)
	{
		if (check[Computer[cur][i]] == false)
		{
			cnt++;
			check[Computer[cur][i]] = true;
			DFS(Computer[cur][i]);
		}
	}
}

int main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	

	cin >> N >> M;
		
	for (int i = 0; i < M; i++)
	{
		int a = 0; int b = 0;
		cin >> a >> b;
		Computer[b].push_back(a); //인접리스트생성
	}

	for (int i = 1; i <= N; i++)
	{
		cnt = 0;
		memset(check, false, sizeof(check));
		check[i] = true;
		DFS(i);
		comnum[i] = cnt;
	}

	int mmax = *max_element(comnum, comnum + N);

	for (int i = 1; i <= N; i++)
	{
	
		if (comnum[i] == mmax) {
			cout << i << " ";
		}
	}

	return 0;
}
