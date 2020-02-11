#include<iostream>
#include<queue>

using namespace std;

struct info { int x, y, active, life, time; bool spread, die; };
struct info2 { int x, y; };
struct info3 { int life, time;};

int T;
int N, M, K;
int map[300][300];
vector<info3> check[1100][1100];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
queue<info>Q;

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		//초기화


		//입력
		cin >> N >> M >> K;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				cin >> map[i][j];
				if (map[i][j] > 0)
				{
					check[i + 400][j + 400].push_back( {map[i][j],0});
					Q.push({ i,j,map[i][j],map[i][j],0,false,false });
				}
			}
		}

		while (!Q.empty())
		{
			int cx = Q.front().x;
			int cy = Q.front().y;
			int active = Q.front().active;
			int life = Q.front().life;
			int ct = Q.front().time;
			bool spread = Q.front().spread;
			bool die = Q.front().die;
			Q.pop();

			if (ct == K + 1) break;

			if (die == false) {
				if (active > 0 && life > 0)
				{
					active--;
					//if (active == 0) life--;
					Q.push({ cx,cy,active,life,ct + 1,false,false });
				}

				else if (active == 0)
				{
					if (spread == false)
					{

						for (int i = 0; i < 4; i++)
						{
							int nx = cx + dx[i];
							int ny = cy + dy[i];

							if (check[nx + 400][ny + 400].empty())
							{
								check[nx + 400][ny + 400].push_back({ life,ct + 1 });
								Q.push({ nx,ny,life,life,ct + 1,false,false });
							}

							else if (!check[nx + 400][ny + 400].empty())
							{
								if (check[nx + 400][ny + 400][0].time == ct + 1)
								{
									if (check[nx + 400][ny + 400][0].life < life)
									{
										check[nx + 400][ny + 400].clear();
										check[nx + 400][ny + 400].push_back({ life,ct + 1 });
										Q.push({ nx,ny,life,life,ct + 1,false,false });
									}
								}
							}
						}
					}
					else if (spread == true)
					{
						life--;
						if (life == 0) {
							check[cx + 400][cy + 400].clear();
							Q.push({ cx,cy,active,life,ct + 1,true,true });
						}
						else
						{
							check[cx + 400][cy + 400].clear();
							check[cx + 400][cy + 400].push_back({ life,ct + 1 });
							Q.push({ cx,cy,active,life,ct + 1,true,true });
						}
					}
				}
			}

		}
		
	
		cout << Q.size() << endl;
		
	}

	return 0;
}
