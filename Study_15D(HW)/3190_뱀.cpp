//뱀의 길이 바뀌는거 deque이용
//map에 방향바뀌는 시간 저장

#include<iostream>
#include<map>
#include<queue>

using namespace std;

int N, K, L,time;
char board[110][110];
struct info { int x, y, dir; };
deque<info>S;
map<int, char>change;
int dx[] = { -1,0,1,0 };
int dy[] = { 0,1,0,-1 };

void move_snake();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	cin >> K;
	for (int i = 0; i < K; i++)
	{
		int a, b = 0;
		cin >> a >> b;
		board[a][b] = 'a';
	}

	cin >> L;
	for (int i = 0; i < L; i++)
	{
		int a = 0; char b;
		cin >> a >> b;
		change[a] = b;
	}

	S.push_back({ 1,1,1 });
	move_snake();
	
	cout << time << endl;

	return 0;
}

void move_snake()
{
	while (1)
	{
		int cx = S.front().x;
		int cy = S.front().y;
		int cd = S.front().dir;
		int nd = cd;
		time++;

		if (change.find(time) != change.end())//time이라는 key값에 value가 있으면 방향바꾸기
		{
			//cout << time << change[time] << endl;
			if (change[time] == 'L')
				nd == 0 ? nd = 3 : nd -= 1;
			else if (change[time] == 'D')
				nd == 3 ? nd = 0 : nd += 1; 

		}
		
		int nx = cx + dx[cd];
		int ny = cy + dy[cd];
		
		if (nx <= 0 || ny <= 0 || nx > N || ny > N || board[nx][ny] == 's')
			break;

		if (board[nx][ny] == 'a')
		{
			board[nx][ny] = 's';
			S.push_front({ nx,ny,nd });
		}
		else
		{
			board[nx][ny] = 's';
			S.push_front({ nx,ny,nd });
			int delx = S.back().x;
			int dely = S.back().y;
			board[delx][dely] = '\0';
			S.pop_back();
		}


	}


}
