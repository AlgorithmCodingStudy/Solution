# 문제 링크
           https://www.acmicpc.net/problem/17450
	   
------------------------------------------------------------------------------------------------------------------------------------

## double형 나눗셈 이용

------------------------------------------------------------------------------------------------------------------------------------

### 접근방법

1. 구조체를 이용해 S, N, U의 정보를 저장(가격, 무게순)

2. 최고의 가성비를 구하기 위해 함수를 만들어 계산

    ㄱ. 각 가격, 무게에 10을 곱한다
    
    ㄴ. 가격 계산값이 5000이상이면 500원을 뺀다 (할인조건 만족)
    
    ㄷ. duble형 변수 result에 S,N,U의 가성비를 계산한 결과 값을 저장.
    
    ㄹ. result값을 저장하면서 max값도 같이 구한다 
         //이때, max값이 바뀌면 바뀐 index번호를 R변수에 저장(가성비 제일 좋은 과자이름 출력하기 위해)
    
3. R의 값에 따라 답을 출력
    
------------------------------------------------------------------------------------------------------------------------------------  

```c
#include<iostream>
#include<algorithm>

using namespace std;

struct info {
	int price,weight;
	double result;
};



int calBest(info A[])
{
	info Ten[3];

	for (int i = 0; i < 3; i++)
	{
		Ten[i].price = A[i].price * 10;
		Ten[i].weight = A[i].weight * 10;

		if (Ten[i].price > 5000 || Ten[i].price == 5000)
		{
			Ten[i].price -= 500;
		}
	}
	
	double max = -999999;
	int R = -99999;
	

	for (int i = 0; i < 3; i++)
	{
		Ten[i].result = ((double)Ten[i].weight / (double)Ten[i].price);
		
		
		if (Ten[i].result > max) 
		{
			max = Ten[i].result;
			R = i;
		}
	}

	return R;
}



int main()
{
	info A[3];

	for (int i = 0; i < 3; i++)
	{
		cin >> A[i].price >> A[i].weight;
	}

	int R = calBest(A);
		
	if (R == 0)
		cout << 'S' << "\n";
	else if (R == 1)
		cout << 'N' << "\n";
	else if (R == 2)
		cout << 'U' << "\n";

	return 0;
}
```
