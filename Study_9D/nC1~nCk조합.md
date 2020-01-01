


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
