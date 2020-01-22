//정답

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N, M, K;
int caneat[15][15] = { 0 };
int init_map[15][15] = { 0 };
vector<int>tree[15][15];
vector<int>alive[15][15];
struct treeinfo { int x, y, age; };
vector<treeinfo>D;

void spring();
void summer();
void fall();
void winter();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cin >> caneat[i][j];
			init_map[i][j] = 5;
		}
	}

	for (int i = 0; i < M; i++)
	{
		int x, y, z;
		cin >> x >> y >> z;
		tree[x][y].push_back(z);
	}

	while (K--)
	{
		spring();
		summer();
		fall();
		winter();
	}

	int count = 0;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (tree[i][j].size() == 0)continue;
			for (int k = 0; k < tree[i][j].size(); k++)
			{
				count++;
			}
		}
	}

	cout << count;

	return 0;
}

void spring()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (tree[i][j].size() == 0)continue;
			sort(tree[i][j].begin(), tree[i][j].end());

			for (int k = 0; k < tree[i][j].size(); k++) 
			{
				int nowtree = tree[i][j][k];
				
				if (init_map[i][j] >= nowtree)
				{
					init_map[i][j] -= nowtree;
					alive[i][j].push_back(nowtree+1);
				}
				else
				{
					D.push_back({ i,j,nowtree });
				}
			}
			tree[i][j].clear();
		}
	}
}

void summer()
{
	if (D.size() > 0)
	{
		for (int i = 0; i < D.size(); i++) {
			int x = D[i].x;
			int y = D[i].y;
			int age = D[i].age;
			init_map[x][y] += age / 2;
		}
	}
	D.clear();
	
}

void fall()
{
	int dx[] = { -1,-1,0,1,1,1,0,-1 };
	int dy[] = { 0,1,1,1,0,-1,-1,-1 };

	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (alive[i][j].size() == 0)continue;
			for (int k = 0; k < alive[i][j].size(); k++)
			{
				int nowtree = alive[i][j][k];

				tree[i][j].push_back(nowtree);

				if ((nowtree % 5) == 0)
				{
					for (int a = 0; a < 8; a++) {

						int nx = i + dx[a];
						int ny = j + dy[a];

						if (nx <1 || ny <1 || nx > N || ny > N)continue;

						tree[nx][ny].push_back(1);
					}
				}
			}
			alive[i][j].clear();
		}
	}
}

void winter()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			init_map[i][j] += caneat[i][j];
		}
	}
}


