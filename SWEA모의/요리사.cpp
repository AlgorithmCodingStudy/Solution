
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;


int N,T;
int team[25][25];
bool pick[25];
vector<int>result;

void ability();
void Recrusive(int idx, int cnt);

int main()
{
	cin >> T;
	for (int q = 1; q <= T; q++) {

		pick[25] = {false};
        for (int i = 1; i <= N; i++)
		{
			for (int j = 1; j <= N; j++)
			{
				team[i][j]=0;
			}
		}
		result.clear();

		//입력
		cin >> N;
		for (int i = 1; i <= N; i++)
		{
			for (int j = 1; j <= N; j++)
			{
				cin >> team[i][j];
			}
		}

		//팀정하기(재귀)
		Recrusive(1, 0);

		//결과값출력
		cout <<'#'<<q<<' '<< *min_element(result.begin(), result.end())<<"\n";
	}
	return 0;

}


void ability()
{
	vector<int>S, L;

	for (int i = 1; i <= N; i++)
	{
		if (pick[i] == true)
			S.push_back(i);
		else
			L.push_back(i);
	}

	int Stotal = 0, Ltotal = 0;
	for (int i = 0; i < S.size(); i++)
	{
		for (int j = 0; j < S.size(); j++)
		{
			if (i == j) continue;
			Stotal += (team[S[i]][S[j]]);
			Ltotal += (team[L[i]][L[j]]);
		}
	}

	result.push_back(abs(Ltotal - Stotal));
}


void Recrusive(int idx, int cnt)
{
	if (cnt == N / 2)
	{
		ability();
		return;
	}

	for (int i = idx; i <= N; i++)
	{
		if (pick[i] == true)continue;
		pick[i] = true;
		Recrusive(i + 1, cnt + 1);
		pick[i] = false;

	}

}
