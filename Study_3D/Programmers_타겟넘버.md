### //실패

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
    if(idx == N && target == hap) //시간초과
    {
        result.push_back(a);
        return;
    }
    
    for(int i = idx; i<N; i++) //==> for문때매 중복되는 값이 생김!
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

### //성공
```c
#include <string>
#include <vector>
#include<iostream>
#include<algorithm>

using namespace std;
bool arr[21] ={false};
vector<int>result;

void DFS(vector<int>numbers, int idx, int N, int hap,int target)
{
    if(idx == N)
    {
        if(target == hap)
            result.push_back(hap);
        return;
    }
    
   if(arr[idx] == false){
        arr[idx] = true;
        DFS(numbers, idx+1,N, hap+numbers[idx],target);
        arr[idx] = false;
        DFS(numbers, idx+1,N, hap-numbers[idx],target);
   }
}


int solution(vector<int> numbers, int target) {
    
    int answer = 0;
   
    DFS(numbers,0,numbers.size(),0,target);
    
    answer = result.size();
    
    return answer;
}
```
