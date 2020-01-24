/*
1. A배열의 가장 처음의 값을 초기값으로 설정
2. 재귀를 통해 연산자의 값이 0이아닌 연산자를 계산
3. 계산된 값을 벡터에 넣고 최소최대 구하기
*/

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N;
int A[110];
int oper[4];
vector<int>result;


void Recursive(int hap, int idx);

int main()
{
	//입력
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> A[i];
	}
	for (int i = 0; i < 4; i++)
	{
		cin >> oper[i];
	}

	
	Recursive(A[0], 1);

	cout << *max_element(result.begin(), result.end())<<"\n";
	cout << *min_element(result.begin(), result.end())<<"\n";

	return 0;
}

void Recursive(int hap, int idx)
{
	if (oper[0] == 0 && oper[1] == 0 && oper[2] == 0 && oper[3] == 0)
	{
		result.push_back(hap);
		return;
	}

	if (oper[0] > 0)
	{
		oper[0]--;
		Recursive(hap + A[idx],idx + 1);
		oper[0]++;
	}

	if (oper[1] > 0)
	{
		oper[1]--;
		Recursive(hap - A[idx],idx + 1);
		oper[1]++;
	}

	if (oper[2] > 0)
	{
		oper[2]--;
		Recursive(hap *A[idx],idx + 1);
		oper[2]++;
	}

	if (oper[3] > 0)
	{
		oper[3]--;
		if (hap < 0)
		{
			Recursive((abs(hap)/ A[idx]) * -1,  idx + 1);
		}
		else
			Recursive(hap / A[idx],  idx + 1);
		
		oper[3]++;
	}

}
