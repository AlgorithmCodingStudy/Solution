#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;


int T,numcnt;
int Num[15];
int oper[5];
vector<int>all;

void Select(int result,int nextidx);

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++)
	{
		//초기화
		memset(Num, 0, sizeof(Num));
		memset(oper, 0, sizeof(oper));
		all.clear();
		numcnt = 0;

		//입력
		cin >> numcnt;
		for (int i = 0; i < 4; i++)
		{
			cin >> oper[i];
		}
		for (int i = 0; i < numcnt; i++)
		{
			cin >> Num[i];
		}

		Select(Num[0],1);

		int mmax = *max_element(all.begin(), all.end());
		int mmin = *min_element(all.begin(), all.end());

		cout << '#'<<q<<' '<<mmax - mmin << "\n";

	}

	return 0;
}

void Select(int result,int nextidx)
{
	if (oper[0] == 0 && oper[1] == 0 && oper[2] == 0 && oper[3] == 0)
	{
		all.push_back(result);
		return;
	}

	if (oper[0] > 0)
	{
		oper[0]--;
		Select(result + Num[nextidx], nextidx + 1);
		oper[0]++;
	}

	if (oper[1] > 0)
	{
		oper[1]--;
		Select(result - Num[nextidx], nextidx + 1);
		oper[1]++;
	}

	if (oper[2] > 0)
	{
		oper[2]--;
		Select(result * Num[nextidx], nextidx + 1);
		oper[2]++;
	}

	if (oper[3] > 0)
	{
		oper[3]--;
		Select(result / Num[nextidx], nextidx + 1);
		oper[3]++;
	}

}
