#include<iostream>
#include<queue>
#include<cstring>

using namespace std;

struct info { int x, y, dust; };
int Ux, Uy, Dx, Dy;

int R, C, T;
int Room[1010][1010];
int Cpy[1010][1010];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
bool first;

queue<info>Q;

void Spread_Dust();
void Action_Cleaner();
void Calculate_Dust();
void Input_Info();


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> R >> C >> T;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> Room[i][j];
			if (Room[i][j] == -1 && !first) { //방정보 입력받으면서 공기청정기의 아래,위의 위치 갱신
				Ux = i;
				Uy = j;
				first = true;
			}
			else if (Room[i][j] == -1 && first)
			{
				Dx = i;
				Dy = j;
			}
		}
	}
 
	while (T--) { //T시간만큼 미세먼지 퍼지고 공기청정기돌리고 반복

		Input_Info(); //미세먼지 퍼트리기위해 큐에 현재방에있는 미세먼지들 모두 저장

		Spread_Dust(); //미세먼지 퍼트리기

		Action_Cleaner(); //공기청정기돌리기

	}

	Calculate_Dust(); //남은 미세먼지수 세주기

	return 0;
}

void Spread_Dust()
{
	while (!Q.empty())
	{
		int cx = Q.front().x;
		int cy = Q.front().y;
		int cdust = Q.front().dust;
		int spread_dust = cdust / 5; //퍼질미세먼지는 초기에미세먼지양의 / 5
		Q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if (nx < 0 || ny < 0 || nx >= R || ny >= C)continue;
			if (Room[nx][ny] != -1) //미세먼지가 퍼질수 있으면
			{
				Room[nx][ny] += spread_dust; //다음칸에 미세먼지 더해주고
				Room[cx][cy] -= spread_dust; //현재칸의 미세먼지 빼줌
			}
		}
	}
}


void Action_Cleaner()
{
	memcpy(&Cpy, &Room, sizeof(Room)); //먼지를 이동할 맵을 따로 생성해 방의 정보 복사

	queue<int>Up;
	queue<int>Down;

	//윗값넣기
	for (int y = 1; y <= C - 1; y++)
		Up.push(Room[Ux][y]);
	
	for (int x = Ux - 1; x >= 0; x--)
		Up.push(Room[x][C - 1]);

	for (int y = C - 2; y >= 0; y--)
		Up.push(Room[0][y]);

	for (int x = 1; x <= Ux - 1; x++)
		Up.push(Room[x][0]);

	//아래값넣기
	for (int y = 1; y <= C - 1; y++)
		Down.push(Room[Dx][y]);

	for (int x = Dx + 1; x <= R-1; x++)
		Down.push(Room[x][C - 1]);

	for (int y = C - 2; y >= 0; y--)
		Down.push(Room[R-1][y]);

	for (int x = R-2; x >= Dx+1; x--)
		Down.push(Room[x][0]);

	
	//위
	for (int y = 2; y <= C - 1 && !Up.empty(); y++) { //y==2부터시작! && !Up.empty()조건 안걸어주면 오류남
		Cpy[Ux][y] = Up.front(); 
		Up.pop();
	}

	for (int x = Ux - 1; x >= 0 && !Up.empty(); x--) {
		Cpy[x][C - 1] = Up.front();
		Up.pop();
	}

	for (int y = C - 2; y >= 0 && !Up.empty(); y--){
		Cpy[0][y] = Up.front();
		Up.pop();
	}

	for (int x = 1; x <= Ux - 1 && !Up.empty(); x++) {
		Cpy[x][0] = Up.front();
		Up.pop();
	}
	
	//아래
	for (int y = 2; y <= C - 1 && !Down.empty(); y++) //y==2부터시작 && !Down.empty()조건 안걸어주면 오류남
	{
		Cpy[Dx][y] = Down.front();
		Down.pop();
	}
	
	for (int x = Dx + 1; x <= R - 1 && !Down.empty(); x++)
	{
		Cpy[x][C - 1] = Down.front();
		Down.pop();
	}
	
	for (int y = C - 2; y >= 0 && !Down.empty(); y--)
	{
		Cpy[R - 1][y] = Down.front();
		Down.pop();
	}
	
	for (int x = R - 2; x >= Dx + 1 && !Down.empty(); x--)
	{
		Cpy[x][0] = Down.front();
		Down.pop();
	}
  
	Cpy[Dx][1] = 0; //공기청정기에서 바람이 시작하는칸은 0으로 초기화! 먼지 밀렸으니까
	Cpy[Ux][1] = 0;

	memcpy(&Room, &Cpy, sizeof(Cpy)); //이동한 먼지들 다시 방에 복사
}


void Input_Info()
{
	while (!Q.empty())
	{
		Q.pop(); //큐초기화 (전역변수)
	}

	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (Room[i][j] > 0) //방이 0보다크면 미세먼지 (저장)
				Q.push({ i,j,Room[i][j] });
		}
	}

}

void Calculate_Dust() //남아있는 미세먼지양 출력
{
	int Answer = 0;
	
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (Room[i][j] > 0)
				Answer += Room[i][j]; 
		}
	}

	cout << Answer << "\n";
}
