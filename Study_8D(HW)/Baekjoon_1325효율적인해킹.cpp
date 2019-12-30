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

/*
예제의 인접리스트 -->  1 | 3
                      2 | 3
		      3 | 4 5
		      4 |
		      5 |
		      문제에서 b를해킹했을때, a도 해킹된다해서 인접리스트를 Computer[b][a]로 만듦

*/

void DFS(int cur) 
{
	for (int i = 0; i < Computer[cur].size(); i++) //현재 컴퓨터의 인덱스의 벡터길이만큼 검사
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
	cout.tie(NULL);

	cin >> N >> M;
		
	for (int i = 0; i < M; i++)
	{
		int a = 0; int b = 0;
		cin >> a >> b;
		Computer[b].push_back(a); //인접리스트 만들기
	}

	for (int i = 1; i <= N; i++)
	{
		cnt = 0; //연결된 컴퓨터수 저장하는 변수
		memset(check, false, sizeof(check)); //컴퓨터 넘버별로 연결된 컴퓨터 찾아야해서 방문 초기화해줘야함
		check[i] = true; //현재 컴퓨터도 방문체크해줘야함
		DFS(i);
		comnum[i] = cnt;
	}

	int mmax = *max_element(comnum+1, comnum + (N+1)); //컴퓨터 넘버 1~N까지 연결된 수를 배열에 저장했으니까, 최댓값구할때 배열 범위 주의

	for (int i = 1; i <= N; i++)
	{
		if (comnum[i] == mmax) {
			cout << i << " ";
		}
	}

	return 0;
}
