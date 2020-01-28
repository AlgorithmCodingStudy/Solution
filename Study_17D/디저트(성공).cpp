/*
  ## 문제를 정확히 읽자! 설계를 제대로하자! 
  
  << 접근 방법 >>

  1. 행 (0~N-2) / 열 (1~N-1) 의 인덱스를 시작점으로 하는 모든 사각형을 만듦 ==> 브루트포스
  
  2. 무조건 우하(0)->좌하(1)->좌상(2)->우상(3) 순서로 dx,dy인덱스를 설정해주고, 이 순서대로 탐색을 진행함 
     ( 이렇게 사각형을 만들어주면 같은모양&다른시작점으로 만들어지는 사각형의 중복을 피할 수 있음 )
     
  3. DFS(현재x,현재y,현재dir)로 설정해주고 0,1,2,3의 순서로 다음방향 탐색 
     -> 만약 먹은 디저트 종류를 체크하는 배열이 false이고, 범위를 벗어나지 않은 경우만 탐색
     -> 탐색할때, 직진인경우와 방향을 꺽은경우 두가지로 나눠서 DFS를 돌려준다 (만들수있는 모든 사각형을 탐색하기위해)
   
*/
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

int T, N;
int map[25][25];
int dx[] = { 1,1,-1,-1 };
int dy[] = { 1,-1,-1,1 };
int MMax = -99999;
bool dessert[110];
int sx, sy;
vector<int>V;

void DFS(int x, int y, int dir);

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		MMax = -99999;
		N = 0;
		cin >> N;
		
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				cin >> map[i][j];
			}
		}

		for (int i = 0; i < N - 2; i++)
		{
			for (int j = 1; j < N - 1; j++)
			{

				V.clear();
				memset(dessert, false, sizeof(dessert));

				sx = i;
				sy = j;

				dessert[map[i][j]] = true;
				V.push_back(map[i][j]);
				DFS(i, j, 0);
			}
		}

		if (MMax == -99999)
			cout <<'#'<<q<<' '<< -1 << endl;
		else
			cout <<'#'<<q<<' '<< MMax << endl;

	}

	return 0;
}


void DFS(int x, int y, int dir)
{

	int nx = x + dx[dir];
	int ny = y + dy[dir];
	int d = dir % 4; //방향을 꺽을경우 d+1을 해줌으로 0,1,2,3의 인덱스에 접근하기 위해 %4해줌

	if (nx == sx && ny == sy && nd == 3) //다음위치가 시작위치랑 같고, 현재 방향이 3 (사각형의 네번째 변)일 경우
	{
		int ans = V.size(); //먹은 디저트의 갯수를 최댓값과 비교
		MMax = max(MMax, ans);
		return;
	}

	if (nx < 0 || ny < 0 || nx >= N || ny >= N)return; //범위벗어나면 리턴

	if (dessert[map[nx][ny]] == false) //다음위치의 디저트종류를 이전에 먹은적이 없을 경우
	{
		dessert[map[nx][ny]] = true;
		V.push_back(map[nx][ny]);
		DFS(nx, ny, d); //직진
		DFS(nx, ny, d + 1); //방향 꺽음
		dessert[map[nx][ny]] = false;
		V.pop_back();
	}
}
