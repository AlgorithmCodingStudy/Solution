#include<iostream>
#include<queue>

using namespace std;

int N, Time;
int Sea[50][50];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
struct info { int x, y, time; };
struct Fish { int x, y, size, dist; 
bool operator<(const Fish& a)const //거리짧은 -> x작은 -> y작은순서
{
	if (dist == a.dist)
	{
		if (x == a.x)
		{
			return y > a.y;
		}
		return x > a.x;
	}
	return dist > a.dist;
};
};

priority_queue<Fish>F;
Fish Shark;

void Reset_Fish();
int FindDist(int x, int y);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> Sea[i][j];
			if (Sea[i][j] == 9)
			{
				Shark.x = i; Shark.y = j; Shark.size = 2; Shark.dist = 0; //초기상어정보저장
				Sea[i][j] = 0;
			}
		}
	}

	while (1) {

		Reset_Fish(); //물고기의 정보를 우선순위큐에 저장한다

		if (F.empty()) break; //만약 잡아먹을 물고기가 없다면 멈춤
		else //물고기가 있으면
		{
			int fishx = F.top().x; //가장위의 물고기정보를 저장
			int fishy = F.top().y;
			int fishsize = F.top().size;
			int fishdist = F.top().dist;
			
			Shark.x = fishx; //상어의 위치는 잡아먹을 물고기의 위치로변경
			Shark.y = fishy;
			Sea[fishx][fishy] = 0; //물고기 잡아먹었으니까 0으로 맵초기화

			Shark.dist++; //상어가 자기보다 작은 물고기 몇마리 잡아먹었는지

			if (Shark.dist == Shark.size) { //상어크기만큼 물고기잡아먹었으면
				Shark.size++; //상어크기 키워주고
				Shark.dist = 0; //잡아먹은물고기수 초기화
			}

			Time += F.top().dist; //상어가 움직인시간은 상어가움직인 거리와 같으므로 전역변수 Time에 계속 잡아먹은 물고기까지의 거리를 더함

			while (!F.empty()) //다음턴을위해 우선순위큐 초기화
			{
				F.pop();
			}
		}
	}

	cout << Time << "\n"; //정답출력
	
	return 0;
}

void Reset_Fish()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (Sea[i][j] < Shark.size && Sea[i][j] != 9 && Sea[i][j] > 0) //상어보다 물고기가작고, 상어가아니고, 0보다크면 잡아먹을수 있는 물고기
			{
				int D = FindDist(i, j); //상어와 물고기의 거리를 BFS로 구해준다
				if (D == -1)continue; //상어가 잡아먹을 물고기에 도달못하면 continue
				F.push({ i,j,Sea[i][j],D }); //우선순위큐에 정보를 저장
			}
		}
	}
}

int FindDist(int x, int y)//물고기위치
{
	queue<info>Q;
	bool visit[50][50] = { false };

	Q.push({ Shark.x,Shark.y,0 });
	visit[Shark.x][Shark.y] = true;

	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int t = Q.front().time;
		Q.pop();

		if (cx == x && cy == y) return t; //물고기위치가 상어위치랑 같을때 움직인 시간리턴

		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;
			if (Shark.size >= Sea[nx][ny] && !visit[nx][ny]) //방문안했고, 상어가 물고기보다 크거나같으면 지나갈수 있는길
			{
				visit[nx][ny] = true;
				Q.push({ nx,ny,t + 1 });
			}
		}
	}
	return -1; //상어가 물고기에 도달못했을때 처리해줘야함!
}
