#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct Dist { int x, y; };
int N, M;
int Map[55][55];
Dist Sel_C[20];

vector<Dist>Chicken;
vector<Dist>House;
vector<int>Result;

void Select_chicken(int idx, int cnt);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> Map[i][j];
			if (Map[i][j] == 1) House.push_back({ i,j });
			else if (Map[i][j] == 2)Chicken.push_back({ i,j });
		}
	}
	
	Select_chicken(0,0);

	cout << *min_element(Result.begin(), Result.end());

	return 0;
}

void Select_chicken(int idx, int cnt)
{
	if (cnt == M)
	{
		int City_Dist = 0;
		for (int i = 0; i < House.size(); i++)//집
		{
			vector<int>Chicken_Dist;

			int Hcx = House[i].x;
			int Hcy = House[i].y;

			for (int j = 0; j < cnt; j++)//치킨
			{
				int Ccx = Sel_C[j].x;
				int Ccy = Sel_C[j].y;
				Chicken_Dist.push_back( abs(Hcx - Ccx) + abs(Hcy - Ccy));
			}
			City_Dist += *min_element(Chicken_Dist.begin(), Chicken_Dist.end());
		}

		Result.push_back(City_Dist);
		return;
	}

	for (int i = idx; i < Chicken.size(); i++)
	{
		if (Sel_C[i].x != 0 && Sel_C[i].y != 0)continue;
		Sel_C[cnt] = { Chicken[i].x,Chicken[i].y };
		Select_chicken(i + 1, cnt + 1);
		Sel_C[cnt] = { 0,0 };
	}

}
