<img width="352" alt="dd" src="https://user-images.githubusercontent.com/29946480/70602851-aa5a1c80-1c38-11ea-918f-119e0df26f09.PNG">

### ???? core dump에러가뭘까요........................................................
    
     ==> 자신이 운영체제로부터 배정받지 못한 메모리영역에 대해 침법할 때 운영체제가 막아주는것이 세그먼트에러!
     
     EX1) 초기화 제대로 안해줬을 때
     
     EX2) 배열의 index에 변수사용했을때..?

     [ 참고 ] 
     
       https://terapi.tistory.com/entry/KLDP%ED%8E%8C-Segmentation-fault%EC%97%90-%EB%8C%80%ED%95%9C-%EC%89%BD%EA%B3%A0%EB%8F%84-%EB%A9%8B%EC%A7%84-%EC%84%A4%EB%AA%85 

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
    
   for(int i = idx; i < words.size(); i++) //idx에서 core dump에러 발생! 
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

--------------------------------------------------▽▽▽--------------------------------------------------------------

### 성공!


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

void DFS(string begin, string target, vector<string>words, int cnt)
{    
   if(begin == target)
   {
       result.push_back(cnt);
       return;
   }
    
   for(int i = 0; i < words.size(); i++)
   {
       if(check[i] == false) {
           string compare = words[i];
           if(can(compare,begin)== true)
           {
               check[i] = true;
               DFS(compare,target,words,cnt+1);  
               check[i] = false;
           }
     }
       
   }
   
}


int solution(string begin, string target, vector<string> words) {
    
    int answer = 0;
    
    for(int i = 0; i < words.size(); i++)
    {
        if(target == words[i]){
            available= true;
            break;
        }  
    }
    
    if(available == false){
        return 0;
    }
    
    DFS(begin,target,words,0);
    answer = *min_element(result.begin(),result.end());
    
    return answer;
}
```
