#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

// 1. 직사각형 색칠하기  =>  map을 1로 체크
//  << 좌표가 기존이랑 다름! *주의* >>
// 2. dfs돌면서 영역의 갯수세기

int M, N, K;
int cnt = 0;
bool map[101][101] = { 0 };
bool check[101][101] = { 0 };
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

struct Dot {
	int x1, y1, x2, y2; //구조체로 좌표 한번에 저장
};

vector<Dot>dir; //vector에 좌표저장
vector<int>result; //각 영역의 값 저장

void paint();
void DFS(int curx, int cury);
void result_print(int region);

int main()
{
	cin >> M >> N >> K;

	for (int i = 0; i < K; i++)
	{
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		dir.push_back({ a,b,c - 1,d - 1 });
	}

	paint(); //좌표값으로 직사각형 색칠

	int region = 0; //큰 덩어리갯수의 변수

	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (check[i][j] == true) continue; // 방문했으면 건너뛰기
			if (map[i][j] == false)  //map에 색칠 안되있으면
			{
				cnt = 1; //현재의 값도 포함해줘야해서 cnt =1 로
				check[i][j] = true; //방문체크
				DFS(i, j); //DFS(돌기)
				region++; //큰 덩어리갯수++
				if (cnt > 0) //영역의갯수가 있으면 result에 저장
					result.push_back(cnt);
			}
		}
	}

	sort(result.begin(), result.end()); // 정렬해줌

	result_print(region); //결과 프린트

	return 0;
}

void result_print(int region) //결과 프린트
{

	cout << region << endl;

	for (int i = 0; i < result.size(); i++)
	{
		cout << result[i] << " ";
	}
}

void DFS(int curx, int cury)
{

	for (int i = 0; i < 4; i++)
	{
		int nx = curx + dx[i];
		int ny = cury + dy[i];

		if (nx < 0 || ny < 0 || nx >= M || ny >= N)continue;
		if (check[nx][ny] == false && map[nx][ny] == false)
		{
			check[nx][ny] = true;
			cnt++; //작은 영역갯수 카운트
			DFS(nx, ny);
		}

	}
}


void paint() //직사각형 색칠
{
	for (int i = 0; i < dir.size(); i++)
	{
		int x1 = dir[i].x1;
		int y1 = dir[i].y1;
		int x2 = dir[i].x2;
		int y2 = dir[i].y2;

		for (int j = y1; j <= y2; j++)
		{
			for (int k = x1; k <= x2; k++)
			{
				map[j][k] = true;
			}
		}
    
	}
}
