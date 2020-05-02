//4:35~

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int Init[15][15];
int Eat[15][15];
vector<int> Map[15][15];
int N, M, K;
int dx[] = {-1,1,0,0,-1,-1,1,1};
int dy[] = {0,0,-1,1,-1,1,-1,1};
struct info { int x, y, age; };
vector<info>Die;

void Spring();
void Summer();
void Fall();
void Winter();
void Spread(int x, int y);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cin >> Init[i][j];
			Eat[i][j] = 5;
		}
	}
	for (int i = 0; i < M; i++)
	{
		int x, y, z;
		cin >> x >> y >> z;
		Map[x][y].push_back(z);
	}

	while (K--)
	{
		Spring();
		Summer();
		Fall();
		/*
		cout << "\n";
		for (int i = 1; i <= N; i++)
		{
			for (int j = 1; j <= N; j++)
			{
				cout << Eat[i][j] << " ";
			}
			cout << "\n";
		}*/
		Winter();
		
		
	}

	int Result = 0;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			//cout << Map[i][j].size() << " ";
			if (Map[i][j].empty())continue;
			Result += Map[i][j].size();
		}
		//cout << "\n";
	}


	cout << Result;

	return 0;
}

void Spring()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (Map[i][j].empty())continue;
			if (Map[i][j].size() >= 1)
			{
				vector<int>Tree;
				Tree = Map[i][j];
				Map[i][j].clear();

				sort(Tree.begin(), Tree.end());

				int idx = -1;
				for (int k = 0; k < Tree.size(); k++)
				{
					if (Eat[i][j] >= Tree[k])
					{
						Eat[i][j] -= Tree[k];
						Tree[k]++;
						idx = k;
						Map[i][j].push_back(Tree[k]);
					}
					else
						Die.push_back({ i,j,Tree[k] });
				}
				
				//cout << "\n";
			}
			else if (Map[i][j].size() == 1)
			{
				if (Eat[i][j] >= Map[i][j][0])
				{
					Eat[i][j] -= Map[i][j][0];
					Map[i][j][0]++;
				}
				else
				{
					Die.push_back({ i,j,Map[i][j][0] });
					Map[i][j].clear();
				}
			}
		
		}
	}

}

void Summer()
{
	if (Die.empty())return;
	for (int i = 0; i < Die.size(); i++)
	{
		int cx = Die[i].x;
		int cy = Die[i].y;
		int cage = Die[i].age;

		Eat[cx][cy] += (cage / 2);
	}
	Die.clear();
}

void Fall()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (Map[i][j].empty())continue;
			if (!Map[i][j].empty()) 
			{
				for (int k = 0; k < Map[i][j].size(); k++)
				{
					if (Map[i][j][k] % 5 == 0)
					{
						Spread(i, j);
					}
				}
			}
		}
	}
}

void Winter()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			Eat[i][j] += Init[i][j];
		}
	}

}

void Spread(int x, int y)
{

	for (int i = 0; i < 8; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx<=0 || ny<=0 || nx>N || ny>N)continue;
		Map[nx][ny].push_back(1);
	}
}
