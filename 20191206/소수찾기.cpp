#include <string>
#include <vector>

using namespace std;

int solution(string numbers) {
    int answer = 0;
	vector<int> number;
          
        
          
          // 2~n
          for(int i=2; i<=n; i++) {
              number[i] = i;
          }
          
          //2,4,6... 0으로
          for(int i=2; i<=n; i++) {
              if(number[i]==0) continue;
              
              for(int j= 2*i; j<=n; j += i) {
                  number[j] = 0;
              }
          }
          
          
          for(int i=0; i<number.length; i++) {
              if(number[i]!=0) {
                  answer++;
              }
          }
          
          return answer;
}
