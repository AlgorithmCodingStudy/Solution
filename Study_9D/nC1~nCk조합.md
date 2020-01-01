# nC1 ~ nCk 조합

```c
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int arr[5] = { 0 };
int tmp[5] = {0};

int main()
{


	for (int i = 0; i < 5; i++)
	{
		arr[i] = i+1;
	}

	memset(tmp, 1, sizeof(tmp));


	for (int i = 0; i < 5; i++)
	{
  
		tmp[i] = 0; 

		do {
			for (int j = 0; j < 5; j++)
			{
				if (tmp[j] == 0)
				{
					cout << arr[j]<< " ";
				}
			}
			cout << "\n";
		} while (next_permutation(tmp, tmp + 5));
	}


	return 0;
}

```
---------------------------------------------------------------------------------------------------------------------------

### 실행결과

<img width="200" alt="조합1" src="https://user-images.githubusercontent.com/29946480/71638943-82e2f680-2cb0-11ea-989d-6b517890e993.PNG">
<img width="200" alt="조합2" src="https://user-images.githubusercontent.com/29946480/71638944-837b8d00-2cb0-11ea-96a5-0ecda7691438.PNG">
