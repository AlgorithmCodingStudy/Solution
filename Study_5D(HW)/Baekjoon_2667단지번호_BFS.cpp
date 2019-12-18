#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>

using namespace std;

int N;
bool check[30][30] = { false };
string map[30]; //띄어쓰기 없는 숫자 입력받을때 문자열로 입력받기!(C++일경우 %1d사용못하니까)
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

vector<int>result;

struct info { int x, y; };
queue<info>Q;

void BFS()
{
	int house = 1; //집의 갯수 1부터 (map[x][y]가 1일때 BFS시작하니까

	while (!Q.empty()) //Q가 빌때까지 반복
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		Q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue; //map의 범위 넘으면 패스
			if (check[nx][ny] == false && map[nx].at(ny) == '1') //다음 위치의 문자열의 값이'1'이고 방문하지 않았으면
			{
				check[nx][ny] = true; //다음위치 방문체크
				house++; //집의 갯수 세줌
				Q.push({ nx,ny }); //Q에 다음위치 넣기
			}
		}
	}

	result.push_back(house); //Q가 비었을때 (단지를 다 돌았을때) 카운트한 집의 갯수를 벡터에 저장
} 


int main()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> map[i]; 
	}


	for (int i = 0; i < N; i++) //행
	{
		for (int j = 0; j < map[i].length(); j++) //열 ==> string의 길이
		{
			if (check[i][j] == true)continue;
			if (map[i].at(j) == '1') //map의 요소를 비교할때 문자열로 입력받았으므로 '1'로 비교해줘야함!
			{
				check[i][j] = true;
				Q.push({ i,j });
				BFS();
			}
		}
	}

	cout << result.size() << endl;
	sort(result.begin(), result.end());
	for (int i = 0; i < result.size(); i++)
	{
		cout << result[i] << endl;
	}

	return 0;
}
