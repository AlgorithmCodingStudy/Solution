#include<iostream>
#include<set>

using namespace std;

int N, M;
int T;
set<int>Truth;
bool check[55] = { false };
int Party[55][55];

void Check();

int main()
{
	cin >> N>> M;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int num;
		cin >> num;
		Truth.insert(num);
	}


	for (int i = 0; i < M; i++)
	{
		cin >> Party[i][0];
		for (int j = 1; j <= Party[i][0]; j++)
		{
			cin >> Party[i][j];
		}
	}

	for (int i = 0; i < M; i++) { //왜M번했는지는 몰겠지만 연결된애들 다 충분히 봐주려면 파티수만큼 돌려봐야한다고 생각..
		Check(); 
	}

	int cnt = 0;
	for (int i = 0; i < M; i++)
	{
		if (!check[i])cnt++; //거짓말할 있는 파티갯수세기
	}
	cout << cnt << endl;
	return 0;
}

void Check()
{
//이중포문돌면서 check가 false인 행(거짓말할수있는파티)나오면 continue;
//만약에 set에 들어있는 번호가 check가 false인 행에서 나오면 check = true; -->거짓말할 수 없는 파티로 바꿔줌
	for (int i = 0; i < M; i++)
	{
		if (check[i])continue;
		for (int j = 1; j <= Party[i][0]; j++)
		{
			if (Truth.find(Party[i][j]) != Truth.end()) {
				check[i] = true;
				break;
			}
		}
	}

	for (int i = 0; i < M; i++)
	{
		if (check[i]) //거짓말할 수 없는 파티에 참석한 사람들 모두 set에 넣기
		{
			for (int j = 1; j <= Party[i][0]; j++)
			{
				Truth.insert(Party[i][j]);
			}
		}
	}

}
