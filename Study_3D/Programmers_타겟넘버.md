```c
#include <string>
#include <vector>
#include<iostream>
#include<algorithm>

using namespace std;
bool arr[21] ={0};
vector<string>result;
vector<string>ans;

void DFS(vector<int>numbers, int idx, int N, int hap, string a,int target)
{
    if(idx == N && target == hap)
    {
        result.push_back(a);
        return;
    }
    
    for(int i = idx; i<N; i++)
    {
        if(arr[i] == true)continue;
        arr[i] = true;
        DFS(numbers, idx+1,N, hap+numbers[i],a+"+",target);
        arr[i] = false;
        DFS(numbers, idx+1,N, hap-numbers[i],a+"-",target);
        
    }    
}


int solution(vector<int> numbers, int target) {
    
    int answer = 0;
   
    DFS(numbers,0,numbers.size(),0,"",target);
    sort(result.begin(),result.end());
    result.erase(unique(result.begin(),result.end()),result.end());
    
    answer = result.size();
    return answer;
}
```
