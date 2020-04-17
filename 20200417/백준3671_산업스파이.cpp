#include<iostream>
#include<math.h>
#include<string>
#include<set>
#include<cstring>

using namespace std;

int c,result;
string num;
bool Sosu[10000000];
bool check[10];
set<int>Result;

void Select(int cnt, int Choicenum, string ans);
void Erathos();

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	Erathos();

	cin >> c;
	for (int i = 0; i < c; i++)
	{
		result = 0;
		num = "";
		Result.clear();

		cin >> num;

		
		for (int j = 1; j <= num.length(); j++) //nC1~nCn
		{
			Select(0, j,"");
		}
		
		set<int>::iterator iter;
		for (iter =Result.begin(); iter != Result.end(); iter++)
		{
			if (!Sosu[*iter])result++;
		}
		cout << result<<endl;
	}
	return 0;
}


void Erathos()
{
	Sosu[0] = Sosu[1] = true;
	for (int i = 2; i < sqrt(10000000); i++)
	{
		if (Sosu[i])continue;
		for (int j = i + i; j < 10000000; j+=i)
		{
			if (Sosu[j])continue;
			Sosu[j] = true;
		}
	}
}

void Select(int cnt, int Choicenum, string ans)
{
	if (cnt == Choicenum)
	{
		if (ans[0] == '0') {
			string A; int idx = 0;
			for (int i = 0; i < ans.length(); i++)
			{
				if (ans[i] != '0')
				{
					idx = i;
					break;
				}
			}
			for (int j = idx; j < ans.length(); j++)
			{
				A += ans[j];
			}
			Result.insert(atoi(A.c_str()));
		}
		else {
			Result.insert(atoi(ans.c_str()));
		}
		return;
	}

	for (int i = 0; i < num.length(); i++)
	{
		if (check[i])continue;
		check[i] = true;
		Select(cnt + 1, Choicenum, ans+num[i]);
		check[i] = false;
	}

}
