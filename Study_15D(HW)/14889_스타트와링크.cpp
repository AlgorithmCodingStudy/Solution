/*
1.1~N까지 재귀로 조합짜기(중복허용불가)
2. 팀별로 능력치 구해서 차이값을 벡터에 저장
3. 벡터에서 최솟값출력
*/
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int N;
int team[25][25];
bool pick[25];
vector<int>result;

void ability();
void Recrusive(int idx, int cnt);

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
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
	cout << *min_element(result.begin(), result.end());

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

	int Stotal = 0,Ltotal = 0;
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
		Recrusive(i+1, cnt + 1);
        pick[i] = false;
        
	}

}
