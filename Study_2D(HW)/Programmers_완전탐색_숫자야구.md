# 문제 링크

      https://programmers.co.kr/learn/courses/30/lessons/42841
      
-------------------------------------------------------------------------------------------------------------

```c
#include <string>
#include <vector>

using namespace std;

int split[3] = {0};
bool isright(vector<vector<int>> baseball)
{
    int base[3] = {0};
    for(int i = 0; i < baseball.size(); i++)
    {
        int strike = 0; 
        int ball = 0;
    
        int num = baseball[i][0];
        int a = num %100;
        base[0] = num / 100;
        base[1] = a /10;
        base[2] = a % 10;
        
        for(int j = 0; j < 3; j++)
        {
            if(split[j] == base[j]) strike++;
            for(int k = 0; k < 3; k++)
            {
                if(j == k) continue;
                if(split[j] == base[k]) ball++;
            }
        }
        
        if(baseball[i][1] != strike || baseball[i][2] != ball)
            return false;
    }
    return true;   
}

int solution(vector<vector<int>> baseball) {
    
    int answer = 0; 
    for(int i = 123; i <= 987; i++)
    {
        int a = i % 100;
        split[0] = i / 100;
        split[1] = a / 10;
        split[2] = a % 10;
        
        if(split[0] == split[1] || split[0] == split[2] || split[1] == split[2]) continue;
        if(split[0] == 0 || split[1] == 0 || split[2] == 0)continue;
        if(isright(baseball))
        {
            answer++;
        }
    }
    return answer;
}
```
