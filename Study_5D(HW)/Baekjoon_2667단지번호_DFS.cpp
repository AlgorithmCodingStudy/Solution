/*
<dfs탐색>
1. 지도크기 25이하
2. 집이있으면 1, 집이 없으면 0
3. 단지의개수(dfs재귀가 끝나면 카운트)
4. 단지 내 집의갯수(dfs에서 카운트)
*/

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>

using namespace std;

int N = 0; 
int house = 0;
int map[26][26] = { 0 };
bool check[26][26] = { false };
int dx[] = { -1,1,0,0 }; //서,동,남,북
int dy[] = { 0,0,-1,1 }; //서,동,남,북

vector<int>houseNum;

void DFS(int cx, int cy)
{
	for (int i = 0; i < 4; i++)
	{
		int nx = cx + dx[i]; //다음x위치
		int ny = cy + dy[i]; //다음y위치

		if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue; //map의 크기 벗어나면 패스
    
		if (check[nx][ny] == false && map[nx][ny] == 1) //방문안했고, map이1이면
		{
			check[nx][ny] = true; //방문체크
			house++; //집개수++
			DFS(nx, ny); //다음위치재귀
		}
    
	}

	return;
}

int main()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%1d",&map[i][j]); //***띄어쓰기 없이 받을때 주의하기!!!!!!!**** 내 두시간...ㅠㅠ
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (check[i][j] == true)continue; //방문했으면 패스
			if (map[i][j] == 1)
			{
				house = 1; //현재위치도 map이1이니까 카운트
				check[i][j] = true; //방문체크
				DFS(i, j);
				houseNum.push_back(house); //집의갯수 vector에넣기
			}
		}
	}

	cout << houseNum.size() << endl; //벡터크기가 영역의 크기
  
	sort(houseNum.begin(), houseNum.end()); //정렬
  
	for (int i = 0; i < houseNum.size(); i++)
	{
		cout << houseNum[i] << endl;
	}

	return 0;
}


