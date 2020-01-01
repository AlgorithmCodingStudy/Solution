#include<iostream>

using namespace std;

int N;
int map[110][110] = { 0 };
int connect_map[110][110] = { 0 };


/*

  1 -> 2 
   \  /
    3
  
1) 1 -> 2 경로있으니까, 2번째 행 검사                       1 1 1
2) 2 -> 3 경로있으니까, 1->3가능                   =>      1 1 1
3) 3 -> 1 경로있으니까 3->1 가능                           1 1 1

*/

void DFS(int curcol, int currow) //현재의 행, 열을 넘김
{
	for (int i = 0; i < N; i++) //열의 인덱스 0~N-1까지 돌면서 경로있나 탐색
	{
		if (map[currow][i] == 1 && connect_map[curcol][i] == 0) 
		{
			connect_map[curcol][i] = 1;
			DFS(curcol,i);
		}
	}

}

int main()
{
  //입력
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> map[i][j];
		}
	}
  
  //DFS탐색
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (map[i][j] == 1) // i->j의 경로가 있을 경우
			{
				connect_map[i][j] = 1; //connect_map에 체크(방문체크대신)
				DFS(i,j); 
			}
		}
	}

  //출력
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cout << connect_map[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}
