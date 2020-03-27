#include<iostream>

using namespace std;

int N, M, H;
bool Ladder[35][15];
bool Stop;
int Ans = -1;

void addline(int cnt, int now, int idx);
bool CheckAns();

int main()
{

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M >> H;
	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		Ladder[a][b] = true;
	}
	

	for (int i = 0; i <= 3; i++) // 추가할 사다리 갯수
	{
		addline(i,0,1); //사다리 갯수, 현재 추가한 사다리갯수, 행번호

		if (Stop) {
			Ans = i;
			break;
		}
	}

	cout << Ans << endl;

	return 0;
}

void addline(int cnt, int now, int idx)
{
	if (cnt == now)
	{
		if (CheckAns()) {
			Stop = true;
			return;
		}

		else
			return;
	}


	for (int i = idx; i <= H; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (!Ladder[i][j] && !Ladder[i][j - 1] && !Ladder[i][j + 1])
			{
				Ladder[i][j] = true;
				addline(cnt, now + 1, i);
				if (Stop) break;
				Ladder[i][j] = false;
			}
		}
		if (Stop) break;
	}
}




bool CheckAns()
{
	
	for (int i = 1; i <= N; i++) //세로
	{
		int row = i;

		for (int j = 1; j <= H; j++)
		{
			if (Ladder[j][row])
				row++;
			else if (Ladder[j][row - 1])
				row--;
		}

		if (row != i) return false;
	}

	return true;
}
