```c
#include <string>
#include <vector>
#include<stdlib.h>
#include<cmath>

using namespace std;

bool Prime[1000000];

void getPrime()
{
    Prime[0] = true;
    
    for(int i = 2; i <= sqrt(10000000); i++)
    {
        if(Prime[i] == true) continue;
        for(int j = i+i; j<10000000; j+=i)
        {
            if(Prime[i] == true)continue;
            Prime[j] = true; //true면 소수가 아님
        }
    }
}


int solution(string numbers) {
    int answer = 0;
    getPrime();
    
    int length = numbers.length();
    int num = atoi(numbers.c_str());
    
    
    
    return answer;
}
```
