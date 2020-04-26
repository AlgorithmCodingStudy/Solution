/*
설계 정리가 필요!
1. 상어위치 저장
2. Can함수 --> ㄱ. 상어위치에서 BFS돌림(상어가 지나갈수 없는 위치 못지나가게 설계)
               ㄴ. BFS돌린 결과 check배열(상어에서 물고기까지 시간저장)에서 물고기가 있고, 상어보다 작은크기의 정보 PQ에 저장
               ㄷ. PQ사이즈가 1이상이면 먹을 물고기가 있는거 return true // 아니면 return false
3. Can함수가 false거나 AllFish ==0 이면 먹을물고기 없는거 -> while문 break
4. Can함수가 true면 상어의 위치를 우선순위큐의 top값으로 바꿔주고, 상어 사이즈와 물고기 먹은개수 바꿔줌, 걸린시간(PQ의 top.time)도 cnt에 더해줌
5. 다음턴을 위해 PQ통 초기화 
*/


//40분컷

#include<iostream>
#include<queue>
#include<cstring>

using namespace std;

struct Shark { int x, y, size, eat; };
struct Fish { int x, y, time;
bool operator <(const Fish& a)const
{
	if (time == a.time)
	{
		if (x == a.x)
			return y > a.y;
		return x > a.x;
	}
	return time > a.time;
};
};
struct QFish{
	int x, y, time;
	
};
int N;
int Map[25][25];
int check[25][25];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int Allfish;
Shark S;
priority_queue<Fish>F;

bool Can();

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
			cin >> Map[i][j];
			if (Map[i][j] == 9)
			{
				S = { i,j,2,0 };
				Map[i][j] = 0;
			}
			else if (Map[i][j] > 0 && Map[i][j] <= 6)
			{
				Allfish++;
			}
		}
	}

	if (Allfish == 0) cout << 0;
	else
	{
		int cnt = 0;
		while (1)
		{
			if (!Can() || Allfish == 0)break;
			int eatx = F.top().x;
			int eaty = F.top().y;
			cnt += F.top().time;
			
			S.eat++;
			S.x = eatx;
			S.y = eaty;
			if (S.eat == S.size)
			{
				S.size++;
				S.eat = 0;
			}
			Map[eatx][eaty] = 0;
			Allfish--;
			while (!F.empty())
			{
				F.pop();
			}
		}
		cout << cnt << endl;
	}

	return 0;
}


bool Can()
{
	memset(check, -1, sizeof(check));
	queue<QFish>Q;

	Q.push({ S.x,S.y,0 });
	check[S.x][S.y] = 0;

	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int ct = Q.front().time;
		
		Q.pop();
		
		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			if (nx < 0 || ny < 0 || nx >= N || ny >= N)continue;

			if (Map[nx][ny] <= S.size && check[nx][ny]==-1)
			{
				check[nx][ny] = check[cx][cy]+1;
				Q.push({ nx,ny,ct+1 });
			}
		}
	}
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (Map[i][j] < S.size && Map[i][j] !=0 && check[i][j] != -1)
				F.push({ i,j,check[i][j] });
		}
	}

	if (F.size() >= 1)return true;
	return false;
}
