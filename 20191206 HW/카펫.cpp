#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;
    
    int len = b + r;
    
    for (int i = 3; i <len; i++) {
        if (len % i == 0) {
            int  j = len / i;
            if ((((2 * i) + (2 * j) - 4) == b) && len - b == r) {
                answer.push_back(j); 
                answer.push_back(i);
                break;
            }
            }
        }
    
    return answer;
}
