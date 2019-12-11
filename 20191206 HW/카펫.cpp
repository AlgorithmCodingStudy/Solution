#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;
    int length = brown + red;
    for (int i = 3; i <length; i++) {
        if (length % i == 0) {
            int  j = length / i;
            if ((((2 * i) + (2 * j) - 4) == brown) && length - brown == red) {
                answer.push_back(j); answer.push_back(i);
                break;
            }
        }
    }
    return answer;
}
