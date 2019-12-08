# 문제 링크

	https://programmers.co.kr/learn/courses/30/lessons/42842
	
-------------------------------------------------------------------------------------------------------------------------------


```c
#include <string>
#include <vector>
#include<iostream>

using namespace std;

vector<pair<int, int>>R;

vector<int> solution(int brown, int red) {

	vector<int> answer;
	int resultSize = brown + red; //카펫 크기

	for (int row = 1; row <= red; row++) //중간에 들어가는 빨간색을 col * row로 나타낸다.
	{
		if (red % row == 0) 
		{
			int col = red / row; 
			if (col < row)continue;
			R.push_back({ col+2,row+2 }); 
		}
	}
	
	for (int i = 0; i < R.size(); i++)
	{
  
		int result = R[i].first * R[i].second; //빨강_col+2 * 빨강_row+2 는 전체카펫의 크기여야함!
		if (result == resultSize)
		{
			answer.push_back(R[i].first);
			answer.push_back(R[i].second);
			break;
		}
    
	}
  
	return answer;
}
```
