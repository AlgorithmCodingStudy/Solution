#include <string>
#include <vector>

using namespace std;

int hap = 0;
int cnt = 0;

void bfs(vector<int> numbers,int idx,int target){
    int size = numbers.size();
    if(idx == size) return; 
    hap += numbers[idx];
    
    
    int next = idx +1;
    bfs(numbers,next,target);
    numbers[next] *= -1;
    bfs(numbers,next,target);
    
   
    
    if(idx == size){
        if(hap == target) cnt++;
    }
    
    
    
    
    
            
}

/*
//배열 선언하는 것도
void bfs(vector<int>& numbers, int hap, int target, int depth){
    
    if(depth ==numbers.size()){
        if(hap == target) {
            cnt++;
                 
        }
        return; 
    }    
        bfs(numbers,hap+numbers[depth],target,depth+1);
        bfs(numbers,hap-numbers[depth],target,depth+1);
        
    
    
    
}
*/
int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    
    int size = numbers.size();
    int idx = 0;
    
    bfs(numbers,size,target);
    /*
    bfs(numbers,numbers[0],target,1);
    bfs(numbers,numbers[0]*(-1),target,1);
    */

    answer= cnt;
    
    
    return answer;
}
