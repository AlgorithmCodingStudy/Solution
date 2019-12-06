# 문제 링크

      https://programmers.co.kr/learn/courses/30/lessons/42840
      
--------------------------------------------------------------------------------------------------------------

### 접근 방법

1. answers의 사이즈를 기준으로 for문을 돌린다 (정답체크하는 for문)

2. 각 vector의 사이즈를 answers의 사이즈로 나눠서 반복하게 만든다.

    ** 2번 그림설명 **

--------------------------------------------------------------------------------------------------------------

```c
#include <string>
#include <vector>
#include <iostream>
#include<algorithm>

using namespace std;


vector<int> solution(vector<int> answers) {

	vector<int>Ans;

	vector<int>first = { 1,2,3,4,5 };
	vector<int>second = { 2,1,2,3,2,4,2,5 };
	vector<int>third = { 3,3,1,1,2,2,4,4,5,5 };

	int count[3] = { 0 };

	for (int i = 0; i < answers.size(); i++)
	{
		if (answers[i] == first[i % (first.size())])
			count[0]++;
		if (answers[i] == second[i % (second.size())])
			count[1]++;
		if (answers[i] == third[i % (third.size())])
			count[2]++;
	}


	int result = *max_element(count, count + 3);

	for (int i = 0; i < 3; i++)
	{
		if (result == count[i]) {
			Ans.push_back(i + 1);
		}
	}

	sort(Ans.begin(), Ans.end());

	return Ans;
}
```
