//벡터와, 벡터map이용하여 접근

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


struct info { int x, y, dir, num; };
struct info2 {
	int num, dir;
	bool operator< (const info2& a) const //내림차순으로 sort 연산자오버로딩
	{
		return a.num < num;
	}
};
int T, N, M, K;
vector<info2> map[110][110];
vector<info>V;
vector<info>Vcpy;
int dx[] = { 0,-1,1,0,0 };
int dy[] = { 0,0,0,-1,1 };

void map_init()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			map[i][j].clear();
		}
	}
}

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		//초기화
		int result = 0;
		N = 0, M = 0, K = 0;
		V.clear();

		//입력
		cin >> N >> M >> K;
		for (int i = 0; i < K; i++)
		{
			int x, y, num, dir;
			cin >> x >> y >> num >> dir;
			V.push_back({ x,y,dir,num });
		}


		for (int w = 0; w < M; w++) //M초까지 돌려줌
		{
			map_init();
			Vcpy.clear();

			for (int i = 0; i < V.size(); i++)
			{
				int cx = V[i].x;
				int cy = V[i].y;
				int cd = V[i].dir;
				int cn = V[i].num;

				int nx = cx + dx[cd];
				int ny = cy + dy[cd];
				int nd = cd;
				int nn = cn;

				if (nx == 0 || ny == 0) { //테두리에 걸릴경우 방향과 미생물의 양 처리
					nd += 1;
					nn /= 2;
					if (nn <= 0) continue;
				}

				else if (nx == N - 1 || ny == N - 1) //테두리에 걸릴경우 방향과 미생물의 양 처리
				{
					nd -= 1;
					nn /= 2;
					if (nn <= 0)continue;
				}

				map[nx][ny].push_back({ nn,nd }); //map에 넣어주는경우 --> 한칸에 여러개의 미생물이 있을경우를 처리하려고
			}


			for (int i = 0; i < N; i++)
			{
				for (int j = 0; j < N; j++)
				{
					if (map[i][j].size() >= 1) //여러개의 미생물이 있을경우
					{
						sort(map[i][j].begin(), map[i][j].end()); //내림차순으로 정렬

						int d = map[i][j][0].dir; //가장 앞에값의 방향이 앞으로 이 군집의 방향 --> 제일 큰 미생물군집의 방향 
						int n = 0;
						for (int k = 0; k < map[i][j].size(); k++)
							n += map[i][j][k].num; //미생물 수 합쳐줌
						Vcpy.push_back({ i,j,d,n }); //새로운 벡터에 미생물군집의 정보 업데이트
					}
				}
			}

			V.clear();
			V.assign(Vcpy.begin(), Vcpy.end()); //처음벡터에 바뀐정보 복사

		}

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (map[i][j].size() > 0)
				{
					for (int k = 0; k < map[i][j].size(); k++)
					{
						result += map[i][j][k].num;
					}
				}
			}
		}
		cout << '#' << q << ' ' << result << endl;
	}

	return 0;
}



