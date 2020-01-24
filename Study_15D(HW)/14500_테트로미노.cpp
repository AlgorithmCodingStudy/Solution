//완탐

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int map[550][550];
int N, M;
vector<int>result;


void cal_all(int shape);

int main()
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
		}
	}

	for (int i = 1; i <= 19; i++)
	{
		cal_all(i);
	}

	cout << *max_element(result.begin(), result.end());
	return 0;
}

void cal_all(int shape)
{

	if (shape == 1)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				
				if (i + 1 >= N || i + 2 >= N || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i + 1][j] + map[i + 2][j] + map[i + 2][j + 1]);
				result.push_back(hap);
			}
		}
	}
	else if (shape == 2)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				
				if (i + 1 >= N || j + 1 >= M || j + 2 >= M)continue;
				int hap = (map[i][j] + map[i + 1][j] + map[i][j + 1] + map[i][j + 2]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 3)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				
				if (i + 1 >= N || j + 1 >= M || i + 2 >= N)continue;
				int hap = (map[i][j] + map[i + 1][j + 1] + map[i + 2][j + 1] + map[i][j + 1]);
				result.push_back(hap);
			}
		}
	}
	else if (shape == 4)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || j + 1 >= M || j + 2 >= M)continue;
				int hap = (map[i + 1][j] + map[i + 1][j + 1] + map[i + 1][j + 2] + map[i][j + 2]);
				result.push_back(hap);
			}
		}
	}
	
	else if (shape == 5)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (j + 1 >= M || j + 2 >= M || j + 3 >= M)continue;
				int hap = (map[i][j] + map[i][j + 1] + map[i][j + 2] + map[i][j + 3]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 6)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				
				if (i + 1 >= N || i + 2 >= N || i + 3 >= N)continue;
				int hap = (map[i][j] + map[i+1][j] + map[i+2][j] + map[i+3][j]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 7)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				
				if (j + 1 >= M || i+1 >= N)continue;
				int hap = (map[i][j] + map[i][j + 1] + map[i+1][j] + map[i+1][j + 1]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 8)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				
				if (i + 1 >= N || i + 2 >= N || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i+1][j] + map[i+1][j + 1] + map[i+2][j + 1]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 9)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				
				if (i + 1 >= N || j + 2 >= M || j + 1 >= M)continue;
				int hap = (map[i+1][j] + map[i][j+1] + map[i][j + 2] + map[i + 1][j + 1]);
				result.push_back(hap);
			}
		}
	
	}

	else if (shape == 10)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || j + 2 >= M || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i][j + 1] + map[i+1][j + 2] + map[i + 1][j + 1]);
				result.push_back(hap);
			}
		}

	}

	else if (shape == 11)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || i + 2 >= N || j + 1 >= M)continue;
				int hap = (map[i+1][j] + map[i + 1][j+1] + map[i+2][j] + map[i][j + 1]);
				result.push_back(hap);
			}
		}
	}


	else if (shape == 12)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || j + 2 >= M || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i + 1][j+1] + map[i][j + 1] + map[i][j + 2]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 13)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || i + 2 >= N || j + 1 >= M)continue;
				int hap = (map[i+1][j] + map[i][j + 1] + map[i+1][j + 1] + map[i+2][j + 1]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 14)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || j + 2 >= M || j + 1 >= M)continue;
				int hap = (map[i+1][j] + map[i + 1][j + 1] + map[i][j + 1] + map[i+1][j + 2]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 15)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || i + 2 >= N || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i + 1][j + 1] + map[i+1][j] + map[i+2][j]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 16)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || i + 2 >= N || j + 1 >= M)continue;
				int hap = (map[i+2][j] + map[i + 2][j + 1] + map[i+1][j + 1] + map[i][j+1]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 17)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || j + 2 >= M || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i + 1][j] + map[i+1][j + 1] + map[i+1][j + 2]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 18)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || i + 2 >= N || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i + 1][j] + map[i + 2][j] + map[i][j + 1]);
				result.push_back(hap);
			}
		}
	}

	else if (shape == 19)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (i + 1 >= N || j + 2 >= M || j + 1 >= M)continue;
				int hap = (map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j + 2]);
				result.push_back(hap);
			}
		}
	}

}
