<img width="352" alt="dd" src="https://user-images.githubusercontent.com/29946480/70602851-aa5a1c80-1c38-11ea-918f-119e0df26f09.PNG">

### ???? core dump에러가뭘까요........................................................


-----------------------------------------------------------------------------------------------------------------------------

```c
#include <vector>
#include<string>
#include<algorithm>

using namespace std;

bool check[100] ={false,};
bool available = false;
vector<int>result;

bool can(string a, string begin)
{
    int count = 0;
    for(int i = 0; i < a.length(); i++)
    {
        if(begin[i] != a[i])
            count++;
    }
    
    if(count == 1)
        return true;
    
    return false;
    
}

void DFS(int idx, string begin, string target, vector<string>words, int cnt)
{    
   if(begin == target)
   {
       result.push_back(cnt);
       return;
   }
    
   for(int i = idx; i < words.size(); i++)
   {
       if(check[i] == false) {
       string compare = words.at(i);
       if(can(compare,begin)== true)
       {
           check[i] = true;
           DFS(i+1,compare,target,words,cnt+1);  
           check[i] = false;
       }
     }
       
   }
   
}


int solution(string begin, string target, vector<string> words) {
    
    int answer = 0;
    
    for(int i = 0; i < words.size(); i++)
    {
        if(target == words.at(i)){
            available= true;
            break;
        }  
    }
    
    if(available == false){
        return 0;
    }
    
    DFS(0,begin,target,words,0);
    answer = *min_element(result.begin(),result.end());
    
    return answer;
}
```
