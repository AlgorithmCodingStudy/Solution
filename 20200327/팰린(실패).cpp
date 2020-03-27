#include<iostream>
#include<string>

using namespace std;

string Name;
bool impossible;

void Search(int idx);
bool CheckPal();

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> Name;

	Search(0);

	if (!impossible) cout << "I'm Sorry Hansoo";

	return 0;
}


void Search(int idx)
{

	if (CheckPal()) {
		impossible = true;
		cout << Name;
		return;
	}
	//else return;

	for (int i = idx; i < Name.length() - 1; i++)
	{
		if (Name[i] != Name[i + 1])
		{
			swap(Name[i], Name[i + 1]);
			Search(i + 1);
			if (impossible)break;
			swap(Name[i], Name[i + 1]);
		}
	}
}

bool CheckPal()
{
	int len = Name.length();
	int idx = len / 2;

	for (int i = 0; i < idx; i++)
	{
		if (Name[i] != Name[len - 1 - i]) return false;
	}

	return true;
}
