//BFS로 접근할 필요없는 시뮬레이션!

/*

잘못생각한 부분 : 같은칸에 미생물이 모였을경우, 한꺼번에 처리를해야하는데 나는 queue이용해서 바로바로 처리해서 틀림

--> a,b,c군집이 한칸에 모인경우 ==> 아래에 구현 : a+b,c --> a+b+c 이런식으로 구현함
                              ==> 맞으려면 a,b,c한번에 size체크해서 방향을 구해야함 

*/


#include<iostream>
#include<queue>

using namespace std;


struct info { int x, y, dir, num, time; };
struct info2 { int num, dir;};
int T,N,M,K;
vector<info2> map[110][110];
//int visit[110][110];
int dx[] = { 0,-1,1,0,0 };
int dy[] = { 0,0,0,-1,1 };
queue<info>Q;

void BFS();

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		//초기화
		int result = 0;
		N = 0, M = 0, K = 0;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				map[i][j].clear();
			}
		}
		while (!Q.empty())
		{
			Q.pop();
		}

		//입력
		cin >> N >> M >> K;
		for (int i = 0; i < K; i++)
		{
			int x, y, num, dir;
			cin >> x >> y >> num >> dir;
			Q.push({ x,y,dir,num,1 });
			map[x][y].push_back({ num,dir });
		}

		BFS();

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
		cout <<'#'<<q<<' '<< result-1<<endl;
	}

	return 0;
}

void BFS()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int cd = Q.front().dir;
		int cn = Q.front().num;
		int ct = Q.front().time;
		Q.pop();
		map[cx][cy].clear();
		
		if (ct == M) return;

		int nx = cx + dx[cd];
		int ny = cy + dy[cd];
		int nd = cd;
		int nn = cn;
		int nt = ct + 1;
		//cout << "cd: " << cd << " nd" << nd << endl;

		if (nx == 0 || ny == 0) {
			nd += 1;
			nn /= 2;
			if (nn <= 0) continue;
		}
		else if (nx == N-1 || ny == N-1)
		{
			nd -= 1;
			nn /= 2;
			if (nn <= 0)continue;
		}
		
		

		if (map[nx][ny].size( )> 1)
		{
			int numhap = nn;
			int maxdir = nd;
			int maxnum = nn;

			for (int i = 0; i < map[nx][ny].size(); i++)
			{
				//cout <<i<<" "<< map[nx][ny][i].num << map[nx][ny][i].dir <<endl;
				if (map[nx][ny][i].num > maxnum)
				{
					maxnum = map[nx][ny][i].num;
					maxdir = map[nx][ny][i].dir;
				}
				numhap += map[nx][ny][i].num;
			}
			//cout << "여러개 : " << nx << " " << ny << ' ' << maxdir<< ' ' << numhap << endl;
			map[nx][ny].clear();
		
			map[nx][ny].push_back({ numhap,maxdir });
			Q.push({ nx,ny,maxdir,numhap,nt });
		}

		else
		{
			map[nx][ny].push_back({ nn,nd });
			Q.push({ nx,ny,nd,nn,nt });
		}
		/*
		cout << endl;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (map[i][j].size() > 0)
				{
					cout << "1";
				}
				else
					cout << "0";
			}
			cout << endl;
		}*/
	}

}
