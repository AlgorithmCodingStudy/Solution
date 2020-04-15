#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int n;
bool check[220];
int Sang[110];
int Geun[110];
int Play = -1;

void pick_sang();
void pick_geun();
bool play_stop();

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> Sang[i];
		check[Sang[i]] = true;
	}

	int cnt = 0;
	for (int i = 1; i <= 2*n; i++)
	{
		if (!check[i]) {
			Geun[cnt] = i;
			cnt++;
		}
	}

	sort(Sang, Sang + n);
	sort(Geun, Geun + n);


	while (!play_stop())
	{
	
		pick_sang();
        if(play_stop())break; //이거때매 틀렸었음!(상근이 고르고 끝날수도있어서)
		pick_geun();
	}


	int Scnt = 0;
	int Gcnt = 0;

	for (int i = 0; i < n; i++)
	{
		if (Sang[i] > 0) Scnt++;
		if (Geun[i] > 0) Gcnt++;
	}

	cout << Gcnt << endl;
	cout << Scnt << endl;
	return 0;
}

void pick_sang()
{
	if (Play == -1)
	{
		for (int i = 0; i < n; i++)
		{
			if (Sang[i] > 0)
			{
				Play=Sang[i];
				Sang[i] = 0;
				break;
			}
		}
	}
	else
	{
		bool can = false;
		int now = 0;

		for (int i = 0; i < n; i++)
		{
			if (Sang[i] > 0)
			{
				now = Sang[i];
				if (Play < now) 
				{
					Sang[i] = 0;
					Play=now;
					can = true;
					break;
				}
			}
		}

		if (!can)
		{
			Play = -1;
		}

	}
}

void pick_geun()
{
	
	if (Play == -1)
	{
		for (int i = 0; i < n; i++)
		{
			if (Geun[i] > 0)
			{
				Play=Geun[i];
				Geun[i] = 0;
				break;
			}
		}
	}
	else
	{
		bool can = false;
		int now = 0;

		for (int i = 0; i < n; i++)
		{
			if (Geun[i] > 0) {
				now = Geun[i];
				if (Play < now)
				{
					Geun[i] = 0;
					Play=now;
					can = true;
					break;
				}
			}
		}

		if (!can)
		{
			Play = -1;
		}
	}
}



bool play_stop()
{
	int Scnt = 0;
	int Gcnt = 0;

	for (int i = 0; i < n; i++)
	{
		if (Sang[i] > 0) Scnt++;
		if (Geun[i] > 0) Gcnt++;
	}

	if (Scnt == 0 || Gcnt == 0) return true;

	return false;
}
