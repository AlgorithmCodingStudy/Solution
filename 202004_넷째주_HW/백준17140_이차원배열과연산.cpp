//1시간20분
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

struct info {
	int num, cnt;
    bool operator <(const info& a)
	{
		if (cnt == a.cnt)
		{
			return num < a.num;
		}
		else
			return cnt < a.cnt;
	}
};
int r, c, k;
int Rcnt = 3; int Ccnt = 3;
int Map[110][110];
int Time;
vector<info>R;
vector<info>C;

void Play_R();
void Play_C();
void Print();

int main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> r >> c >> k;
	for (int i = 1; i <= 3; i++)
	{
		for (int j = 1; j <= 3; j++)
		{
			cin >> Map[i][j];
		}
	}

	while (1)
	{
		if (Time > 100)break;
		if (Map[r][c] == k)break;
		Time++;
		if (Rcnt >= Ccnt)
		{
			Play_R();
		}
		else if (Rcnt < Ccnt)
		{
			Play_C();
		}
		
	}

	if (Time > 100)cout << -1;
	else cout << Time;

	return 0;
}

void Play_R()
{
	int count[101] = { 0 };
	
	for (int i = 1; i <= Rcnt; i++)
	{
		R.clear();
		memset(count, 0, sizeof(count));
		int mmax = -1;

		for (int j = 1; j <= Ccnt; j++)
		{
			if (Map[i][j] == 0)continue;
			count[Map[i][j]]++;
			mmax = max(Map[i][j], mmax);
			Map[i][j] = 0;
		}
		
		for (int k = 1; k <=mmax; k++)
		{
			if (count[k] == 0)continue;
			R.push_back({ k,count[k] });
		}

		sort(R.begin(), R.end());

		int idx = 1;
		for (int j = 0; j < R.size(); j++)
		{
			Map[i][idx] = R[j].num;
			idx++;
			Map[i][idx] = R[j].cnt;
			idx++;
		}
		if (idx-1 > Ccnt)
			Ccnt =idx-1;
	}
}

void Play_C()
{
	int count[101] = { 0 };
	
	for (int i = 1; i <= Ccnt; i++)
	{
		C.clear();
		memset(count, 0, sizeof(count));
		int mmax = -1;

		for (int j = 1; j <= Rcnt; j++)
		{
			if (Map[j][i] == 0)continue;
			count[Map[j][i]]++;
			mmax = max(Map[j][i], mmax);
			Map[j][i] = 0;	
		}
		
		for (int k = 1; k <= mmax; k++)
		{
			if (count[k] == 0)continue;
			C.push_back({ k,count[k] });
		}

		sort(C.begin(), C.end());

		int idx = 1;
		for (int j = 0; j < C.size(); j++)
		{
			Map[idx][i] = C[j].num;
			idx++;
			Map[idx][i] = C[j].cnt;
			idx++;
		}

		if (idx-1 > Rcnt)
			Rcnt = idx-1;
	}

}

void Print()
{
	cout << endl;
	for (int i = 1; i <= Rcnt; i++)
	{
		for (int j = 1; j <= Ccnt; j++)
		{
			cout << Map[i][j] << " ";
		}
		cout << endl;
	}

	cout << endl;
}
