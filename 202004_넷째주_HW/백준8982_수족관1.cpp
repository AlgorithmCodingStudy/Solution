#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct info { int y, x; };
struct info2 { int y, depth;
bool operator<(const info2& a)
{
	return depth < a.depth;
}
};// y1,y2,depth
int N, K;
int Sujo[40100];
int Out[40100];
vector<info>Spot;
vector<info2>Hole; 

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int y, x;
		cin >> y >> x;
		Spot.push_back({ y,x });
	}

	int idx = 0;
	for (int i = 2; i < Spot.size(); i++)
	{
		if (i % 2 == 0) {

			int count = Spot[i].y - Spot[i - 1].y;

			while (count--)
			{
				Sujo[idx] = Spot[i].x;
				idx++;
			}
		}
	}
	/*
	for (int i = 0; i < idx; i++)
	{
		cout << Sujo[0][i] << " ";
	}*/
	cin >> K;
	for (int i = 0; i < K; i++)
	{
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		Out[a] = b;
		Hole.push_back({a,b});
	}

	sort(Hole.begin(), Hole.end());

	for (int i = 0; i < Hole.size(); i++)
	{
		int now = Hole[i].y;
		int cutline = Hole[i].depth;

		for (int j = now - 1; j >= 0; j--)
		{
			if (Sujo[j] >= cutline) {
				if (Out[j] == 0)
					Out[j] = cutline;
				else
					Out[j] = max(Out[j], cutline);
			}
			else if (Sujo[j] < cutline)
			{
				cutline = Sujo[j];
				if (Out[j] == 0)
					Out[j] = cutline;
				else
					Out[j] = max(Out[j], cutline);
			}
		}


		cutline = Hole[i].depth;
		for (int j = now + 1; j <idx; j++)
		{
			if (Sujo[j] >= cutline) {
				if (Out[j] == 0)
					Out[j] = cutline;
				else
					Out[j] = max(Out[j], cutline);
			}
			else if (Sujo[j] < cutline)
			{
				cutline = Sujo[j];
				if (Out[j] == 0)
					Out[j] = cutline;
				else
					Out[j] = max(Out[j], cutline);
			}
		}
	}

	int Result = 0;
	for (int i = 0; i < idx; i++)
	{
		Result += (Sujo[i] - Out[i]);
	}

	cout << Result;
	return 0;
}
