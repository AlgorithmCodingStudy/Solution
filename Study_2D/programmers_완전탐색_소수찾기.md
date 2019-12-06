```c
//틀림ㅠㅠ

#include <string>
#include <vector>
#include<cstring>
#include<iostream>
#include<cmath>

using namespace std;

bool Prime[1000000];
bool check[1000000];
vector<string>result;

void getPrime() //소수인지 판별하는 배열 작성하는함수
{
	Prime[0] = true;

	for (int i = 2; i <= sqrt(10000000); i++)
	{
		if (Prime[i] == true) continue;
		for (int j = i + i; j < 10000000; j += i)
		{
			if (Prime[i] == true)continue;
			Prime[j] = true; //true면 소수가 아님
		}
	}
}

void selectNum(string numbers, int idx, string a)
{
	if (idx == numbers.length())
	{
		result.push_back(a);
		return;
	}

	for (int i = idx; i < numbers.length(); i++)
	{
		if (check[i] == true)continue;
		check[i] = true;
		cout << numbers[i];
		selectNum(numbers, idx + 1, a + numbers[i]);
		check[i] = false;
		selectNum(numbers, idx + 1, a);
	}
}

int solution(string numbers) {

	int answer = 0;
	getPrime();

	cout << numbers.length();
	selectNum(numbers, 0, " ");
	for (int i = 0; i < result.size(); i++)
	{
		cout << result[i] << endl;
		int a = atoi(result[i].c_str());
		if (Prime[a] == false)
			answer++;
	}

	return answer;
}
int main()
{
	string numbers = "17";
	int re = solution(numbers);
	cout << re << endl;
	return 0;
}
```
