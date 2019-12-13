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
